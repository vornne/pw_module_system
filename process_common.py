import string
import re
import header_operations

full_table = string.maketrans(" '`()-\t", "_______")
def convert_to_identifier(s):
  return string.translate(s, full_table, ",|")

part_table = string.maketrans(" \t\n", "__^")
def replace_spaces(s):
  return string.translate(s, part_table)

is_valid_regex = re.compile("[a-z0-9_]+$")
def is_valid_identifier(s):
  try:
    return is_valid_regex.match(s)
  except TypeError:
    return False

def assert_valid_identifier(s, entry=None, tag=None):
  if not is_valid_identifier(s):
    ERROR("identifier %s is invalid: must be a string of lowercase, digit, or underscore characters" % repr(s), entry=entry, tag=tag)

def format_error_message(prefix, msg, entry=None, opcode=None, tag=None):
  message = [prefix, msg]
  info = []
  if tag:
    info.extend([",", " type tag: ", tag])
  if opcode:
    info.extend([",", " operation: ", header_operations.get_opcode_name(opcode)])
  if entry:
    entry_string = repr(entry)
    if len(entry_string) > 100:
      entry_string = entry_string[:100] + " ... <snipped>"
    info.extend([",", " entry: ", entry_string])
  if len(info):
    info[0] = ";"
  return "".join(message + info)

class ModuleSystemError(Exception):

  def __init__(self, msg, entry=None, opcode=None, tag=None):
    self.msg = msg
    self.entry = entry
    self.opcode = opcode
    self.tag = tag

  def __str__(self):
    return format_error_message("ERROR: ", msg=self.msg, entry=self.entry, opcode=self.opcode, tag=self.tag)

def ERROR(*a, **k):
  raise ModuleSystemError(*a, **k)

def WARNING(*a, **k):
  print format_error_message("WARNING: ", *a, **k)

def set_warnings_as_errors():
  global WARNING
  WARNING = ERROR

def print_error(*a, **k):
  print format_error_message("ERROR: ", *a, **k)

def set_errors_non_fatal():
  global ERROR
  ERROR = print_error
