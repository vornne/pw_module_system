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

slot_player_next_chat_event           = 5
slot_player_next_chat_event_type      = 6
slot_player_list_button_id            = 7
slot_player_outlaw_rating             = 8

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

slot_agent_horse_last_rider           = 0
slot_agent_drowning_count             = 1

########################################################
##  SCENE PROP SLOTS       #############################
########################################################

slot_scene_prop_item_id               = 0
slot_scene_prop_gold_value            = 1
slot_scene_prop_gold_multiplier       = 2
slot_scene_prop_use_string            = 3
slot_scene_prop_troop_id              = 4
slot_scene_prop_full_hit_points       = 5

slot_scene_prop_linked_scene_prop     = 10
slot_scene_prop_linked_scene_prop_1   = 10
slot_scene_prop_linked_scene_prop_2   = 11
slot_scene_prop_linked_scene_prop_3   = 12
linked_scene_prop_slot_count          = 3

slot_scene_prop_linked_sail           = slot_scene_prop_linked_scene_prop_1
slot_scene_prop_linked_sail_off       = slot_scene_prop_linked_scene_prop_2
slot_scene_prop_linked_ramp           = slot_scene_prop_linked_scene_prop_3

slot_scene_prop_position              = 15
slot_scene_prop_target_position       = 16
slot_scene_prop_rotation              = 17
slot_scene_prop_target_rotation       = 18

slot_scene_prop_attached_to_agent     = 19
slot_scene_prop_controlling_agent     = 20
slot_scene_prop_length                = 21
slot_scene_prop_width                 = 22
slot_scene_prop_collision_kind        = 23

slot_scene_prop_next_resource_hp      = 30
slot_scene_prop_state                 = 31
slot_scene_prop_state_time            = 32

scene_prop_state_active               = 0
scene_prop_state_destroyed            = 1
scene_prop_state_hidden               = 2
scene_prop_state_regenerating         = 3

slot_scene_prop_inventory_max_size    = 998
slot_scene_prop_inventory_count       = 999
slot_scene_prop_inventory_begin       = 1000
slot_scene_prop_inventory_obj_begin   = 2000
slot_scene_prop_inventory_obj_item_0  = 2990
slot_scene_prop_inventory_mesh_begin  = 3000
slot_scene_prop_inventory_mesh_item_0 = 3990

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_difficulty                  = 0
slot_item_length                      = 1
slot_item_class                       = 2
slot_item_resource_amount             = 3

item_class_none                       = 0
item_class_repair                     = 1
item_class_wood_cutting               = 2
item_class_wood                       = 3
item_class_mining                     = 4
item_class_iron                       = 5

########################################################
##  FACTION SLOTS          #############################
########################################################

slot_faction_banner_mesh              = 0
slot_faction_name_is_custom           = 1

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
player_array_outlaw_rating            = 4
player_array_entry_size               = 5

slot_mission_data_castle_owner_faction_begin    = 0
slot_mission_data_castle_owner_faction_end      = 8
slot_mission_data_faction_to_change_name_of     = 100

slot_last_chat_message_event          = 0
slot_last_chat_message_event_type     = 1
slot_last_chat_message_not_recieved   = 2

chat_event_type_local                 = 0
chat_event_type_local_shout           = 1
chat_event_type_set_faction_name      = 2

slot_ship_array_count                 = 0
slot_ship_array_begin                 = 1
slot_ship_array_collision_props_count = 100
slot_ship_array_collision_props_begin = 101

########################################################
##  TEAM SLOTS             #############################
########################################################


########################################################

team_default                          = 0
team_spawn_invulnerable               = 1
team_spectators                       = 2
team_faction_1                        = 3
team_faction_2                        = 4
team_faction_3                        = 5
team_faction_4                        = 6

spawn_invulnerable_time               = 10

loop_player_check_interval            = 5
loop_player_check_outlaw_interval     = 60
loop_horse_check_interval             = 30

max_distance_to_play_sound            = 10000
max_distance_to_see_labels            = 1500
max_distance_horse_rider              = 2000
max_distance_local_chat               = 3000
max_distance_local_chat_shout         = 5000
ambient_distance_local_chat           = 1000
ambient_distance_local_chat_shout     = 2000
z_position_to_hide_object             = -4999
max_distance_to_use                   = 200

seconds_before_removing_dropped_item  = 300
sell_item_gold_multiplier             = 80

winch_type_drawbridge                 = 0
winch_type_portcullis                 = 1

repairable_hit                        = 0
repairable_destroyed                  = 1
repairable_hit_destroyed              = 2
repairable_repairing                  = 3
repairable_resource_required          = 4
repairable_repaired                   = 5

destroy_scene_prop_hit_points         = 200
fell_tree_hit_points                  = 500
sink_ship_hit_points                  = 500

ship_station_not_on_ship              = 0
ship_station_none                     = 1
ship_station_mast                     = 2
ship_station_rudder                   = 3

ship_forwards_maximum                 = 4
ship_rotation_maximum                 = 5
ship_forwards_multiplier              = 200
ship_rotation_multiplier              = 5

escape_menu_item_height               = 35
admin_panel_item_height               = 40

outlaw_rating_for_kill                = 5
outlaw_rating_outlawed                = 15

inventory_slots_per_row               = 6
inventory_slot_spacing                = 100

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

banner_items_begin = "itm_pw_banner_pole_a01"
banner_items_end = "itm_test_horse"

commands_module_system_names_begin = "str_bot_count"
