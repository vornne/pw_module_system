from module_info import *
from module_party_templates import *

from process_common import *

import module_factions
import module_troops
import module_map_icons

def save_party_template_troop(file,troop):
  if troop:
    file.write("%d %d %d "%(find_str_id(module_troops.troops, troop[0], tag_troop),troop[1],troop[2]))
    if (len(troop) > 3):
      file.write("%d "%troop[3])
    else:
      file.write("0 ")
  else:
    file.write("-1 ")

def save_party_templates():
  file = open(export_dir + "party_templates.txt","w")
  file.write("partytemplatesfile version 1\n")
  file.write("%d\n"%(len(party_templates)))
  for party_template in party_templates:
    icon_flags = 0 if not party_template[2] else (find_str_id(module_map_icons.map_icons, party_template[2][0], tag_map_icon)
      | (party_template[2][1] if len(party_template[2]) > 1 else 0))
    file.write("pt_%s %s %d %d %d %d "%(convert_to_identifier(party_template[0]),replace_spaces(party_template[1]), icon_flags, party_template[3], find_str_id(module_factions.factions, party_template[4], tag_faction), party_template[5]))
    members = party_template[6]
    if (len(members) > 6):
      print "Error! NUMBER OF TEMPLATE MEMBERS EXCEEDS 6 " + party_template[0]
      members = members[0:6]
    for party_template_member in members:
      save_party_template_troop(file,party_template_member)
    for i in xrange(6 - len(members)):
      save_party_template_troop(file,0)
    file.write("\n")
  file.close()

def save_python_header():
  file = open("./ID_party_templates.py","w")
  for i, party_template in enumerate(party_templates):
    file.write("pt_%s = %d\n"%(convert_to_identifier(party_template[0]), i))
  file.close()

print "Exporting party templates..."
save_python_header()
save_party_templates()
