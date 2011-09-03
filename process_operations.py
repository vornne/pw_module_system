import string

from process_common import *
from header_common import *
from header_operations import *

from module_strings import *
from module_skills import *
from module_music import *
from module_meshes import *
from module_sounds import *
from module_items import *
from module_troops import *
from module_factions import *
from module_quests import *
from module_party_templates import *
from module_parties import *
from module_scenes import *
from module_scripts import *
from module_mission_templates import *
from module_game_menus import *
from module_particle_systems import *
from module_scene_props import *
from module_scene_props import *
from module_presentations import *
from module_map_icons import *
from module_tableau_materials import *
from module_animations import *

def get_id_value(tag, identifier, tag_uses):
  tag_type = -1
  id_no = -1
  if (tag == "str"):
    id_no = find_object(strings, identifier)
    tag_type = tag_string
  elif (tag == "itm"):
    id_no = find_object(items, identifier)
    tag_type = tag_item
  elif (tag == "trp"):
    id_no = find_object(troops, identifier)
    tag_type = tag_troop
  elif (tag == "fac"):
    id_no = find_object(factions, identifier)
    tag_type = tag_faction
  elif (tag == "qst"):
    id_no = find_object(quests, identifier)
    tag_type = tag_quest
  elif (tag == "pt"):
    id_no = find_object(party_templates, identifier)
    tag_type = tag_party_tpl
  elif (tag == "p"):
    id_no = find_object(parties, identifier)
    tag_type = tag_party
  elif (tag == "scn"):
    id_no = find_object(scenes, identifier)
    tag_type = tag_scene
  elif (tag == "mt"):
    id_no = find_object(mission_templates, identifier)
    tag_type = tag_mission_tpl
  elif (tag == "mnu"):
    id_no = find_object(game_menus, identifier)
    tag_type = tag_menu
  elif (tag == "script"):
    id_no = find_object(scripts, identifier)
    tag_type = tag_script
  elif (tag == "psys"):
    id_no = find_object(particle_systems, identifier)
    tag_type = tag_particle_sys
  elif (tag == "spr"):
    id_no = find_object(scene_props, identifier)
    tag_type = tag_scene_prop
  elif (tag == "prsnt"):
    id_no = find_object(presentations, identifier)
    tag_type = tag_presentation
  elif (tag == "snd"):
    id_no = find_object(sounds, identifier)
    tag_type = tag_sound
  elif (tag == "icon"):
    id_no = find_object(map_icons, identifier)
    tag_type = tag_map_icon
  elif (tag == "skl"):
    id_no = find_object(skills, identifier)
    tag_type = tag_skill
  elif (tag == "track"):
    id_no = find_object(tracks, identifier)
    tag_type = tag_track
  elif (tag == "mesh"):
    id_no = find_object(meshes, identifier)
    tag_type = tag_mesh
  elif (tag == "anim"):
    id_no = find_object(animations, identifier)
    tag_type = tag_animation
  elif (tag == "tableau"):
    id_no = find_object(tableaus, identifier)
    tag_type = tag_tableau

  return (tag_type, id_no)

def get_identifier_value(full_str, tag_uses):
  underscore_pos = string.find(full_str, "_")
  result = -1
  if (underscore_pos > 0):
    tag_str = full_str[0:underscore_pos]
    id_str  = full_str[underscore_pos + 1:len(full_str)]
    (tag_type, id_no) = get_id_value(tag_str, id_str, tag_uses)
    if (tag_type > 0):
      if (id_no < 0):
        print "Error: Unable to find object: " + full_str
      else:
        result = id_no | (tag_type << op_num_value_bits)
    else:
      print "Error: Unrecognized tag: " + tag_str + " in object: " + full_str
  else:
    print "Error: Invalid object: " + full_str + ". Variables should start with a $ or : character and references should start with a tag"
  return result

def load_quick_strings(export_dir):
  quick_strings = []
  try:
    file = open(export_dir + "quick_strings.txt", "r")
    str_list = file.readlines()
    file.close()
    for s in str_list:
      s = string.strip(s)
      if s:
        ssplit = s.split(' ')
        if len(ssplit) == 2:
          quick_strings.append(ssplit)
  except:
    print "Creating new quick_strings.txt file..."
  return quick_strings

def save_quick_strings(export_dir, quick_strings):
  file = open(export_dir + "quick_strings.txt", "w")
  file.write("%d\n" % len(quick_strings))
  for quick_string in quick_strings:
    file.write("%s %s\n" % (quick_string[0], quick_string[1]))
  file.close()

def load_variables(export_dir, variable_uses):
  variables = []
  try:
    file = open(export_dir + "variables.txt", "r")
    var_list = file.readlines()
    file.close()
    for v in var_list:
      vv = string.strip(v)
      if vv:
        variables.append(vv)
  except:
    print "variables.txt not found. Creating new variables.txt file"

  try:
    file = open(export_dir + "variable_uses.txt", "r")
    var_list = file.readlines()
    file.close()
    for v in  var_list:
      vv = string.strip(v)
      if vv:
        variable_uses.append(int(vv))
  except:
    print "variable_uses.txt not found. Creating new variable_uses.txt file"

  return variables

def save_variables(export_dir, variables_list, variable_uses):
  file = open(export_dir + "variables.txt", "w")
  for i in xrange(len(variables_list)):
    file.write("%s\n"%variables_list[i])
  file.close()
  file = open(export_dir + "variable_uses.txt", "w")
  for i in xrange(len(variables_list)):
    file.write("%d\n"%variable_uses[i])
  file.close()

def check_varible_not_defined(variable_string, variables_list):
  if variable_string in variables_list:
    print "WARNING: Variable name used for both local and global contexts: " + variable_string

def add_variable(variable_string, variables_list, variable_uses):
  found = 0
  for i_t in xrange(len(variables_list)):
    if variable_string == variables_list[i_t]:
      found = 1
      variable_uses[i_t] = variable_uses[i_t] - 1
      break
  if not found:
    variables_list.append(variable_string)
    variable_uses.append(-1)

def get_variable(variable_string, variables_list, variable_uses):
  found = 0
  result = -1
  var_string = variable_string[1:]
  for i_t in xrange(len(variables_list)):
    if var_string == variables_list[i_t]:
      found = 1
      result = i_t
      variable_uses[result] = variable_uses[result] + 1
      break
  if not found:
    if (variable_string[0] == '$'):
      variables_list.append(variable_string)
      variable_uses.append(0)
      result = len(variables_list) - 1
      print "WARNING: Usage of unassigned global variable: " + variable_string
    else:
      print "ERROR: Usage of unassigned local variable: " + variable_string
  return result

def is_lhs_operation(op_code):
  return op_code in lhs_operations

def is_lhs_operation_for_global_vars(op_code):
  return op_code in lhs_operations or op_code in global_lhs_operations

def is_can_fail_operation(op_code):
  return op_code in can_fail_operations

def insert_quick_string_with_auto_id(sentence, quick_strings):
  id_str = "qstr_" + convert_to_identifier_with_no_lowercase(sentence)
  sentence = replace_spaces(sentence)
  id_len = 25
  index = -1
  for i, quick_string in enumerate(quick_strings):
    if id_str.startswith(quick_string[0], 0, id_len):
      if quick_string[1] == sentence:
        index = i
        break
      else:
        id_len += 1
  else:
    index = len(quick_strings)
    quick_strings.append([id_str[0:id_len], sentence])
  return index

def process_param(param, global_vars_list, global_var_uses, local_vars_list, local_var_uses, tag_uses, quick_strings):
  result = 0
  if isinstance(param, str):
    if (param[0] == '$'):
      check_varible_not_defined(param[1:], local_vars_list)
      result = get_variable(param, global_vars_list, global_var_uses)
      result |= opmask_variable
    elif (param[0] == ':'):
      check_varible_not_defined(param[1:], global_vars_list)
      result = get_variable(param, local_vars_list, local_var_uses)
      result |= opmask_local_variable
    elif (param[0] == '@'):
      result = insert_quick_string_with_auto_id(param[1:], quick_strings)
      result |= opmask_quick_string
    else:
      result = get_identifier_value(param, tag_uses)
      if (result < 0):
        print "ERROR: Illegal Identifier: " + param
  else:
    result = param
  return result

def save_statement(ofile, opcode, no_variables, statement, variable_list, variable_uses, local_vars_list, local_var_uses, tag_uses, quick_strings):
  if no_variables:
    ofile.write("%d 0 " % opcode)
  else:
    statement_len = len(statement) - 1
    ofile.write("%d %d " % (opcode, statement_len))
    if is_lhs_operation(opcode) and statement_len > 0:
      lhs_var = statement[1]
      if isinstance(lhs_var, str) and lhs_var[0] == ':':
        add_variable(lhs_var[1:], local_vars_list, local_var_uses)
    for param in statement[1:]:
      operand = process_param(param, variable_list, variable_uses, local_vars_list, local_var_uses, tag_uses, quick_strings)
      ofile.write("%d " % operand)

def save_statement2(ofile, opcode, no_variables, statement, variable_list, variable_uses, local_vars_list, local_var_uses, tag_uses, quick_strings):
  if no_variables == 0:
    lenstatement = len(statement) - 1
    if is_lhs_operation(opcode):
      if (lenstatement > 0):
        param = statement[1]
        if isinstance(param, str):
          if (param[0] == ':'):
            add_variable(param[1:], local_vars_list, local_var_uses)
  else:
    lenstatement = 0
  ofile.write("%d %d "%(opcode, lenstatement))
  for i in xrange(lenstatement):
    operand = process_param(statement[i + 1], variable_list, variable_uses, local_vars_list, local_var_uses, tag_uses, quick_strings)
    ofile.write("%d "%operand)

def compile_global_vars_in_statement(statement, variable_list, variable_uses):
  opcode = 0
  if not isinstance(statement, (list, tuple)):
    opcode = statement
  else:
    opcode = statement[0]
    if is_lhs_operation_for_global_vars(opcode):
      if (len(statement) > 1):
        param = statement[1]
        if isinstance(param, str):
          if (statement[1][0] == '$'):
            add_variable(statement[1][1:], variable_list, variable_uses)

def save_statement_block(ofile, statement_name, can_fail_statement, statement_block, variable_list, variable_uses, tag_uses, quick_strings):
  local_vars = []
  local_var_uses = []
  ofile.write(" %d "%(len(statement_block)))
  store_script_param_1_uses = 0
  store_script_param_2_uses = 0
  current_depth = 0
  can_fail = 0
  for statement in statement_block:
    if isinstance(statement, (list, tuple)):
      opcode = statement[0]
      no_variables = 0
    else:
      opcode = statement
      no_variables = 1
    if opcode in try_begin_operations:
      current_depth = current_depth + 1
    elif opcode == try_end:
      current_depth = current_depth - 1
    elif opcode == store_script_param_1 or (opcode == store_script_param and statement[2] == 1):
      store_script_param_1_uses = store_script_param_1_uses + 1
    elif opcode == store_script_param_2 or (opcode == store_script_param and statement[2] == 2):
      store_script_param_2_uses = store_script_param_2_uses + 1
    elif (can_fail_statement == 0 and current_depth == 0 and
        (is_can_fail_operation(opcode) or ((opcode == call_script) and (statement[1].startswith("cf_", 7)))) and (not statement_name.startswith("cf_"))):
      print "WARNING: Script can fail from opcode " + `opcode` + ". Use cf_ at the beginning of its name: " + statement_name
    save_statement(ofile, opcode, no_variables, statement, variable_list, variable_uses, local_vars, local_var_uses, tag_uses, quick_strings)
  if (store_script_param_1_uses > 1):
    print "WARNING: store_script_param_1 is used more than once:" + statement_name
  if (store_script_param_2_uses > 1):
    print "WARNING: store_script_param_2 is used more than once:" + statement_name
  for local_var, uses in zip(local_vars, local_var_uses):
    if uses == 0 and not local_var.startswith("unused"):
      print "WARNING: Local variable never used: " + local_var + ", at: " + statement_name
  if current_depth != 0:
    if current_depth > 0:
      missing = " missing"
    else:
      missing = " extra"
      current_depth *= -1
    print "WARNING: " + `current_depth` + missing + " try_end, at: " + statement_name

def compile_global_vars(statement_block, variable_list, variable_uses):
  for statement in statement_block:
    compile_global_vars_in_statement(statement, variable_list, variable_uses)

def save_simple_triggers(ofile, triggers, variable_list, variable_uses, tag_uses, quick_strings, debug_name="unknown"):
  ofile.write("%d\n"%len(triggers))
  for trigger in triggers:
    ofile.write("%f "%trigger[0])
    debug_name += ", trigger id " + `trigger[0]`
    save_statement_block(ofile, debug_name, 1, trigger[1], variable_list, variable_uses, tag_uses, quick_strings)
    ofile.write("\n")
  ofile.write("\n")
