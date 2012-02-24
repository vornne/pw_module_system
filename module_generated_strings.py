####################################################################################################################
# Generates strings at module system build time.
#
# To use, make a function called "generate_" then the string name which returns the string text.
####################################################################################################################

from module_items import *
from module_scene_props import *

def generate_book_of_weapons(string, processor):
  crafting_list = [string]
  for entry in crafting_info:
    crafting_list.extend([items[processor.process_id(entry[0])][1], ": "])
    for i, resource in enumerate(entry[2]):
      if i > 0:
        crafting_list.append(", ")
      if isinstance(resource, tuple):
        crafting_list.extend([str(resource[1]), " "])
        resource = resource[0]
      crafting_list.append(items[processor.process_id(resource)][1])
    crafting_list.append("^^")
  return "".join(crafting_list)
