import string
import types

from module_info import *
from module_mission_templates import *

from process_common import *
from process_operations import *

import module_items

mission_template_name_pos = 0
mission_template_flags_pos = 1
mission_template_types_pos = 2
mission_template_desc_pos = 3
mission_template_groups_pos =4
mission_template_triggers_pos = 5

def save_triggers(file,template_name,triggers,variable_list,variable_uses,tag_uses,quick_strings):
  file.write("%d\n"%len(triggers))
  for i, trigger in enumerate(triggers):
    file.write("%f %f %f "%(trigger[trigger_check_pos],trigger[trigger_delay_pos],trigger[trigger_rearm_pos]))
    if trigger[0] < 0.0:
      debug_name = template_name + ", trigger id " + `trigger[0]`
    else:
      debug_name = template_name + ", trigger #" + `i`
    save_statement_block(file, debug_name + " conditions", 1, trigger[trigger_conditions_pos]  , variable_list,variable_uses,tag_uses,quick_strings)
    save_statement_block(file, debug_name + " consequences", 1, trigger[trigger_consequences_pos], variable_list,variable_uses,tag_uses,quick_strings)
    file.write("\n")
  file.write("\n")

def save_mission_template_group(file,entry):
  if (len(entry[5]) > 8):
    print "ERROR: Too many item_overrides!"
    error()
  file.write("%d %d %d %d %d %d  "%(entry[0],entry[1],entry[2],entry[3],entry[4], len(entry[5])))
  for item_override in entry[5]:
    item_override = find_str_id(module_items.items, item_override, tag_item)
    file.write("%d "%(item_override))
  file.write("\n")

def save_mission_templates(variables,variable_uses,tag_uses,quick_strings):
  file = open(export_dir + "mission_templates.txt","w")
  file.write("missionsfile version 1\n")
  file.write(" %d\n"%(len(mission_templates)))
  for mission_template in mission_templates:
    file.write("mst_%s %s %d "%(convert_to_identifier(mission_template[mission_template_name_pos]),convert_to_identifier(mission_template[mission_template_name_pos]),mission_template[mission_template_flags_pos]))
    file.write(" %d\n"%(mission_template[mission_template_types_pos]))
    file.write("%s \n"%(string.replace(mission_template[mission_template_desc_pos]," ","_")))
    file.write("\n%d "%len(mission_template[mission_template_groups_pos]))
    for group in mission_template[mission_template_groups_pos]:
      save_mission_template_group(file,group)
    save_triggers(file,convert_to_identifier(mission_template[mission_template_name_pos]), mission_template[mission_template_triggers_pos],variables,variable_uses,tag_uses,quick_strings)
    file.write("\n")
  file.close()

def save_python_header():
  file = open("./ID_mission_templates.py","w")
  for i, mission_template in enumerate(mission_templates):
    file.write("mst_%s = %d\n"%(mission_template[0], i))
  file.close()

print "Exporting mission templates..."
save_python_header()
variable_uses = []
variables = load_variables(export_dir, variable_uses)
tag_uses = []
quick_strings = load_quick_strings(export_dir)
save_mission_templates(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_quick_strings(export_dir,quick_strings)
