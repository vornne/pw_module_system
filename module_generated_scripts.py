####################################################################################################################
# This file is for scripts that are generated automatically from lists generated in other module files,
# which needs to be executed once just before writing scripts.txt, rather than every time module_scripts is loaded,
# to avoid extra or cyclic dependencies.
#
# To use, make a function called "generate_" then the script name which will contain the generated script body.
####################################################################################################################

from header_skills import *
from header_troops import *
from module_items import *
from module_scene_props import *
from module_animations import *

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

def generate_initialize_item_slots():
  script_body = []
  for item_id, item in enumerate(items):
    item_difficulty = item_difficulties_list[item_id]
    if item_difficulty > 0:
      script_body.append((item_set_slot, item_id, slot_item_difficulty, item_difficulty))
    item_length = item_lengths_list[item_id]
    if item_length > 0:
      script_body.append((item_set_slot, item_id, slot_item_length, item_length))
    if (item[7] & imodbit_female == imodbit_female):
      script_body.append((item_set_slot, item_id, slot_item_gender, tf_female))
    item_type = item[3] & 0xff
    item_max_ammo = get_max_ammo(item[6])
    if item_type in (itp_type_arrows, itp_type_bolts, itp_type_thrown) and item_max_ammo > 0:
      script_body.append((item_set_slot, item_id, slot_item_max_ammo, item_max_ammo))
    if item[3] & itp_bonus_against_shield:
      script_body.append((item_set_slot, item_id, slot_item_bonus_against_wood, 1))
    if item[3] & itp_couchable:
      script_body.append((item_set_slot, item_id, slot_item_couchable, 1))
    if item_type in itm_weapons and item_difficulty > 0 and item[4] & itc_attack_capable:
      script_body.append((item_set_slot, item_id, slot_item_has_attack_requirements, 1))
      script_body.append((item_set_slot, item_id, slot_item_max_raw_damage,
        max(get_raw_damage(get_swing_damage(item[6])), get_raw_damage(get_thrust_damage(item[6])))))
  for entry in item_class_list:
    script_body.append((item_set_slot, entry[0], slot_item_class, entry[1]))
    if len(entry) > 2 and entry[2] > 0:
      script_body.append((item_set_slot, entry[0], slot_item_resource_amount, entry[2]))
  for animal in herd_animal_list:
    adult_item_id, child_item_id, grow_age, max_in_herd, attack_reaction, death_sound, meat, hide, wildness = animal
    script_body.extend([
      (item_set_slot, adult_item_id, slot_item_animal_adult_item_id, adult_item_id),
      (item_set_slot, child_item_id, slot_item_animal_adult_item_id, adult_item_id),
      (item_set_slot, adult_item_id, slot_item_animal_child_item_id, child_item_id),
      (item_set_slot, child_item_id, slot_item_animal_child_item_id, child_item_id),
      (item_set_slot, adult_item_id, slot_item_animal_grow_time, grow_age * 60),
      (item_set_slot, child_item_id, slot_item_animal_grow_time, grow_age * 60),
      (item_set_slot, adult_item_id, slot_item_animal_max_in_herd, max_in_herd),
      (item_set_slot, child_item_id, slot_item_animal_max_in_herd, max_in_herd),
      (item_set_slot, adult_item_id, slot_item_animal_attack_reaction, attack_reaction),
      (item_set_slot, child_item_id, slot_item_animal_attack_reaction, animal_reaction_flee),
      (item_set_slot, adult_item_id, slot_item_animal_death_sound, death_sound),
      (item_set_slot, child_item_id, slot_item_animal_death_sound, death_sound),
      (item_set_slot, adult_item_id, slot_item_animal_meat_count, meat),
      (item_set_slot, child_item_id, slot_item_animal_meat_count, meat / 3),
      (item_set_slot, adult_item_id, slot_item_animal_hide_count, hide),
      (item_set_slot, child_item_id, slot_item_animal_hide_count, hide / 4),
      (item_set_slot, adult_item_id, slot_item_animal_wildness, wildness),
      (item_set_slot, child_item_id, slot_item_animal_wildness, wildness),
      ])
  return script_body

def generate_setup_all_linked_scene_props():
  script_body = []
  for link_entry in scene_props_to_link:
    script_body.append(tuple([call_script, "script_setup_linked_scene_props"] + link_entry))
  return script_body

def generate_setup_scene_props_after_mission_start():
  script_body = []
  for link_entry in scene_props_to_init:
    script_body.extend([
      (scene_prop_get_num_instances, ":num_instances", link_entry[0]),
      (try_for_range, ":instance_no", 0, ":num_instances"),
        (scene_prop_get_instance, ":instance_id", link_entry[0], ":instance_no"),
        tuple([call_script, link_entry[1], ":instance_id"] + link_entry[2:]),
      (try_end),
      ])
  return script_body

def generate_initialize_animation_durations():
  script_body = []
  for animation_id, animation in enumerate(animations):
    variant_durations = [variant[0] for variant in animation[3:]]
    average_duration = int(1000 * sum(variant_durations) / len(variant_durations) + 200)
    script_body.append((troop_set_slot, "trp_animation_durations", animation_id, average_duration))
  return script_body
