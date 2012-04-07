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

slot_player_inactive_index            = 5
slot_player_next_chat_event_type      = 6
slot_player_list_button_id            = 7
slot_player_outlaw_rating             = 8
slot_player_is_lord                   = 9
slot_player_non_lord_troop_id         = 10
slot_player_poll_faction_id           = 11
slot_player_requested_spawn_point     = 12
slot_player_has_faction_door_key      = 13
slot_player_has_faction_money_key     = 14
slot_player_has_faction_item_key      = 15
slot_player_teleport_to_ship_no       = 16
slot_player_last_faction_kicked_from  = 17
slot_player_accessing_instance_id     = 18
slot_player_last_action_time          = 19

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

slot_player_spawn_food_amount         = 34
slot_player_faction_chat_muted        = 35

slot_player_admin_no_panel            = 40
slot_player_admin_no_gold             = 41
slot_player_admin_no_kick             = 42
slot_player_admin_no_temporary_ban    = 43
slot_player_admin_no_permanent_ban    = 44
slot_player_admin_no_kill_fade        = 45
slot_player_admin_no_freeze           = 46
slot_player_admin_no_teleport_self    = 47
slot_player_admin_no_admin_items      = 48
slot_player_admin_no_heal_self        = 49
slot_player_admin_no_godlike_troop    = 50
slot_player_admin_no_ships            = 51
slot_player_admin_no_announce         = 52
slot_player_admin_no_override_poll    = 53
slot_player_admin_no_all_items        = 54
slot_player_admin_no_mute             = 55
slot_player_admin_no_animals          = 56
slot_player_admin_no_factions         = 57
slot_player_admin_end                 = 58

########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_horse_last_rider           = 0
slot_agent_drowning_count             = 1
slot_agent_poison_amount              = 2
slot_agent_poisoner_agent_id          = 3
slot_agent_poisoner_player_uid        = 4
slot_agent_freeze_instance_id         = 5
slot_agent_is_targeted                = 6
slot_agent_food_amount                = 7
slot_agent_fishing_last_school        = 8
slot_agent_last_horse_ridden          = 9

slot_agent_money_bag_1_value          = 10
slot_agent_money_bag_2_value          = 11
slot_agent_money_bag_3_value          = 12
slot_agent_money_bag_4_value          = 13

slot_agent_hunting_last_carcass       = 14

slot_agent_animal_herd_manager        = 20
slot_agent_animal_birth_time          = 21
slot_agent_animal_grow_time           = 22
slot_agent_animal_move_time           = 23
slot_agent_animal_last_damage_time    = 24
slot_agent_animal_meat_count          = 25
slot_agent_animal_hide_count          = 26
slot_agent_animal_times_stuck         = 27
slot_agent_animal_end                 = 28

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
slot_scene_prop_required_horse        = 7

slot_scene_prop_linked_scene_prop     = 10
slot_scene_prop_linked_scene_prop_1   = 10
slot_scene_prop_linked_scene_prop_2   = 11
slot_scene_prop_linked_scene_prop_3   = 12
slot_scene_prop_linked_scene_prop_4   = 13
linked_scene_prop_slot_count          = 4

slot_scene_prop_linked_sail           = slot_scene_prop_linked_scene_prop_1
slot_scene_prop_linked_sail_off       = slot_scene_prop_linked_scene_prop_2
slot_scene_prop_linked_ramp           = slot_scene_prop_linked_scene_prop_3
slot_scene_prop_linked_hold           = slot_scene_prop_linked_scene_prop_4

slot_scene_prop_linked_platform_1     = slot_scene_prop_linked_scene_prop_1
slot_scene_prop_linked_platform_2     = slot_scene_prop_linked_scene_prop_2
slot_scene_prop_linked_ferry_winch    = slot_scene_prop_linked_scene_prop_3

slot_scene_prop_position              = 15
slot_scene_prop_target_position       = 16
slot_scene_prop_rotation              = 17
slot_scene_prop_target_rotation       = 18
slot_scene_prop_max_position          = slot_scene_prop_rotation
slot_scene_prop_max_distance          = slot_scene_prop_target_rotation

slot_scene_prop_attached_to_agent     = 19
slot_scene_prop_controlling_agent     = 20
slot_scene_prop_length                = 21
slot_scene_prop_width                 = 22
slot_scene_prop_height                = 23
slot_scene_prop_collision_kind        = 24
slot_scene_prop_speed_limit           = 25
slot_scene_prop_no_move_physics       = 26

slot_scene_prop_next_resource_hp      = 30
slot_scene_prop_state                 = 31
slot_scene_prop_state_time            = 32
slot_scene_prop_stock_count           = 33
slot_scene_prop_stock_count_update_time = 34
slot_scene_prop_unlocked              = 35
slot_scene_prop_regrow_script         = 36
slot_scene_prop_resource_item_id      = 37

slot_scene_prop_water                 = 40
slot_scene_prop_seeds                 = 41

scene_prop_state_active               = 0
scene_prop_state_destroyed            = 1
scene_prop_state_hidden               = 2
scene_prop_state_regenerating         = 3

slot_scene_prop_inventory_max_size    = 198
slot_scene_prop_inventory_count       = 199
slot_scene_prop_inventory_begin       = 200
slot_scene_prop_inventory_item_0      = 290
slot_scene_prop_inventory_ammo_begin  = 300
slot_scene_prop_inventory_mod_begin   = 400
slot_scene_prop_inventory_mod_item_0  = 490
slot_scene_prop_inventory_obj_begin   = 500
slot_scene_prop_inventory_obj_item_0  = 590
slot_scene_prop_inventory_mesh_begin  = 600
slot_scene_prop_inventory_mesh_item_0 = 690
slot_scene_prop_inventory_end         = slot_scene_prop_inventory_ammo_begin
slot_scene_prop_inventory_mod_end     = slot_scene_prop_inventory_obj_begin
slot_scene_prop_inventory_obj_end     = slot_scene_prop_inventory_mesh_begin
inventory_count_maximum               = slot_scene_prop_inventory_item_0 - slot_scene_prop_inventory_begin

slot_animal_herd_manager_adult_item_id= 100

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_difficulty                  = 0
slot_item_length                      = 1
slot_item_class                       = 2
slot_item_resource_amount             = 3
slot_item_gender                      = 4
slot_item_max_ammo                    = 5

item_class_none                       = 0
item_class_repair                     = 1
item_class_wood_cutting               = 2
item_class_wood                       = 3
item_class_mining                     = 4
item_class_iron                       = 5
item_class_lock_pick                  = 6
item_class_heraldic                   = 7
item_class_precious                   = 8
item_class_food                       = 9
item_class_grain_harvesting           = 10
item_class_knife                      = 11
item_class_cloth                      = 12
item_class_leather                    = 13
item_class_herding_calm               = 14
item_class_herding_rouse              = 15

slot_item_animal_adult_item_id        = 20
slot_item_animal_child_item_id        = 21
slot_item_animal_grow_time            = 22
slot_item_animal_max_in_herd          = 23
slot_item_animal_attack_reaction      = 24
slot_item_animal_death_sound          = 25
slot_item_animal_meat_count           = 26
slot_item_animal_hide_count           = 27

animal_reaction_flee                  = 0
animal_reaction_charge                = 1

########################################################
##  FACTION SLOTS          #############################
########################################################

slot_faction_banner_mesh              = 0
slot_faction_name_is_custom           = 1
slot_faction_is_active                = 2
slot_faction_lord_player_uid          = 3
slot_faction_lord_last_seen_time      = 4
slot_faction_castle_banner_variant    = 5
slot_faction_list_button_id           = 6
slot_faction_is_locked                = 7

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
poll_cost_faction_lord                = 1000

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

slot_faction_relations_begin          = 30

faction_cost_change_banner            = 500
faction_cost_change_name              = 500
faction_cost_kick_player              = 500
faction_cost_outlaw_player            = 1000

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

slot_troop_ranking                    = 50
slot_troop_spawn_health_percent       = 51

slot_player_array_size                = 0
slot_player_array_begin               = 1

player_array_unique_id                = 0
player_array_troop_id                 = 1
player_array_faction_id               = 2
player_array_gold_value               = 3
player_array_outlaw_rating            = 4
player_array_entry_size               = 5

max_castle_count = 8
slot_mission_data_castle_owner_faction_begin    = 0
slot_mission_data_castle_owner_faction_end      = 8
slot_mission_data_castle_is_active_begin        = 10
slot_mission_data_castle_is_active_end          = 18
slot_mission_data_castle_name_string_begin      = 20
slot_mission_data_castle_name_string_end        = 28
slot_mission_data_castle_money_chest_begin      = 30
slot_mission_data_castle_money_chest_end        = 38
slot_mission_data_castle_allows_training_begin  = 40
slot_mission_data_castle_allows_training_end    = 48
slot_mission_data_faction_to_change_name_of     = 100

slot_last_chat_message_event_type     = 0
slot_last_chat_message_not_recieved   = 1

chat_event_type_local                 = 0
chat_event_type_local_shout           = 1
chat_event_type_set_faction_name      = 2
chat_event_type_faction               = 4
chat_event_type_faction_lord          = 5
chat_event_type_admin                 = 6
chat_event_type_admin_shout           = 7

slot_chat_overlay_local_color         = 0
slot_chat_overlay_faction_color       = 1

slot_ship_array_count                 = 0
slot_ship_array_begin                 = 1
slot_ship_array_collision_props_count = 100
slot_ship_array_collision_props_begin = 101

slot_array_count                      = 0
slot_array_begin                      = 1

########################################################
##  TEAM SLOTS             #############################
########################################################


########################################################

team_default                          = 0
team_spawn_invulnerable               = 1
team_spectators                       = 2

spawn_invulnerable_time               = 10
loop_player_check_outlaw_interval     = 60
loop_agent_check_interval             = 2
loop_horse_check_interval             = 30
loop_health_check_interval            = 15
stock_count_check_interval            = 5
repeat_action_min_interval            = 5
carcass_search_min_interval           = 5
poll_time_duration                    = 60

max_distance_to_play_sound            = 10000
max_distance_to_see_labels            = 1500
max_distance_horse_rider              = 5000
max_distance_local_chat               = 3000
max_distance_local_chat_shout         = 5000
ambient_distance_local_chat           = 1000
ambient_distance_local_chat_shout     = 2000
z_position_to_hide_object             = -4999
z_position_water_level                = -30
max_distance_to_use                   = 300
max_distance_to_loot                  = 100
max_distance_to_catch_fish            = 2000
fish_school_minimum_depth             = 200
fish_spawn_time                       = 300
max_distance_to_include_in_herd       = 5000

sell_item_gold_multiplier             = 80
castle_tax_gold_multiplier            = 20
castle_training_gold_multiplier       = 50
craft_skill_reward_gold_multiplier    = 100
base_export_multiplier                = 100

winch_type_drawbridge                 = 0
winch_type_portcullis                 = 1
winch_type_platform                   = 2

repairable_hit                        = 0
repairable_destroyed                  = 1
repairable_hit_destroyed              = 2
repairable_repairing                  = 3
repairable_resource_required          = 4
repairable_repaired                   = 5

min_scene_prop_hit_points             = 1

ship_station_not_on_ship              = 0
ship_station_none                     = 1
ship_station_mast                     = 2
ship_station_rudder                   = 3

ship_forwards_maximum                 = 9
ship_rotation_maximum                 = 5
ship_forwards_multiplier              = 100
ship_rotation_multiplier              = 3

player_list_item_height               = 20
escape_menu_item_height               = 35
admin_panel_item_height               = 40
action_menu_item_height               = 23
faction_menu_item_height              = 120
chat_overlay_item_height              = 17
chat_overlay_ring_buffer_begin        = "trp_chat_overlay_ring_buffer_0"
chat_overlay_ring_buffer_end          = "trp_chat_overlay_ring_buffer_end"
chat_overlay_ring_buffer_size         = 11
local_chat_color                      = 0xFFFFDD8A
local_chat_shout_color                = 0xFFFF8C27
admin_chat_color                      = 0xFFFF00FF
invalid_faction_color                 = 0xFF888888

outlaw_rating_for_kill                = 2
outlaw_rating_for_team_kill           = 5
outlaw_rating_for_lord_outlawed       = 4
outlaw_rating_outlawed                = 15
outlaw_rating_maximum                 = 30

change_faction_type_respawn           = 0
change_faction_type_no_respawn        = 1
change_faction_type_outlawed          = 2

redraw_all_banners                    = 0
redraw_castle_banners                 = 1
redraw_faction_banners                = 2

inventory_slots_per_row               = 6
inventory_slot_spacing                = 100
inventory_mesh_offset                 = 50
inventory_container_x_offset          = 190
inventory_container_y_offset          = 175

select_agent_max_x                    = 300
select_agent_max_y                    = 200
presentation_max_x                    = 1000
presentation_max_y                    = 750

max_scene_prop_instance_id            = 10000

max_food_amount                       = 100

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
banner_meshes_end = "mesh_banners_default_a"
banner_meshes_end_minus_one = "mesh_banner_f21"

banner_items_begin = "itm_pw_banner_pole_a01"
banner_items_end = "itm_admin_horse"

commands_module_system_names_begin = "str_bot_count"

admin_action_log_strings_begin = "str_log_admin_kick"

ambient_sounds_begin = "snd_fire_loop"
ambient_sounds_end = "snd_sounds_end"

action_menu_strings_begin = "str_toggle_name_labels"
action_menu_strings_end = "str_action_menu_end"
