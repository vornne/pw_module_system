####################################################################################################################
# Generates strings at module system build time.
#
# To use, make a function called "generate_" then the string name which will be combined with the generated text.
####################################################################################################################

from module_items import *
from module_scene_props import *

def process_item(processor, item_str, entry=None):
  try:
    return items[processor.process_id(item_str)]
  except Exception as e:
    if not e.entry:
      if entry:
        e.entry = "crafting data for %s" % (entry)
      else:
        e.entry = "crafting data"
    raise

def crafting_book_generator(string, processor, item_type_checker):
  crafting_list = [string]
  for entry in crafting_data:
    item = process_item(processor, entry[0])
    if not item_type_checker(item[3] & 0xff, entry[1][0][0]):
      continue
    crafting_list.extend([item[1], ": "])
    for i, resource in enumerate(entry[2]):
      if i > 0:
        crafting_list.append(", ")
      if isinstance(resource, tuple):
        crafting_list.extend([str(resource[1]), " "])
        resource = resource[0]
      crafting_list.append(process_item(processor, resource, entry[0])[1])
    crafting_list.append("^^")
  return "".join(crafting_list)

def type_is_armor(item_type):
  return itp_type_head_armor <= item_type <= itp_type_hand_armor

def is_weapon(item_type, skill):
  return not type_is_armor(item_type)

def generate_book_of_weapons(string, processor):
  return crafting_book_generator(string, processor, is_weapon)

def is_clothing(item_type, skill):
  return type_is_armor(item_type) and skill == "skl_tailoring"

def generate_book_of_clothing(string, processor):
  return crafting_book_generator(string, processor, is_clothing)

def is_armor(item_type, skill):
  return type_is_armor(item_type) and skill == "skl_engineer"

def generate_book_of_armor(string, processor):
  return crafting_book_generator(string, processor, is_armor)
