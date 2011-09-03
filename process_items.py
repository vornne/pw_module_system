import string

from process_common import *
from module_items import *

import module_factions

def get_item_code(item):
  prefix = "it_"
  code = prefix + item[0]
  return code

def save_python_header():
  file = open("./ID_items.py","w")
  for i, item in enumerate(items):
    file.write("itm_%s = %d\n"%(convert_to_identifier(item[0]), i))
  file.close()

def write_items(variable_list,variable_uses,tag_uses,quick_strings):
  itemkinds_file_name = export_dir + "item_kinds1.txt"
  ofile = open(itemkinds_file_name,"w")
  ofile.write("itemsfile version 3\n")
  ofile.write("%d\n"%len(items))
  for item in items:
    if (item[3] & itp_merchandise) > 0:
      id_no = find_object(items,convert_to_identifier(item[0]),tag_item)
      add_tag_use(tag_uses,tag_item,id_no)
    ofile.write(" itm_%s %s %s %d "%(convert_to_identifier(item[0]),replace_spaces(item[1]),replace_spaces(item[1]),len(item[2])))
    item_variations = item[2]
    for item_variation in item_variations:
      ofile.write(" %s %d "%(item_variation[0],item_variation[1]))
    ofile.write(" %d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\n"%(item[3], item[4], item[5], item[7],
                                                   get_weight(item[6]),
                                                   get_abundance(item[6]),
                                                   get_head_armor(item[6]),
                                                   get_body_armor(item[6]),
                                                   get_leg_armor(item[6]),
                                                   get_difficulty(item[6]),
                                                   get_hit_points(item[6]),
                                                   get_speed_rating(item[6]),
                                                   get_missile_speed(item[6]),
                                                   get_weapon_length(item[6]),
                                                   get_max_ammo(item[6]),
                                                   get_thrust_damage(item[6]),
                                                   get_swing_damage(item[6]),
                                                  ))
    if (len(item) > 9):
      ofile.write(" %d\n"%(len(item[9])))
      for item_faction in item[9]:
        ofile.write(" %d"%find_str_id(module_factions.factions, item_faction, tag_faction))
      ofile.write("\n")
    else:
      ofile.write(" 0\n")
    trigger_list = []
    if (len(item) > 8):
      trigger_list = item[8]
    save_simple_triggers(ofile, trigger_list, variable_list, variable_uses, tag_uses, quick_strings, debug_name=item[0])

  ofile.close()

print "Exporting items..."
save_python_header()

from module_info import *

from process_common import *
from process_operations import *

variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = []
quick_strings = load_quick_strings(export_dir)
write_items(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_quick_strings(export_dir,quick_strings)
