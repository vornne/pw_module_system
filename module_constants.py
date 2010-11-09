##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_faction_id                = 0
slot_player_spawn_state               = 1
slot_player_spawn_invulnerable_time   = 2
slot_player_spawn_hit_points          = 3
slot_player_spawn_entry_point         = 4

player_spawn_state_dead               = 0
player_spawn_state_invulnerable       = 1
player_spawn_state_at_marker          = 2
player_spawn_state_alive              = 3

slot_player_equip_item_0              = 20
slot_player_equip_item_1              = 21
slot_player_equip_item_2              = 22
slot_player_equip_item_3              = 23
slot_player_equip_head                = 24
slot_player_equip_body                = 25
slot_player_equip_foot                = 26
slot_player_equip_gloves              = 27
slot_player_equip_horse               = 28
slot_player_equip_end                 = 29

########################################################
##  AGENT SLOTS            #############################
########################################################


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

slot_scene_prop_item_id               = 0
slot_scene_prop_gold_value            = 1
slot_scene_prop_gold_multiplier       = 2
slot_scene_prop_use_string            = 3
slot_scene_prop_troop_id              = 4

slot_scene_prop_linked_scene_prop     = 10
slot_scene_prop_linked_scene_prop_1   = 10
slot_scene_prop_linked_scene_prop_2   = 11
slot_scene_prop_linked_scene_prop_3   = 12
linked_scene_prop_slot_count          = 3

slot_scene_prop_position              = 15
slot_scene_prop_target_position       = 16

slot_scene_prop_attached_to_agent     = 19

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_difficulty                  = 0
slot_item_length                      = 1

########################################################
##  FACTION SLOTS          #############################
########################################################

slot_faction_banner_mesh              = 0

########################################################
##  SCENE SLOTS            #############################
########################################################


########################################################
##  TROOP SLOTS            #############################
########################################################

troop_slot_count_per_equipment_type   = 5
slot_troop_equipment_one_hand_begin   = 0
slot_troop_equipment_two_hand_begin   = 1 * troop_slot_count_per_equipment_type
slot_troop_equipment_ranged_begin     = 2 * troop_slot_count_per_equipment_type
slot_troop_equipment_ammo_begin       = 3 * troop_slot_count_per_equipment_type
slot_troop_equipment_shield_begin     = 4 * troop_slot_count_per_equipment_type
slot_troop_equipment_head_begin       = 5 * troop_slot_count_per_equipment_type
slot_troop_equipment_body_begin       = 6 * troop_slot_count_per_equipment_type
slot_troop_equipment_foot_begin       = 7 * troop_slot_count_per_equipment_type
slot_troop_equipment_hand_begin       = 8 * troop_slot_count_per_equipment_type
slot_troop_equipment_horse_begin      = 9 * troop_slot_count_per_equipment_type

slot_player_array_size                = 0
slot_player_array_begin               = 1

player_array_unique_id                = 0
player_array_troop_id                 = 1
player_array_faction_id               = 2
player_array_gold_value               = 3
player_array_entry_size               = 4

slot_mission_data_castle_owner_faction_begin    = 0
slot_mission_data_castle_owner_faction_end      = 8

########################################################
##  TEAM SLOTS             #############################
########################################################


########################################################

team_active_players                   = 0
team_spawn_invulnerable               = 1

spawn_invulnerable_time               = 10

loop_player_check_interval            = 5

max_distance_to_play_sound            = 10000
max_distance_to_see_labels            = 1500

seconds_before_removing_dropped_item  = 300
sell_item_gold_multiplier             = 80

winch_type_drawbridge                 = 0
winch_type_portcullis                 = 1

all_items_begin = "itm_straw_hat"
all_items_end = "itm_all_items_end"

wielded_items_begin = "itm_club"
wielded_items_end = "itm_all_items_end"

playable_troops_begin = "trp_peasant"
playable_troops_end = "trp_playable_troops_end"

factions_begin = "fac_commoners"
castle_factions_begin = "fac_1"
factions_end = "fac_factions_end"

castle_names_begin = "str_castle_name_0"
castle_names_end = "str_castle_names_end"

scenes_begin = 0
scenes_end = "scn_scenes_end"

scene_names_begin = "str_scene_name_1"
scene_names_end = "str_scene_names_end"

game_type_mission_templates_begin = "mt_conquest"
game_type_mission_templates_end = "mt_edit_scene"

game_type_names_begin = "str_game_type_1"
game_type_names_end = "str_game_types_end"

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end = "mesh_arms_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"
