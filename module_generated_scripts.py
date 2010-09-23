from module_scripts import *
from module_items import *
from module_scene_props import *

def generate_script(name, body):
  for script in scripts:
    if script[0] == name:
      script[1].extend(body)
      return
  else:
    raise Exception("Script '" + name + "' not found")

def generate_store_troop_skills_description():
  script_body = [(store_script_param, ":troop_id", 1)]
  for skill in pw_skills:
    script_body.extend([
      (store_skill_level, reg10, "skl_"+skill, ":troop_id"),
      (try_begin),
        (gt, reg10, 0),
        (str_store_string, s0, "@{s0}^"+get_skill_name(skill)+": {reg10}"),
      (try_end),
      ])
  return script_body
generate_script("store_troop_skills_description", generate_store_troop_skills_description())

def generate_initialize_item_slots():
  script_body = []
  for item_id, item in enumerate(items):
    difficulty = get_difficulty(item[6])
    if difficulty > 0:
      script_body.append((item_set_slot, item_id, slot_item_difficulty, difficulty))
    length = get_weapon_length(item[6])
    if length > 0:
      script_body.append((item_set_slot, item_id, slot_item_length, length))
  return script_body
generate_script("initialize_item_slots", generate_initialize_item_slots())

def generate_setup_all_linked_scene_props():
  script_body = []
  for link_entry in scene_props_to_link:
    script_body.append(tuple([call_script, "script_setup_linked_scene_props"] + link_entry))
  return script_body
generate_script("setup_all_linked_scene_props", generate_setup_all_linked_scene_props())

def generate_setup_scene_props_after_mission_start():
  script_body = []
  for link_entry in scene_props_to_init:
    script_body.extend([
      (scene_prop_get_num_instances, ":num_instances", link_entry[0]),
      (try_for_range, ":instance_no", 0, ":num_instances"),
        (scene_prop_get_instance, ":instance_id", link_entry[0], ":instance_no"),
        tuple([call_script] + [link_entry[1]] + [":instance_id"] + link_entry[2:]),
      (try_end),
      ])
  return script_body
generate_script("setup_scene_props_after_mission_start", generate_setup_scene_props_after_mission_start())
