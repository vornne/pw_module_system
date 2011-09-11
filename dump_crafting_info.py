#!/usr/bin/python -tt

from module_items import *
from module_scene_props import *
from process_common import *

def get_pretty_item_name(item_id):
  item_name = item_id.partition("_")[2]
  pretty_name = "INVALID ITEM"
  for item in items:
    if item[0] == item_name:
      pretty_name = item[1]
  return pretty_name

file = open("./crafting_info.txt","w")
for craft in crafting_info:
  resource_str = ""
  for resource in craft[2]:
    if type(resource) == type(tuple()):
      resource_str = resource_str + ", {0} {1}".format(resource[1], get_pretty_item_name(resource[0]))
    else:
      resource_str = resource_str + ", " + get_pretty_item_name(resource)
  use_time = 0
  for spr in scene_props:
    if len(spr[4]) >= 3:
      init_trigger_op1 = spr[4][0][1][1]
      if init_trigger_op1[0] == scene_prop_set_slot and init_trigger_op1[2] == slot_scene_prop_item_id and init_trigger_op1[3] == craft[0]:
        use_time = get_spr_use_time(spr[1])
  file.write("{0:30} skill: {1:1}, time: {2:2}{3}\n".format(get_pretty_item_name(craft[0]), craft[1], use_time, resource_str))

