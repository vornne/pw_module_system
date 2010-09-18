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
      ]),

    (ti_server_player_joined, 0, 0, [],
     [(store_trigger_param_1, ":player_id"),
      (player_set_team_no, ":player_id", 0),
      (player_set_troop_id, ":player_id", "trp_peasant"),
      ]),

    (0, 0, 0, [(multiplayer_is_server)],
     [(val_add, "$g_loop_player_id", 1),
      (get_max_players, ":max_players"),
      (try_begin),
        (ge, "$g_loop_player_id", ":max_players"),
        (assign, "$g_loop_player_id", 0),
      (try_end),

      (player_is_active, "$g_loop_player_id"),
      (neg|player_is_busy_with_menus, "$g_loop_player_id"),
      (player_get_agent_id, ":agent_id", "$g_loop_player_id"),
      (this_or_next|lt, ":agent_id", 0),
      (neg|agent_is_alive, ":agent_id"),
      (player_get_troop_id, ":troop_id", "$g_loop_player_id"),
      (call_script, "script_player_add_spawn_items", "$g_loop_player_id", ":troop_id"),
      (player_spawn_new_agent, "$g_loop_player_id", 0),
      ]),

    (ti_escape_pressed, 0, 0, [],
     [(finish_mission),
      ]),

    ]),

    ("edit_scene", 0, -1, "edit_scene", [(0,0,0,0,1,[])],
     [(ti_before_mission_start, 0, 0, [], [(scene_set_day_time, 12)]), (ti_escape_pressed, 0, 0, [], [(finish_mission)])]),
]
