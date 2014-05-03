import collections
from header_common import *
from header_operations import *
from header_triggers import *
import process_common as pc
import header_lazy_evaluation as lazy
import module_info

remove_opmask = 0xffffffff

class LocalVariables:
  """Manages local variable mapping to numbers."""

  def __init__(self):
    self.variables = {}
    self.number = 0
    self.limit = 128

  def add_id(self, name, uses=0):
    id_uses = self.variables.setdefault(name, [self.number, 0])
    if id_uses[0] == self.number:
      self.number += 1
    if uses > 0:
      id_uses[1] += uses
    if self.limit is not None and self.number >= self.limit:
      pc.ERROR("new local variable '%s' exceeds the maximum count of %d per operations block" % (name, self.limit))
    return self.opmask|id_uses[0]

  def get_id(self, name):
    try:
      id_uses = self.variables[name]
      id_uses[1] += 1
      return self.opmask|id_uses[0]
    except KeyError:
      pc.ERROR("local variable '%s' used uninitialized" % name)

  def warn_unused(self, location):
    for name, id_uses in self.variables.iteritems():
      if id_uses[1] == 0 and not name.startswith("unused"):
        pc.WARNING("variable '%s' never used" % name, entry=location)

  opmask = opmask_local_variable

class GlobalVariables(LocalVariables):
  """Manages global variable loading, saving, and mapping to numbers."""

  def __init__(self):
    LocalVariables.__init__(self)
    self.variables = collections.OrderedDict()
    self.limit = None

  def load_old(self):
    try:
      with open("variables.txt", "r") as old_file:
        for name in old_file:
          name = name.strip()
          if name:
            self.add_id(name, uses=1)
    except EnvironmentError:
      pass

  def write(self):
    with open(module_info.export_path("variables.txt"), "wb") as var_file:
      for name, id_uses in self.variables.iteritems():
        var_file.write("%s\r\n" % name)

  opmask = opmask_variable

class QuickStrings:
  """Manages quick string loading, saving, and mapping to numbers."""

  def __init__(self):
    self.quick_strings = collections.OrderedDict()
    self.number = 0

  def add_str(self, sentence):
    full_id = pc.convert_to_identifier(sentence)
    sentence = pc.replace_spaces(sentence)
    id_len = min(len(full_id), 20)
    id_str = full_id[:id_len]
    duplicate_number = 1
    result = None
    while result is None:
      num_str = self.quick_strings.setdefault(id_str, [self.number, sentence])
      if num_str[0] == self.number:
        result = self.number
        self.number += 1
      elif num_str[1] == sentence:
        result = num_str[0]
      elif id_len < len(full_id):
        id_len += 1
        id_str = full_id[:id_len]
      else:
        id_str = "%s%d" % (full_id, duplicate_number)
        duplicate_number += 1
    return opmask_quick_string|result

  def load_old(self):
    try:
      with open("quick_strings.txt", "r") as old_file:
        for line in old_file:
          id_str = line.partition(" ")
          if id_str[0].startswith("qstr_") and id_str[2]:
            self.quick_strings[id_str[0][5:]] = [self.number, str.strip(id_str[2])]
            self.number += 1
    except EnvironmentError:
      pass

  def write(self):
    with open(module_info.export_path("quick_strings.txt"), "wb") as f:
      f.write("%d\r\n" % len(self.quick_strings))
      for id_str, num_str in self.quick_strings.iteritems():
        f.write("qstr_%s %s\r\n" % (id_str, num_str[1]))


class IdentifierMap:
  """Maps text identifiers for different types of module data to numbers."""

  def __init__(self):
    self.tag_map = {}

  def load_ids(self, tag, data, opmask):
    if not tag in self.tag_map:
      self.tag_map[tag] = {}
    id_map = self.tag_map[tag]
    for i, entry in enumerate(data):
      try:
        name = entry[0]
      except TypeError:
        pc.ERROR("'%s' entry number %d, '%s': has no valid identifier field" % (tag, i, entry))
      pc.assert_valid_identifier(name, entry=entry, tag=tag)
      if name in id_map:
        pc.ERROR("duplicate identifier '%s_%s'" % (tag, name))
      id_map[name] = opmask|i

  def get_id(self, tag, name, opmask=False):
    try:
      id_no = self.tag_map[tag][name]
      return id_no if opmask else id_no & remove_opmask
    except KeyError:
      pc.ERROR("identifier '%s_%s' not found" % (tag, name))

class Processor:
  """Compiles operation blocks in module data to the numbers in the module text files."""

  def __init__(self, global_variables, quick_strings, identifier_map, write_id=False, show_backtrace=False):
    self.global_variables = global_variables
    self.quick_strings = quick_strings
    self.identifier_map = identifier_map
    self.write_id = write_id
    self.show_backtrace = show_backtrace

  def process_id(self, param, tag=None):
    if isinstance(param, str):
      tag_name = param.partition("_")
      if tag and tag_name[0] != tag:
        pc.ERROR("identifier '%s_%s' is the wrong type: %s required" % (tag_name[0], tag_name[2], tag))
      param = self.identifier_map.get_id(tag_name[0], tag_name[2], opmask=False)
    return param

  def process_param(self, param, opcode, is_lhs_param=False):
    result = None
    if isinstance(param, str):
      if param[0] == ':':
        if is_lhs_param and opcode in lhs_operations:
          result = self.local_variables.add_id(param[1:])
        else:
          result = self.local_variables.get_id(param[1:])
      elif param[0] == '$':
        uses = 0 if is_lhs_param and opcode in global_lhs_operations else 1
        result = self.global_variables.add_id(param[1:], uses)
      elif param[0] == '@':
        result = self.quick_strings.add_str(param[1:])
      else:
        tag_name = param.partition("_")
        result = self.identifier_map.get_id(tag_name[0], tag_name[2], opmask=True)
    elif isinstance(param, lazy.LazyIdEvaluation):
      result = param.process(self)
    else:
      result = param
    return result

  def process_statement(self, statement):
    try:
      if isinstance(statement, (int, long)):
        opcode = statement
        param_count = 0
      else:
        opcode = statement[0]
        param_count = len(statement) - 1
        if param_count > 16:
          raise pc.ModuleSystemError("%d parameters exceeds the maximum count of 16" % param_count, opcode=opcode)
      result = ["%d %d " % (opcode, param_count)]
    except TypeError:
      raise pc.ModuleSystemError("invalid operation %s" % repr(statement))
    if param_count > 0:
      is_lhs_param = True
      for param in statement[1:]:
        param_no = self.process_param(param, opcode, is_lhs_param)
        try:
          result.append("%d " % param_no)
        except TypeError:
          raise pc.ModuleSystemError("invalid parameter %s" % repr(param), opcode=opcode)
        except pc.ModuleSystemError as e:
          e.opcode = opcode
          raise
        is_lhs_param = False
    return result, opcode

  def process_statements(self, statements):
    for statement in statements:
      if isinstance(statement, lazy.block):
        self.process_statements(statement.block)
      else:
        statement_result, opcode = self.process_statement(statement)
        self.current_block_result.extend(statement_result)
        self.current_statement_count += 1
        if opcode in try_begin_operations:
          self.current_indent += 1
        elif opcode == try_end:
          self.current_indent -= 1
        if self.current_block_check_can_fail and self.current_indent == 0 and not self.current_block_name.startswith("cf_"):
          if opcode & 0xfffffff in can_fail_operations:
            pc.WARNING("script can fail: use cf_ at the beginning of its name", entry=self.current_block_name, opcode=opcode)
          elif opcode == call_script and statement[1].startswith("cf_", 7):
            pc.WARNING("script can fail from calling '%s': use cf_ at the beginning of its name" % statement[1], entry=self.current_block_name, opcode=opcode)

  def process_block(self, block, name, check_can_fail=False):
    self.local_variables = LocalVariables()
    self.current_block_result = [None]
    self.current_statement_count = 0
    self.current_indent = 0
    self.current_block_name = name
    self.current_block_check_can_fail = check_can_fail
    try:
      self.process_statements(block)
    except pc.ModuleSystemError as e:
      if not e.entry:
        e.entry = name
      raise
    self.local_variables.warn_unused(name)
    if self.current_indent != 0:
      if self.current_indent > 0:
        missing = "missing"
      else:
        missing = "extra"
        self.current_indent *= -1
      pc.ERROR("%d %s try_end" % (self.current_indent, missing), entry=name)
    self.current_block_result[0] = " %d " % self.current_statement_count
    return self.current_block_result

  def process_triggers(self, triggers, name):
    result = ["%d" % block_len(triggers)]
    for trigger in triggers:
      result.append("\r\n%f " % trigger[0])
      trigger_name = "%s: %s" % (name, get_trigger_name(trigger[0]))
      result.extend(self.process_block(trigger[1], trigger_name))
    result.append("\r\n")
    return result


def make_export(data, data_name, tag=None, file_name=None, header_format=None, process_entry=None, process_list=None):
  """Generates module system data exporting functions."""
  def export_wrapper(processor):
    if not file_name:
      file_name_ = data_name
    else:
      file_name_ = file_name
    txt_file = open(module_info.export_path("%s.txt" % file_name_), "wb")
    print "Exporting %s..." % data_name.replace("_", " ")
    if tag and processor.write_id:
      id_file = open("ID_%s.py" % data_name, "w")
    else:
      id_file = None
    try:
      if process_list:
        process_list(processor, txt_file)
      if header_format:
        txt_file.write(header_format % len(data))
      for i, entry in enumerate(data):
        name = entry[0]
        if tag:
          pc.assert_valid_identifier(name, entry=data_name)
          if id_file:
            id_file.write("%s_%s = %d\n" % (tag, name, i))
        if process_entry:
          try:
            process_entry(processor, txt_file, entry, i)
          except pc.ModuleSystemError as e:
            if not e.entry:
              e.entry = "%s_%s" % (tag, name) if tag else "#%d" % i
            raise
          except Exception as e:
            if processor.show_backtrace:
              raise
            else:
              msg = e.args[0]
              if isinstance(e, TypeError) and ("has no len()" in msg or
                "object is not iterable" in msg or "object is not subscriptable" in msg):
                msg = "a list was expected: %s" % msg
              else:
                msg = "%s: %s" % (type(e).__name__, repr(msg))
              raise pc.ModuleSystemError(msg, entry=("%s_%s" % (tag, name) if tag else "#%d" % i))
    finally:
      txt_file.close()
      if id_file:
        id_file.close()
  return export_wrapper

def block_len(block):
  if not isinstance(block, (list, tuple)):
    pc.ERROR("%s %s found where list was expected" % (repr(block), type(block)))
  return len(block)
