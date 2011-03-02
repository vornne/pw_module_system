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
slot_player_is_lord                   = 9
slot_player_non_lord_troop_id         = 10
slot_player_poll_faction_id           = 11

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
slot_player_equip_item_0_ammo         = 30
slot_player_equip_item_1_ammo         = 31
slot_player_equip_item_2_ammo         = 32
slot_player_equip_item_3_ammo         = 33

########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_horse_last_rider           = 0
slot_agent_drowning_count             = 1
slot_agent_poison_amount              = 2
slot_agent_poisoner_agent_id          = 3
slot_agent_freeze_instance_id         = 4

slot_agent_money_bag_1_value          = 10
slot_agent_money_bag_2_value          = 11
slot_agent_money_bag_3_value          = 12
slot_agent_money_bag_4_value          = 13

########################################################
##  SCENE PROP SLOTS       #############################
########################################################

slot_scene_prop_item_id               = 0
slot_scene_prop_gold_value            = 1
slot_scene_prop_gold_multiplier       = 2
slot_scene_prop_use_string            = 3
slot_scene_prop_troop_id              = 4
slot_scene_prop_full_hit_points       = 5
slot_scene_prop_is_mercenary          = 6

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
slot_scene_prop_stack_count           = 33
slot_scene_prop_stack_count_update_time = 34
slot_scene_prop_unlocked              = 35

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
slot_item_gender                      = 4

item_class_none                       = 0
item_class_repair                     = 1
item_class_wood_cutting               = 2
item_class_wood                       = 3
item_class_mining                     = 4
item_class_iron                       = 5
item_class_lock_pick                  = 6
item_class_heraldic                   = 7

########################################################
##  FACTION SLOTS          #############################
########################################################

slot_faction_banner_mesh              = 0
slot_faction_name_is_custom           = 1
slot_faction_is_active                = 2
slot_faction_lord_player_uid          = 3
slot_faction_lord_last_seen_time      = 4
slot_faction_castle_banner_type_begin = 5

slot_faction_poll_end_time            = 20
slot_faction_poll_voter_count         = 21
slot_faction_poll_yes_votes           = 22
slot_faction_poll_no_votes            = 23
slot_faction_poll_type                = 24
slot_faction_poll_value_1             = 25
slot_faction_poll_value_2             = 26
slot_faction_poll_target_unique_id    = 27

poll_type_change_scene                = 0
poll_type_kick_player                 = 1
poll_type_ban_player                  = 2
poll_type_faction_lord                = 10

poll_cost_change_scene                = 1000
poll_cost_kick_player                 = 500
poll_cost_ban_player                  = 700
poll_cost_faction_lord                = 500

poll_vote_no                          = 0
poll_vote_yes                         = 1
poll_vote_admin_no                    = 2
poll_vote_admin_yes                   = 3
poll_vote_abstain                     = 4
poll_result_no                        = -1
poll_result_yes                       = -2
poll_result_admin_no                  = -3
poll_result_admin_yes                 = -4
poll_result_existing                  = -5
poll_result_invalid                   = -6
poll_result_color                     = 0xFF0000

faction_cost_change_banner            = 500
faction_cost_change_name              = 500

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
slot_mission_data_castle_is_active_begin        = 10
slot_mission_data_castle_is_active_end          = 18
slot_mission_data_castle_name_string_begin      = 20
slot_mission_data_castle_name_string_end        = 28
slot_mission_data_castle_money_chest_begin      = 30
slot_mission_data_castle_money_chest_end        = 38
slot_mission_data_faction_to_change_name_of     = 100

slot_last_chat_message_event          = 0
slot_last_chat_message_event_type     = 1
slot_last_chat_message_not_recieved   = 2
slot_last_chat_message_buffer_color_begin       = 10

chat_event_type_local                 = 0
chat_event_type_local_shout           = 1
chat_event_type_set_faction_name      = 2

slot_ship_array_count                 = 0
slot_ship_array_begin                 = 1
slot_ship_array_collision_props_count = 100
slot_ship_array_collision_props_begin = 101

slot_removed_plants_count             = 0
slot_removed_plants_begin             = 1

########################################################
##  TEAM SLOTS             #############################
########################################################


########################################################

team_default                          = 0
team_spawn_invulnerable               = 1
team_spectators                       = 2

spawn_invulnerable_time               = 10
lord_wait_for_reconnect_interval      = 300
loop_player_check_interval            = 5
loop_player_check_outlaw_interval     = 60
loop_horse_check_interval             = 30
loop_health_check_interval            = 15
stack_count_check_interval            = 5
redraw_castle_banners_interval        = 60
poll_time_duration                    = 60

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
castle_tax_gold_multiplier            = 10
craft_skill_reward_gold_multiplier    = 100
base_export_multiplier                = 100

winch_type_drawbridge                 = 0
winch_type_portcullis                 = 1

repairable_hit                        = 0
repairable_destroyed                  = 1
repairable_hit_destroyed              = 2
repairable_repairing                  = 3
repairable_resource_required          = 4
repairable_repaired                   = 5

destroy_scene_prop_hit_points         = 200
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
chat_overlay_item_height              = 20
chat_overlay_max_lines                = 100
chat_overlay_ring_buffer_begin        = 60
chat_overlay_ring_buffer_size         = 10
chat_overlay_ring_buffer_end          = chat_overlay_ring_buffer_begin + chat_overlay_ring_buffer_size

outlaw_rating_for_kill                = 5
outlaw_rating_outlawed                = 15

inventory_slots_per_row               = 6
inventory_slot_spacing                = 100

all_items_begin = "itm_straw_hat"
all_items_end = "itm_all_items_end"

wielded_items_begin = "itm_club"
wielded_items_end = "itm_all_items_end"

scripted_items_begin = "itm_surgeon_scalpel"
scripted_items_end = "itm_money_bag"

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

admin_action_log_strings_begin = "str_log_admin_kick"

ambient_sounds_begin = "snd_fire_loop"
ambient_sounds_end = "snd_sounds_end"
