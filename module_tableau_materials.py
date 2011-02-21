from header_common import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *

####################################################################################################################
#  Each tableau material contains the following fields:
#  1) Tableau id (string): used for referencing tableaux in other files. The prefix tab_ is automatically added before each tableau-id.
#  2) Tableau flags (int). See header_tableau_materials.py for a list of available flags
#  3) Tableau sample material name (string).
#  4) Tableau width (int).
#  5) Tableau height (int).
#  6) Tableau mesh min x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  7) Tableau mesh min y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  8) Tableau mesh max x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  9) Tableau mesh max y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  10) Operations block (list): A list of operations. See header_operations.py for reference.
#     The operations block is executed when the tableau is activated.
# 
####################################################################################################################

#banner height = 200, width = 85 with wood, 75 without wood

tableaus = [
  ("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532, []),
  ("game_inventory_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270, []),
  ("game_party_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300, []),

  ("game_profile_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480,
   [(store_script_param, ":profile_no", 1),
    (assign, ":gender", ":profile_no"),
    (val_mod, ":gender", 2),
    (try_begin),
      (eq, ":gender", 0),
      (assign, ":troop_no", "trp_multiplayer_profile_troop_male"),
    (else_try),
      (assign, ":troop_no", "trp_multiplayer_profile_troop_female"),
    (try_end),
    (troop_set_face_key_from_current_profile, ":troop_no"),
    (cur_tableau_set_background_color, 0xFF888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),

    (init_position, pos1),
    (position_set_z, pos1, 100),
    (position_set_x, pos1, -20),
    (position_set_y, pos1, -20),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_color", ":troop_no", pos1, 0, 0),
    (position_set_z, pos1, 200),
    (cur_tableau_add_tableau_mesh, "tableau_troop_profile_alpha_mask", ":troop_no", pos1, 0, 0),
    ]),

  ("troop_profile_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400,
   [(store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0x00888888),
    (cur_tableau_set_ambient_light, 10,11,15),
    (cur_tableau_render_as_alpha_mask),
    (call_script, "script_add_troop_to_cur_tableau_for_profile", ":troop_no"),
    ]),

  ("troop_profile_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400,
   [(store_script_param, ":troop_no", 1),
    (cur_tableau_set_background_color, 0xFFF9E7A8),
    (cur_tableau_set_ambient_light, 10,11,15),
    (call_script, "script_add_troop_to_cur_tableau_for_profile", ":troop_no"),
    ]),

  ("game_troop_label_banner", 0, "tableau_with_transparency", 256, 256, -128, 0, 128, 256,
   [(store_script_param, ":banner_mesh", 1),
    (cur_tableau_set_background_color, 0xFF888888),
    (set_fixed_point_multiplier, 100),
    (cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),

    (init_position, pos1),
    (position_set_y, pos1, 120),
    (cur_tableau_add_mesh, ":banner_mesh", pos1, 120, 0),
    ]),

]
