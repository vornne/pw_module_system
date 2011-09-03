import types
from header_game_menus import *
from module_info import *
from module_game_menus import *
from module_parties import *
from process_operations import *

from process_common import *

import module_party_templates
import module_factions
import module_troops
import module_map_icons

def save_parties(parties):
  file = open(export_dir + "parties.txt","w")
  file.write("partiesfile version 1\n")
  party_count = len(parties)
  file.write("%d %d\n"%(party_count, party_count))
  for i, party in enumerate(parties):
    file.write(" 1 %d %d "%(i, i))
    icon_flags = find_str_id(module_map_icons.map_icons, party[2][0], tag_map_icon) | (party[2][1] if len(party[2]) > 1 else 0)
    file.write("p_%s %s %d "%(convert_to_identifier(party[0]),replace_spaces(party[1]), icon_flags))
    menu_no = 0
    menu_param = party[3]
    if (type(menu_param) == types.StringType):
      menu_no = find_object(game_menus,menu_param,tag_menu)
      if (menu_no < 0):
        print "Error: Unable to find menu-id :" + menu_param
    else:
      menu_no = menu_param
    file.write("%d "%(menu_no))
    file.write("%d %d %d %d %d "%(find_str_id(module_party_templates.party_templates, party[4], tag_party_tpl), find_str_id(module_factions.factions, party[5], tag_faction), party[6], party[6],party[7]))
    ai_behavior_object = find_str_id(parties, party[8], tag_party)
    file.write("%d %d "%(ai_behavior_object,ai_behavior_object))
    position = party[9]
    default_behavior_location = position
    file.write("%f %f "%(default_behavior_location[0],default_behavior_location[1]))
    file.write("%f %f "%(default_behavior_location[0],default_behavior_location[1]))
    file.write("%f %f 0.0 "%position)
    member_list = party[10]
    file.write("%d "%len(member_list))
    for member in member_list:
      file.write("%d %d 0 %d "%(find_str_id(module_troops.troops, member[0], tag_troop),member[1],member[2]))
    bearing = 0.0
    if (len(party) > 11):
      bearing = (3.1415926 / 180.0) * party[11]
    file.write("\n%f\n"%(bearing))
  file.close()

def save_python_header(parties):
  file = open("./ID_parties.py","w")
  for i, party in enumerate(parties):
    file.write("p_%s = %d\n"%(convert_to_identifier(party[0]), i))
  file.close()

print "Exporting parties..."
save_python_header(parties)
save_parties(parties)
