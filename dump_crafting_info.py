#!/usr/bin/python -tt

from module_items import *
from module_scene_props import *
from module_skills import *
import process_operations as po

id_map = po.IdentifierMap()
id_map.load_ids("itm", items, 0)
id_map.load_ids("skl", skills, 0)

def get_name(obj_list, id_str):
  s = id_str.partition("_")
  return obj_list[id_map.get_id(s[0], s[2])][1]

file = open("./crafting_info.txt","w")
for craft in crafting_info:
  resource_list = []
  for resource in craft[2]:
    if type(resource) == type(tuple()):
      resource_list.extend([", ", str(resource[1]), " ", get_name(items, resource[0])])
    else:
      resource_list.extend([", ", get_name(items, resource)])
  use_time = 0
  for spr in scene_props:
    if len(spr[4]) >= 3:
      init_trigger_op1 = spr[4][0][1][1]
      if init_trigger_op1[0] == scene_prop_set_slot and init_trigger_op1[2] == slot_scene_prop_item_id and init_trigger_op1[3] == craft[0]:
        use_time = get_spr_use_time(spr[1])
  skill_list = ["none"]
  if craft[1][0][0] > -1:
    skill_list = [get_name(skills, craft[1][0][0]), " ", str(craft[1][0][1])]
    if craft[1][1][0] > -1:
      skill_list.extend([" / ", get_name(skills, craft[1][1][0]), " ", str(craft[1][1][1])])
  file.write("{0:30} {1:25} Time: {2:2}{3}\n".format(get_name(items, craft[0]), ''.join(skill_list), use_time, ''.join(resource_list)))

