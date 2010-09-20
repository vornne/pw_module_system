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
      ]),

    (ti_after_mission_start, 0, 0, [],
     [(set_spawn_effector_scene_prop_kind, 0, -1),
      (set_spawn_effector_scene_prop_kind, 1, -1),
      (assign, "$g_preset_message_display_enabled", 0),
      ]),

    (ti_server_player_joined, 0, 0, [],
     [(store_trigger_param_1, ":player_id"),
      (player_set_team_no, ":player_id", 0),
      (call_script, "script_setup_player_joined", ":player_id"),
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

    (1, 0, ti_once, [(neg|multiplayer_is_server)],
     [(assign, "$g_preset_message_display_enabled", 1),
      ]),

    ]),

    ("edit_scene", 0, -1, "edit_scene", [(0,0,0,0,1,[])],
     [(ti_before_mission_start, 0, 0, [], [(scene_set_day_time, 12)]), (ti_escape_pressed, 0, 0, [], [(finish_mission)])]),
]
