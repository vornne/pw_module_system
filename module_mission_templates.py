from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
#
####################################################################################################################

mission_templates = [
  ("conquest", mtf_battle_mode, -1, "Fight for control of the castles.",
   [
    (0,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    ],
   [
    (ti_before_mission_start, 0, 0, [],
     [(scene_set_day_time, 12),
      (server_set_melee_friendly_fire, 1),
      (server_set_friendly_fire_damage_self_ratio, 0),
      (server_set_friendly_fire_damage_friend_ratio, 100),
      (team_set_relation, 0, 0, -1),
      (multiplayer_is_server),
      (call_script, "script_setup_owner_faction_for_castles"),
      (call_script, "script_setup_all_linked_scene_props"),
      ]),

    (ti_after_mission_start, 0, 0, [],
     [(set_spawn_effector_scene_prop_kind, 0, -1),
      (set_spawn_effector_scene_prop_kind, 1, -1),
      (assign, "$g_preset_message_display_enabled", 0),
      (multiplayer_is_server),
      (call_script, "script_setup_scene_props_after_mission_start"),
      ]),

    (ti_server_player_joined, 0, 0, [],
     [(store_trigger_param_1, ":player_id"),
      (player_set_team_no, ":player_id", 0),
      (call_script, "script_setup_player_joined", ":player_id"),
      ]),

    (ti_on_agent_spawn, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (agent_get_player_id, ":player_id", ":agent_id"),
      (try_begin),
        (player_is_active, ":player_id"),
        (player_get_slot, ":spr_instance_id", ":player_id", slot_player_respawn_at_scene_prop),
        (try_begin),
          (gt, ":spr_instance_id", 0),
          (prop_instance_get_position, pos1, ":spr_instance_id"),
          (position_move_y, pos1, -100),
          (position_move_z, pos1, 100),
          (position_set_z_to_ground_level, pos1),
          (agent_set_position, ":agent_id", pos1),
          (player_set_slot, ":player_id", slot_player_respawn_at_scene_prop, 0),
        (try_end),
      (try_end),
      ]),

    (0, 0, 0.1,
     [(multiplayer_is_server),
      (val_add, "$g_loop_player_id", 1),
      (get_max_players, ":max_players"),
      (try_begin),
        (ge, "$g_loop_player_id", ":max_players"),
        (assign, "$g_loop_player_id", 0),
        (store_mission_timer_a, ":time"),
        (try_begin),
          (ge, ":time", "$g_loop_player_check_time"),
          (val_add, "$g_loop_player_check_time", loop_player_check_interval),
          (assign, "$g_loop_player_check", 1),
        (else_try),
          (assign, "$g_loop_player_check", 0),
        (try_end),
      (try_end),
      (try_begin),
        (gt, "$g_loop_player_id", 0),
        (assign, ":player_id", "$g_loop_player_id"),
        (try_begin),
          (eq, "$g_loop_player_check", 1),
          (call_script, "script_player_check_stored_values", ":player_id"),
        (try_end),
        (player_is_active, ":player_id"),
        (call_script, "script_player_check_spawn_agent", ":player_id"),
      (try_end),
      (eq, "$g_loop_player_id", 0),
      ], []),

    (ti_escape_pressed, 0, 0, [],
     [(finish_mission),
      ]),

    (ti_battle_window_opened, 0, 0, [],
     [(try_begin),
        (eq, "$g_display_agent_labels", 1),
        (start_presentation, "prsnt_display_agent_labels"),
      (try_end),
      ]),

    (0, 0, 0, [(game_key_clicked, gk_character_window)],
     [(try_begin),
        (eq, "$g_display_agent_labels", 0),
        (assign, "$g_display_agent_labels", 1),
        (start_presentation, "prsnt_display_agent_labels"),
      (else_try),
        (assign, "$g_display_agent_labels", 0),
      (try_end),
      ]),

    (0, 1, 1, [(key_clicked, key_slash)],
     [(multiplayer_send_message_to_server, client_event_detach_scene_prop),
      ]),

    (1, 0, ti_once, [(neg|multiplayer_is_server)],
     [(assign, "$g_preset_message_display_enabled", 1),
      ]),

    ]),

  ("edit_scene", 0, -1, "edit_scene", [(0,0,0,0,1,[])],
   [
    (ti_before_mission_start, 0, 0, [],
     [(scene_set_day_time, 12),
      (server_set_add_to_game_servers_list, 0),
      (assign, "$g_edit_scene", 1),
      ]),

    (ti_escape_pressed, 0, 0, [],
     [(question_box, "str_leave_edit_mode"),
      ]),

    (ti_question_answered, 0, 0, [],
     [(store_trigger_param_1, ":answer"),
      (eq, ":answer", 0),
      (finish_mission),
      ]),

    (0, 0, 0, [(key_clicked, key_f12)],
     [(scene_prop_get_instance, ":instance_id", "spr_pw_test_gold", 0),
      (prop_instance_get_position, pos1, ":instance_id"),
      (get_player_agent_no, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos2, ":agent_id"),
      (get_distance_between_positions, reg1, pos1, pos2),
      (get_sq_distance_between_positions, reg2, pos1, pos2),
      (display_message, "str_distance_reg1_sq_distance_reg2"),
      ]),

    (0, 0, 0, [(key_clicked, key_f11)],
     [(get_player_agent_no, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos1, ":agent_id"),
      (position_move_x, 50),
      (set_spawn_position, pos1),
      (spawn_horse, "itm_test_horse"),
      ]),

    ]),
]
