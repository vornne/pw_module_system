# -*- coding: cp1254 -*-
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [
  ("game_start", []),
  ("game_get_use_string", []),
  ("game_quick_start", []),
  ("game_set_multiplayer_mission_end", []),
  ("game_enable_cheat_menu", []),
  ("game_get_console_command", []),
  ("game_event_party_encounter", []),
  ("game_event_simulate_battle", []),
  ("game_event_battle_end", []),
  ("game_get_item_buy_price_factor", []),
  ("game_get_item_sell_price_factor", []),
  ("game_event_buy_item", []),
  ("game_event_sell_item", []),
  ("game_get_troop_wage", []),
  ("game_get_total_wage", []),
  ("game_get_join_cost", []),
  ("game_get_upgrade_xp", []),
  ("game_get_upgrade_cost", []),
  ("game_get_prisoner_price", []),
  ("game_check_prisoner_can_be_sold", []),
  ("game_get_morale_of_troops_from_faction", []),
  ("game_event_detect_party", []),
  ("game_event_undetect_party", []),
  ("game_get_statistics_line", []),
  ("game_get_date_text", []),
  ("game_get_money_text", []),
  ("game_get_party_companion_limit", []),
  ("game_reset_player_party_name", []),
  ("game_get_troop_note", []),
  ("game_get_center_note", []),
  ("game_get_faction_note", []),
  ("game_get_quest_note", []),
  ("game_get_info_page_note", []),
  ("game_get_scene_name", []),
  ("game_get_mission_template_name", []),
  ("game_receive_url_response", []),
  ("game_get_cheat_mode", []),
  ("game_receive_network_message", []),
  ("game_get_multiplayer_server_option_for_mission_template", []),
  ("game_multiplayer_server_option_for_mission_template_to_string", []),
  ("game_multiplayer_event_duel_offered", []),
  ("game_get_multiplayer_game_type_enum", []),
  ("game_multiplayer_get_game_type_mission_template", []),
  ("game_get_party_prisoner_limit", []),
  ("game_get_item_extra_text", []),
  ("game_on_disembark", []),
  ("game_context_menu_get_buttons", []),
  ("game_event_context_menu_button_clicked", []),
  ("game_get_skill_modifier_for_troop", []),
  ("game_check_party_sees_party", []),
  ("game_get_party_speed_multiplier", []),

  ("add_troop_to_cur_tableau_for_profile",
   [(store_script_param, ":troop_no",1),
    (set_fixed_point_multiplier, 100),

    (cur_tableau_clear_override_items),
    (cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),

    (init_position, pos5),
    (assign, ":cam_height", 105),
    (assign, ":camera_distance", 380),
    (assign, ":camera_yaw", -15),
    (assign, ":camera_pitch", -18),
    (assign, ":animation", "anim_stand_man"),

    (position_set_z, pos5, ":cam_height"),
    (position_rotate_x, pos5, -90),
    (position_rotate_z, pos5, 180),
    (position_rotate_y, pos5, ":camera_yaw"),
    (position_rotate_x, pos5, ":camera_pitch"),
    (position_move_z, pos5, ":camera_distance", 0),
    (position_move_x, pos5, 5, 0),

    (profile_get_banner_id, ":profile_banner"),
    (try_begin),
      (ge, ":profile_banner", 0),
      (init_position, pos2),
      (val_add, ":profile_banner", banner_meshes_begin),
      (position_set_x, pos2, -175),
      (position_set_y, pos2, -300),
      (position_set_z, pos2, 180),
      (position_rotate_x, pos2, 90),
      (position_rotate_y, pos2, -15),
      (cur_tableau_add_mesh, ":profile_banner", pos2, 0, 0),
    (try_end),

    (init_position, pos2),
    (try_begin),
      (troop_is_hero, ":troop_no"),
      (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
    (else_try),
      (store_mul, ":random_seed", ":troop_no", 126233),
      (val_mod, ":random_seed", 1000),
      (val_add, ":random_seed", 1),
      (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
    (try_end),
    (cur_tableau_set_camera_position, pos5),

    (copy_position, pos8, pos5),
    (position_rotate_x, pos8, -90),
    (position_rotate_z, pos8, 30),
    (position_rotate_x, pos8, -60),
    (cur_tableau_add_sun_light, pos8, 175,150,125),
    ]),

]
