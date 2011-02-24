from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
  ("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_infantry", 0, "flag_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_archers", 0, "flag_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_cavalry", 0, "flag_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("inv_slot", 0, "inv_slot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_host_maps_1", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_2", 0, "mp_ui_host_maps_a2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_3", 0, "mp_ui_host_maps_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_4", 0, "mp_ui_host_maps_ruinedf", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_5", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_6", 0, "mp_ui_host_maps_a1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_7", 0, "mp_ui_host_maps_fieldby", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_8", 0, "mp_ui_host_maps_castle2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_9", 0, "mp_ui_host_maps_snovyv", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_10", 0, "mp_ui_host_maps_castle3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_11", 0, "mp_ui_host_maps_c1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_12", 0, "mp_ui_host_maps_c2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_13", 0, "mp_ui_host_maps_c3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_randomp", 0, "mp_ui_host_maps_randomp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_randoms", 0, "mp_ui_host_maps_randoms", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw", 0, "flag_project_sw", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg", 0, "flag_project_vg", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh", 0, "flag_project_kh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd", 0, "flag_project_nd", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh", 0, "flag_project_rh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr", 0, "flag_project_sr", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_projects_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw_miss", 0, "flag_project_sw_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg_miss", 0, "flag_project_vg_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh_miss", 0, "flag_project_kh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd_miss", 0, "flag_project_nd_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh_miss", 0, "flag_project_rh_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr_miss", 0, "flag_project_sr_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_misses_end", 0, "0", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("tableau_mesh_shield_round_1",  0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_2",  0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_3",  0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_4",  0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_5",  0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_1",  0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_2",  0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_3",  0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_1",   0, "tableau_mesh_shield_kite_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_2",   0, "tableau_mesh_shield_kite_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_3",   0, "tableau_mesh_shield_kite_3",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_4",   0, "tableau_mesh_shield_kite_4",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("heraldic_armor_bg", 0, "heraldic_armor_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_c",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("outer_terrain_plain_1", 0, "ter_border_a", -90, 0, 0, 0, 0, 0, 1, 1, 1),
  ("banner_a01", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a02", 0, "banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a03", 0, "banner_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a04", 0, "banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a06", 0, "banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a08", 0, "banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a12", 0, "banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a13", 0, "banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a16", 0, "banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a17", 0, "banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a18", 0, "banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a19", 0, "banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a20", 0, "banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a21", 0, "banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b01", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b02", 0, "banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b05", 0, "banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b06", 0, "banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b07", 0, "banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b08", 0, "banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b09", 0, "banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b10", 0, "banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b14", 0, "banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b15", 0, "banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b16", 0, "banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b18", 0, "banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b20", 0, "banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c01", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c04", 0, "banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c06", 0, "banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c07", 0, "banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c10", 0, "banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c12", 0, "banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c13", 0, "banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c14", 0, "banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c16", 0, "banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c19", 0, "banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d02", 0, "banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d03", 0, "banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d04", 0, "banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d06", 0, "banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d07", 0, "banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d08", 0, "banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d09", 0, "banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d11", 0, "banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d12", 0, "banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d13", 0, "banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d14", 0, "banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d15", 0, "banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d16", 0, "banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d17", 0, "banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d18", 0, "banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d19", 0, "banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d20", 0, "banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d21", 0, "banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f21", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_g01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_g10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("arms_a01", 0, "arms_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a02", 0, "arms_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a03", 0, "arms_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a04", 0, "arms_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a06", 0, "arms_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a08", 0, "arms_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a12", 0, "arms_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a13", 0, "arms_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a16", 0, "arms_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a17", 0, "arms_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a18", 0, "arms_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a19", 0, "arms_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a20", 0, "arms_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a21", 0, "arms_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b01", 0, "arms_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b02", 0, "arms_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b05", 0, "arms_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b06", 0, "arms_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b07", 0, "arms_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b08", 0, "arms_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b09", 0, "arms_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b10", 0, "arms_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b14", 0, "arms_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b15", 0, "arms_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b16", 0, "arms_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b18", 0, "arms_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b20", 0, "arms_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c01", 0, "arms_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c04", 0, "arms_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c06", 0, "arms_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c07", 0, "arms_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c10", 0, "arms_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c12", 0, "arms_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c13", 0, "arms_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c14", 0, "arms_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c16", 0, "arms_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c19", 0, "arms_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d02", 0, "arms_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d03", 0, "arms_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d04", 0, "arms_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d06", 0, "arms_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d07", 0, "arms_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d08", 0, "arms_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d09", 0, "arms_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d11", 0, "arms_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d12", 0, "arms_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d13", 0, "arms_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d14", 0, "arms_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d15", 0, "arms_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d16", 0, "arms_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d17", 0, "arms_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d18", 0, "arms_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d19", 0, "arms_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d20", 0, "arms_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d21", 0, "arms_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e02", 0, "arms_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("arms_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("arms_g01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_g10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("arms_kingdom_a", 0, "banner_kingdom_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_kingdom_b", 0, "banner_kingdom_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_kingdom_c", 0, "banner_kingdom_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_kingdom_d", 0, "banner_kingdom_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_kingdom_e", 0, "banner_kingdom_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),  
  ("arms_kingdom_f", 0, "banner_kingdom_f", 0, 0, 0, -90, 0, 0, 1, 1, 1),  
  ("arms_f21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("troop_label_banner",  0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("ui_kingdom_shield_1", 0, "ui_kingdom_shield_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_2", 0, "ui_kingdom_shield_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_3", 0, "ui_kingdom_shield_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_4", 0, "ui_kingdom_shield_4", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_5", 0, "ui_kingdom_shield_5", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_6", 0, "ui_kingdom_shield_6", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mouse_arrow_down", 0, "mouse_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_right", 0, "mouse_arrow_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_left", 0, "mouse_arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_up", 0, "mouse_arrow_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_plus", 0, "mouse_arrow_plus", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_left_click", 0, "mouse_left_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_right_click", 0, "mouse_right_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("status_ammo_ready", 0, "status_ammo_ready", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("ui_quick_battle_a", 0, "ui_quick_battle_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_bg_plane_a", 0, "white_bg_plane_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_icon_infantry", 0, "cb_ui_icon_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_icon_archer", 0, "cb_ui_icon_archer", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_icon_horseman", 0, "cb_ui_icon_horseman", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_01", 0, "cb_ui_maps_scene_01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_02", 0, "cb_ui_maps_scene_02", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_03", 0, "cb_ui_maps_scene_03", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_04", 0, "cb_ui_maps_scene_04", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_05", 0, "cb_ui_maps_scene_05", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_06", 0, "cb_ui_maps_scene_06", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_07", 0, "cb_ui_maps_scene_07", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_08", 0, "cb_ui_maps_scene_08", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_09", 0, "cb_ui_maps_scene_09", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_host_maps_14", 0, "mp_ui_host_maps_c4", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_15", 0, "mp_ui_host_maps_c5", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("quit_adv", 0, "quit_adv", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("quit_adv_b", 0, "quit_adv_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("ui_kingdom_shield_7", 0, "ui_kingdom_shield_7", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("flag_project_rb", 0, "flag_project_rb", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rb_miss", 0, "flag_project_rb_miss", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_16", 0, "mp_ui_host_maps_d1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_17", 0, "mp_ui_host_maps_d2", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_maps_18", 0, "mp_ui_host_maps_d3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("tableau_mesh_pw_banner_pole", 0, "tableau_mesh_pw_banner_pole",  0, 0, 0, 0, 0, 0, 1, 1, 1),

]
