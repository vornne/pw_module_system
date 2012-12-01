#!/usr/bin/python -tt

from module_items import *

convert_items = [

]

def convert_item_to_buy_spr():
  file = open("./module_scene_props.py","a")
  for item in convert_items:
    item_type = (item[3] & ibf_armor_mask)
    if item_type == itp_type_head_armor:
      if (item[3] & itp_attach_armature) == itp_attach_armature:
        bo_string = "bo_armor_head_armature"
      else:
        bo_string = "bo_armor_head"
    elif item_type == itp_type_body_armor:
      bo_string = "bo_armor_body"
    elif item_type == itp_type_foot_armor:
      bo_string = "bo_armor_foot"
    elif item_type == itp_type_hand_armor:
      bo_string = "bo_armor_hand"
    elif item_type == itp_type_shield:
      bo_string = "bo_shield_round"
    elif item_type == itp_type_bow:
      bo_string = "bo_weapon"
    elif item_type == itp_type_crossbow:
      bo_string = "bo_weapon_small"
    elif item_type == itp_type_horse:
      bo_string = "bo_horse"
    else:
      length = get_weapon_length(item[6])
      if length < 80:
        bo_string = "bo_weapon_small"
      elif length > 120:
        bo_string = "bo_weapon_big"
      else:
        bo_string = "bo_weapon"

    if len(item) > 8 and item[8][0][1][2][1] == "script_item_set_banner":
      tableau_param = ', tableau="{0}"'.format(item[8][0][1][2][2])
    else:
      tableau_param = ""

    file.write('  ("pw_buy_{0}",spr_buy_item_flags(1),"{1}","{2}", spr_buy_item_triggers("itm_{0}", resources=[], engineer=0{3})),\n'.format(
      item[0], item[2][0][0], bo_string, tableau_param))

  file.close()

convert_item_to_buy_spr()
