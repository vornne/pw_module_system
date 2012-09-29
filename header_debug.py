from header_common import reg
from header_operations import assign, display_message, server_add_message_to_log
import header_lazy_evaluation as lazy

register_begin = 80
register_end = 100
current_register = register_begin
register_names = {}

def increment():
  global current_register
  if current_register >= register_end:
    raise Exception("Too many variables for debug output.")
  current_register += 1

def var(name, display_name=None):
  global register_names
  if display_name is None:
    display_name = str.strip(name, ":$")
  register_names[current_register] = display_name
  op = (assign, reg(current_register), name)
  increment()
  return op

def op(name, operation, *args):
  global register_names
  register_names[current_register] = name
  op = [operation, reg(current_register)]
  op.extend(args)
  increment()
  return tuple(op)

def generate_string(message, reset):
  global current_register
  global register_names
  string_list = ["@"]
  if message is not None:
    string_list.append(message)
    string_list.append(" - ")
  for i in xrange(register_begin, current_register):
    if i > register_begin:
      string_list.append(", ")
    string_list.append("{0}: {{reg{1}}}".format(register_names[i], i))
  debug_string = ''.join(string_list)
  if reset is True:
    current_register = register_begin
  return debug_string

def display(message=None, reset=True):
  return (display_message, generate_string(message, reset))

def log(message=None, reset=True):
  return (server_add_message_to_log, generate_string(message, reset))

def vars(*args):
  return lazy.block([var(arg) for arg in args])

def vars_display(*args):
  return lazy.block([var(arg) for arg in args] + [display()])
