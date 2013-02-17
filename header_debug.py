from header_common import reg
from header_operations import assign, display_message, server_add_message_to_log
import header_lazy_evaluation as lazy

####################################################################################################################
# Short helper functions to generate operations for displaying debugging output.
####################################################################################################################

register_begin = 80
register_end = 100
current_register = register_begin
register_names = {}

# internal use only
def increment():
  global current_register
  if current_register >= register_end:
    raise Exception("Too many variables for debug output.")
  current_register += 1

# example: dbg.var(":player_id"),
def var(name, display_name=None):
  global register_names
  if display_name is None:
    display_name = str.strip(name, ":$")
  register_names[current_register] = display_name
  op = (assign, reg(current_register), name)
  increment()
  return op

# example: dbg.op("pos2_x", position_get_x, pos2),
def op(name, operation, *args):
  global register_names
  register_names[current_register] = name
  op = [operation, reg(current_register)]
  op.extend(args)
  increment()
  return tuple(op)

# internal use only
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

# example: dbg.display(),
def display(message=None, reset=True):
  return (display_message, generate_string(message, reset))

# example: dbg.log(),
def log(message=None, reset=True):
  return (server_add_message_to_log, generate_string(message, reset))

# example: dbg.vars(":player_id", ":agent_id", ":gold"),
def vars(*args):
  return lazy.block([var(arg) for arg in args])

# example: dbg.vars_display(":agent_id", ":horse_agent_id", ":distance"),
def vars_display(*args):
  return lazy.block([var(arg) for arg in args] + [display()])

# initialize all debug registers in case some are not set
def reset_all(value=-989):
  return lazy.block((assign, reg(r), value)
    for r in range(register_begin, register_end + 1))
