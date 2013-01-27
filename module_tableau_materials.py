from header_common import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *
import header_debug as dbg
import header_lazy_evaluation as lazy

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
#      The operations block is executed when the tableau is activated.
####################################################################################################################

# banner height = 200, width = 85 with wood, 75 without wood

# Apply a banner to an armor mesh, overlaying 'mesh_tableau' as a sort of stencil on top.
# 'banner_xyz' and 'banner_scale' adjust the position and scale of the banner relative to the armor (tableau) texture.
# 'mesh_xyz' can be used to adjust the position of the tableau mesh on the armor; the default should be correct in most cases.
def tableau_armor_banner(mesh_tableau, banner_xyz=(0,0,0), banner_scale=100, mesh_xyz=(0,0,100)):
  script = [(store_script_param, ":banner_mesh", 1),
    (set_fixed_point_multiplier, 100),
    (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":banner_mesh"),
    (cur_tableau_set_background_color, ":background_color"),
    (try_begin),
      (is_between, ":banner_mesh", banner_meshes_begin, banner_meshes_end),
      (init_position, pos1)]
  if banner_xyz[0] != 0:
    script.append((position_set_x, pos1, banner_xyz[0]))
  if banner_xyz[1] != 0:
    script.append((position_set_y, pos1, banner_xyz[1]))
  if banner_xyz[2] != 0:
    script.append((position_set_z, pos1, banner_xyz[2]))
  script.extend([(cur_tableau_add_mesh, ":banner_mesh", pos1, banner_scale, 0),
    (try_end),
    (init_position, pos1)])
  if mesh_xyz[0] != 0:
    script.append((position_set_x, pos1, mesh_xyz[0]))
  if mesh_xyz[1] != 0:
    script.append((position_set_y, pos1, mesh_xyz[1]))
  if mesh_xyz[2] != 0:
    script.append((position_set_z, pos1, mesh_xyz[2]))
  script.extend([(cur_tableau_add_mesh, mesh_tableau, pos1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000)])
  return script

# Apply just the background color of a banner to an armor mesh, overlaying 'mesh_tableau' on top.
def tableau_armor_color(mesh_tableau):
  return [(store_script_param, ":banner_mesh", 1),
    (set_fixed_point_multiplier, 100),
    (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":banner_mesh"),
    (cur_tableau_set_background_color, ":background_color"),
    (init_position, pos1),
    (cur_tableau_add_mesh, mesh_tableau, pos1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
    ]

# Apply the background color of a banner over the entire armor mesh as vertex color.
def tableau_armor_vertex_color(mesh_tableau):
  return [(store_script_param, ":banner_mesh", 1),
    (set_fixed_point_multiplier, 100),
    (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":banner_mesh"),
    (init_position, pos1),
    (cur_tableau_add_mesh_with_vertex_color, mesh_tableau, pos1, 0, 0, ":background_color"),
    (cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
    ]

# Apply a banner to a shield mesh, with 'mesh_tableau' overlaid.
def tableau_shield_banner(mesh_tableau, banner_xy, banner_scale, camera_width_height):
  return [(store_script_param, ":banner_mesh", 1),
    (set_fixed_point_multiplier, 100),
    (try_begin),
      (is_between, ":banner_mesh", banner_meshes_begin, banner_meshes_end),
      (init_position, pos1),
      (position_set_x, pos1, banner_xy[0]),
      (position_set_y, pos1, banner_xy[1]),
      (cur_tableau_add_mesh, ":banner_mesh", pos1, banner_scale, 0),
    (else_try),
      (troop_get_slot, ":background_color", "trp_banner_background_color_array", ":banner_mesh"),
      (cur_tableau_set_background_color, ":background_color"),
    (try_end),
    (init_position, pos1),
    (position_set_z, pos1, 10),
    (cur_tableau_add_mesh, mesh_tableau, pos1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, camera_width_height[0], camera_width_height[1], 0, 100000),
    ]

# Only applies the banner of the passed faction id to the mesh, for castle banners.
def tableau_castle_banner():
  return [(store_script_param, ":faction_id", 1),
    (set_fixed_point_multiplier, 100),
    (init_position, pos1),
    (position_set_y, pos1, 100),
    (position_set_x, pos1, -9),
    (faction_get_slot, ":banner_mesh", ":faction_id", slot_faction_banner_mesh),
    (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000),
    ]

# Only applies the banner to the mesh, for hand held banners.
def tableau_banner_pole():
  return [(store_script_param, ":banner_mesh", 1),
    (set_fixed_point_multiplier, 100),
    (init_position, pos1),
    (position_set_y, pos1, 100),
    (position_set_x, pos1, -1),
    (cur_tableau_add_mesh, ":banner_mesh", pos1, 0, 0),
    (init_position, pos1),
    (position_set_z, pos1, 100),
    (cur_tableau_add_mesh, "mesh_tableau_mesh_pw_banner_pole", pos1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000),
    ]

# Applies the banner to a shield shape for use in a presentation. If 'war' is True, crossed swords are overlaid.
def tableau_stats_chart_banner(war=False):
  script = [(store_script_param, ":banner_mesh", 1),
    (set_fixed_point_multiplier, 100),
    (init_position, pos1),
    (position_set_y, pos1, 130),
    (cur_tableau_add_mesh, ":banner_mesh", pos1, 115, 0)]
  if war == True:
    script.extend([(init_position, pos1),
      (cur_tableau_add_mesh, "mesh_pw_stats_chart_war", pos1, 0, 0)])
  script.append((cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000))
  return script

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

  ("round_shield_1", 0, "sample_shield_round_1", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_round_1", banner_xy=(-50,125), banner_scale=120, camera_width_height=(200,100))),
  ("round_shield_2", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_round_2", banner_xy=(-50,120), banner_scale=116, camera_width_height=(200,100))),
  ("round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_round_3", banner_xy=(-50,120), banner_scale=116, camera_width_height=(200,100))),
  ("round_shield_4", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_round_4", banner_xy=(-50,125), banner_scale=123, camera_width_height=(200,100))),
  ("round_shield_5", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_round_5", banner_xy=(-50,125), banner_scale=122, camera_width_height=(200,100))),
  ("small_round_shield_1", 0, "sample_shield_small_round_1", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_small_round_1", banner_xy=(-50,130), banner_scale=127, camera_width_height=(200,100))),
  ("small_round_shield_2", 0, "sample_shield_small_round_2", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_small_round_2", banner_xy=(-50,130), banner_scale=127, camera_width_height=(200,100))),
  ("small_round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_small_round_3", banner_xy=(-50,130), banner_scale=127, camera_width_height=(200,100))),
  ("kite_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_kite_1", banner_xy=(-60,140), banner_scale=116, camera_width_height=(200,200))),
  ("kite_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_kite_2", banner_xy=(-57,140), banner_scale=116, camera_width_height=(200,200))),
  ("kite_shield_3", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_kite_3", banner_xy=(-57,140), banner_scale=116, camera_width_height=(200,200))),
  ("kite_shield_4", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_kite_4", banner_xy=(-50,160), banner_scale=120, camera_width_height=(200,200))),
  ("heater_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_heater_1", banner_xy=(-60,151), banner_scale=116, camera_width_height=(200,200))),
  ("heater_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_heater_2", banner_xy=(-50,150), banner_scale=116, camera_width_height=(200,200))),
  ("pavise_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_pavise_1", banner_xy=(-54,120), banner_scale=118, camera_width_height=(200,200))),
  ("pavise_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, tableau_shield_banner("mesh_tableau_mesh_shield_pavise_2", banner_xy=(-54,120), banner_scale=116, camera_width_height=(200,200))),

  ("heraldic_armor_a", 0, "sample_heraldic_armor_a", 512, 512, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_armor_a", banner_xyz=(-26,120,50), banner_scale=70)),
  ("heraldic_armor_b", 0, "sample_heraldic_armor_b", 512, 512, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_armor_b", banner_xyz=(-5,120,10), banner_scale=70)),
  ("heraldic_armor_c", 0, "sample_heraldic_armor_c", 512, 512, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_armor_c", banner_xyz=(0,120,10), banner_scale=70)),
  ("heraldic_armor_d", 0, "sample_heraldic_armor_d", 512, 512, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_armor_d", banner_xyz=(0,120,10), banner_scale=70)),

  ("heraldic_leather_vest_a", 0, "leather_vest_a", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_leather_vest_a", banner_xyz=(-61,110,10), banner_scale=60)),
  ("heraldic_padded_cloth_a", 0, "padded_cloth_a", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_padded_cloth_a", banner_xyz=(-61,120,10), banner_scale=60)),
  ("heraldic_padded_cloth_b", 0, "padded_cloth_b", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_padded_cloth_b", banner_xyz=(-63,120,10), banner_scale=60)),
  ("heraldic_tabard_b", 0, "tabard_b", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_tabard_b", banner_xyz=(52,110,10), banner_scale=50)),
  ("heraldic_brigandine_b", 0, "brigandine_b", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_brigandine_b", banner_xyz=(-59,115,10), banner_scale=70)),
  ("heraldic_coat_of_plates", 0, "coat_of_plates_red", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_coat_of_plates", banner_xyz=(20,25,10), banner_scale=80)),
  ("heraldic_lamellar_armor_d", 0, "lamellar_armor_d", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_lamellar_armor_d", banner_xyz=(62,29,10), banner_scale=70)),
  ("heraldic_mail_long_surcoat", 0, "mail_long_surcoat", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_mail_long_surcoat", banner_xyz=(54,70,10), banner_scale=40)),
  ("heraldic_surcoat_over_mail", 0, "surcoat_over_mail", 1024, 1024, 0, 0, 0, 0, tableau_armor_banner("mesh_tableau_mesh_heraldic_surcoat_over_mail", banner_xyz=(-60,70,10), banner_scale=40)),

  ("colored_arena_tunic", 0, "arena_tunicW", 512, 512, 0, 0, 0, 0, tableau_armor_color("mesh_tableau_mesh_colored_arena_tunic")),
  ("colored_arena_armor", 0, "arena_armorW", 512, 512, 0, 0, 0, 0, tableau_armor_color("mesh_tableau_mesh_colored_arena_armor")),
  ("colored_lamellar_leather", 0, "lamellar_leather", 512, 512, 0, 0, 0, 0, tableau_armor_color("mesh_tableau_mesh_colored_lamellar_leather")),
  ("colored_lamellar_vest_b", 0, "lamellar_vest_b", 1024, 1024, 0, 0, 0, 0, tableau_armor_color("mesh_tableau_mesh_colored_lamellar_vest_b")),

  ("colored_helmets_new_b", 0, "helmets_new_b", 512, 512, 0, 0, 0, 0, tableau_armor_vertex_color("mesh_tableau_mesh_colored_helmets_new_b")),
  ("colored_helmets_new_d", 0, "helmets_new_d", 512, 512, 0, 0, 0, 0, tableau_armor_vertex_color("mesh_tableau_mesh_colored_helmets_new_d")),
  ("colored_helmets_new_e", 0, "helmets_new_e", 512, 512, 0, 0, 0, 0, tableau_armor_vertex_color("mesh_tableau_mesh_colored_helmets_new_e")),

  ("castle_banner_a", 0, "pw_banner_castle", 1024, 512, 0, 0, 0, 0, tableau_castle_banner()),
  ("castle_banner_b", 0, "pw_banner_castle", 1024, 512, 0, 0, 0, 0, tableau_castle_banner()),

  ("faction_banner_pole", 0, "pw_banner_pole", 512, 1024, 0, 0, 0, 0, tableau_banner_pole()),
  ("stats_chart_banner", 0, "pw_banner_pole", 512, 1024, 0, 0, 0, 0, tableau_stats_chart_banner()),
  ("stats_chart_banner_war", 0, "pw_banner_pole", 512, 1024, 0, 0, 0, 0, tableau_stats_chart_banner(war=True)),

]
