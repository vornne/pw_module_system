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
  return is_valid_regex.match(s)

def assert_valid_identifier(s, entry=None):
  if not is_valid_identifier(s):
    ERROR("identifier '%s' contains invalid characters: must be lowercase, digits, and underscores" % s, entry=entry)

def format_error_message(prefix, msg, entry=None, opcode=None):
  output = [prefix, msg]
  if entry:
    output.append("; at ")
    output.append(repr(entry))
  if opcode:
    output.append(", operation: ")
    output.append(header_operations.get_opcode_name(opcode))
  return "".join(output)

class ModuleSystemError(Exception):

  def __init__(self, msg, entry=None, opcode=None):
    self.msg = msg
    self.entry = entry
    self.opcode = opcode

  def __str__(self):
    return format_error_message("ERROR: ", msg=self.msg, entry=self.entry, opcode=self.opcode)

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
