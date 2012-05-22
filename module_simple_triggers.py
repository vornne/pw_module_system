from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################



simple_triggers = [

# This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead  
  (ti_on_party_encounter,
   [
    ]),


# This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead 
  (ti_simulate_battle,
   [
    ]),


  (1,
   [
      (try_begin),
        (eq, "$training_ground_position_changed", 0),
        (assign, "$training_ground_position_changed", 1),
		(set_fixed_point_multiplier, 100),
        (position_set_x, pos0, 7050),
        (position_set_y, pos0, 7200),
        (party_set_position, "p_training_ground_3", pos0),
      (try_end),
	  
      (gt,"$auto_besiege_town",0),
      (gt,"$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
      (store_current_hours, ":cur_hours"),
      (eq, "$g_siege_force_wait", 0),
      (ge, ":cur_hours", "$g_siege_method_finish_hours"),
      (neg|is_currently_night),
      (rest_for_hours, 0, 0, 0), #stop resting
    ]),


  (0,
   [
      (try_begin),
        (eq, "$bug_fix_version", 0),     
      
        #fix for hiding test_scene in older savegames
        (disable_party, "p_test_scene"),
        #fix for correcting town_1 siege type
        (party_set_slot, "p_town_1", slot_center_siege_with_belfry, 0),
        #fix for hiding player_faction notes
        (faction_set_note_available, "fac_player_faction", 0),
        #fix for hiding faction 0 notes
        (faction_set_note_available, "fac_no_faction", 0),
        #fix for removing kidnapped girl from party
        (try_begin),
          (neg|check_quest_active, "qst_kidnapped_girl"),
          (party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
        (try_end),
        #fix for not occupied but belong to a faction lords
        (try_for_range, ":cur_troop", lords_begin, lords_end),
          (try_begin),                
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_inactive),
            (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
            (is_between, ":cur_troop_faction", "fac_kingdom_1", kingdoms_end),          
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),          
          (try_end),
        (try_end),  
        #fix for an error in 1.105, also fills new slot values
        (call_script, "script_initialize_item_info"),  
        
        (assign, "$bug_fix_version", 1),     
      (try_end),  

      (eq,"$g_player_is_captive",1),
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
    ]),


#Auto-menu
  (0,
   [          
     (try_begin),
       (gt, "$g_last_rest_center", 0),
       (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
       (gt, ":besieger_party", 0),
       (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
       (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
       (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
       (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
       (ge, ":faction_relation", 0),
       (lt, ":besieger_party_relation", 0),
       (start_encounter, "$g_last_rest_center"),
       (rest_for_hours, 0, 0, 0), #stop resting
     (else_try),
       (store_current_hours, ":cur_hours"),
       (assign, ":check", 0),
       (try_begin),
         (neq, "$g_check_autos_at_hour", 0),
         (ge, ":cur_hours", "$g_check_autos_at_hour"),
         (assign, ":check", 1),
         (assign, "$g_check_autos_at_hour", 0),
       (try_end),
       (this_or_next|eq, ":check", 1),
       (map_free),
       (try_begin),
         (ge,"$auto_menu",1),
         (jump_to_menu,"$auto_menu"),
         (assign,"$auto_menu",-1),
       (else_try),
         (ge,"$auto_enter_town",1),
         (start_encounter, "$auto_enter_town"),
       (else_try),
         (ge,"$auto_besiege_town",1),
         (start_encounter, "$auto_besiege_town"),
       (else_try),
         (ge,"$g_camp_mode", 1),
         (assign, "$g_camp_mode", 0),
         (assign, "$g_infinite_camping", 0),
         (assign, "$g_player_icon_state", pis_normal),
         
         (rest_for_hours, 0, 0, 0), #stop camping
                  
         (display_message, "@Breaking camp..."),
       (try_end),
     (try_end),
     ]),


#Notification menus
  (0,
   [
     (troop_slot_ge, "trp_notification_menu_types", 0, 1),
     (troop_get_slot, ":menu_type", "trp_notification_menu_types", 0),
     (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
     (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
     (jump_to_menu, ":menu_type"),
     (assign, ":end_cond", 2),
     (try_for_range, ":cur_slot", 1, ":end_cond"),
       (try_begin),
         (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
         (val_add, ":end_cond", 1),
       (try_end),
       (store_sub, ":cur_slot_minus_one", ":cur_slot", 1),
       (troop_get_slot, ":local_temp", "trp_notification_menu_types", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_types", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var1", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var1", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var2", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var2", ":cur_slot_minus_one", ":local_temp"),
     (try_end),
    ]),

  #Music,
  (1,
   [
       (map_free),
       (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
	    ]),	

  (0,
	[
	  #escort caravan quest auto dialog trigger
	  (try_begin),
        (eq, "$caravan_escort_state", 1),
        (party_is_active, "$caravan_escort_party_id"),
		
        (store_distance_to_party_from_party, ":caravan_distance_to_destination","$caravan_escort_destination_town","$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_destination", 2),
        
        (store_distance_to_party_from_party, ":caravan_distance_to_player","p_main_party","$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_player", 5),

        (assign, "$talk_context", tc_party_encounter),
        (assign, "$g_encountered_party", "$caravan_escort_party_id"),
        (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),     
        (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),    
        
        (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
      (try_end),
      
      (try_begin),
        (gt, "$g_reset_mission_participation", 1),
        
        (try_for_range, ":troop", active_npcs_begin, kingdom_ladies_end),
          (troop_set_slot, ":troop", slot_troop_mission_participation, 0),
        (try_end),
      (try_end),
	]),
	
(24, 
[
    (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
      (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),

	  (store_sub, ":divisor", 140, "$player_right_to_rule"),
	  (val_div, ":divisor", 14),
	  (val_max, ":divisor", 1),
	  
      (store_div, ":faction_morale_div_10", ":faction_morale", ":divisor"), #10 is the base, down to 2 for 100 rtr     
      (val_sub, ":faction_morale", ":faction_morale_div_10"),           

      (faction_set_slot, ":kingdom_no",  slot_faction_morale_of_player_troops, ":faction_morale"),
    (try_end),
]),

	
 (4, #Locate kingdom ladies
    [
      #change location for all ladies
      (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
        (neg|troop_slot_ge, ":troop_id", slot_troop_prisoner_of_party, 0),
        (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
        (assign, ":location", reg1),
        (troop_set_slot, ":troop_id", slot_troop_cur_center, ":location"),
      (try_end),	
	]),

	
 (2, #Error check for multiple parties on the map
	[
	(eq, "$cheat_mode", 1),
	(assign, ":debug_menu_noted", 0),
	(try_for_parties, ":party_no"),
		(gt, ":party_no", "p_spawn_points_end"),
		(party_stack_get_troop_id, ":commander", ":party_no", 0),
		(is_between, ":commander", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":commander_party", ":commander", slot_troop_leaded_party),
		(neq, ":party_no", ":commander_party"),
		(assign, reg4, ":party_no"),
		(assign, reg5, ":commander_party"),
		
		(str_store_troop_name, s3, ":commander"),
		(display_message, "@{!}{s3} commander of party #{reg4} which is not his troop_leaded party {reg5}"), 
		(str_store_string, s65, "str_party_with_commander_mismatch__check_log_for_details_"),

		(try_begin),
			(eq, ":debug_menu_noted", 0),
			(call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
			(assign, ":debug_menu_noted", 1),
		(try_end),
	(try_end),
	]),	
	
   
 (24, #Kingdom ladies send messages
 [ 
	(try_begin),
		(neg|check_quest_active, "qst_visit_lady"),
		(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
		(neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
		
		(assign, ":lady_not_visited_longest_time", -1),
		(assign, ":longest_time_without_visit", 120), #five days
		
		(try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
		
			#set up message for ladies the player is courting
			(troop_slot_ge, ":troop_id", slot_troop_met, 2),
			(neg|troop_slot_eq, ":troop_id", slot_troop_met, 4),
			
			(troop_slot_eq, ":troop_id", slot_lady_no_messages, 0),
			(troop_slot_eq, ":troop_id", slot_troop_spouse, -1),
			
			(troop_get_slot, ":location", ":troop_id", slot_troop_cur_center),
			(is_between, ":location", walled_centers_begin, walled_centers_end),
			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_id"),
			(gt, reg0, 1),
			
			(store_current_hours, ":hours_since_last_visit"),
			(troop_get_slot, ":last_visit_hour", ":troop_id", slot_troop_last_talk_time),
			(val_sub, ":hours_since_last_visit", ":last_visit_hour"),
			
			(gt, ":hours_since_last_visit", ":longest_time_without_visit"),
			(assign, ":longest_time_without_visit", ":hours_since_last_visit"),
			(assign, ":lady_not_visited_longest_time", ":troop_id"),
			(assign, ":visit_lady_location", ":location"),
		
		(try_end),
		
		(try_begin),
			(gt, ":lady_not_visited_longest_time", 0),
			(call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":lady_not_visited_longest_time", ":visit_lady_location"),
		(try_end),
		
	(try_end),	
	]),
   
   
#Player raiding a village
# This trigger will check if player's raid has been completed and will lead control to village menu.
  (1,
   [
      (ge,"$g_player_raiding_village",1),
      (try_begin),
        (neq, "$g_player_is_captive", 0),
        #(rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
      (else_try),
        (map_free), #we have been attacked during raid
        (assign,"$g_player_raiding_village",0),
      (else_try),
        (this_or_next|party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_looted),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_deserted),
        (start_encounter, "$g_player_raiding_village"),
        (rest_for_hours, 0),
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",1),
      (else_try),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_being_raided),
        (rest_for_hours, 3, 5, 1), #rest while attackable
      (else_try),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",0),
      (try_end),
    ]),

  #Pay day.
  (24 * 7,
   [
     (assign, "$g_presentation_lines_to_display_begin", 0),
     (assign, "$g_presentation_lines_to_display_end", 15),
     (assign, "$g_apply_budget_report_to_gold", 1),
     (try_begin),
       (eq, "$g_infinite_camping", 0),
       (start_presentation, "prsnt_budget_report"),
     (try_end),
    ]),

  # Oath fulfilled -- ie, mercenary contract expired?
  (24,
   [
      (le, "$auto_menu", 0),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (eq, "$player_has_homage", 0),
	  
	  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	  
	  #A player bound to a kingdom by marriage will not have the contract expire. This should no longer be the case, as I've counted wives as having homage, but is in here as a fallback
	  (assign, ":player_has_marriage_in_faction", 0),
	  (try_begin),
		(is_between, ":player_spouse", active_npcs_begin, active_npcs_end),
		(store_faction_of_troop, ":spouse_faction", ":player_spouse"),
		(eq, ":spouse_faction", "$players_kingdom"),
	    (assign, ":player_has_marriage_in_faction", 1),
	  (try_end),
	  (eq, ":player_has_marriage_in_faction", 0),
	  
      (store_current_day, ":cur_day"),
      (gt, ":cur_day", "$mercenary_service_next_renew_day"),
      (jump_to_menu, "mnu_oath_fulfilled"),
    ]),

  # Reducing luck by 1 in every 180 hours
  (180,
   [
     (val_sub, "$g_player_luck", 1),
     (val_max, "$g_player_luck", 0),
    ]),

	#courtship reset
  (72,
   [
     (assign, "$lady_flirtation_location", 0),
    ]),

	#reset time to spare
  (4,
   [
     (assign, "$g_time_to_spare", 1),

    (try_begin),
		(troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
		(assign, "$g_player_banner_granted", 1),
	(try_end),

	 ]),

	
  # Banner selection menu
  (24,
   [
    (eq, "$g_player_banner_granted", 1),
    (troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
    (le,"$auto_menu",0),
#normal_banner_begin
    (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#    (start_presentation, "prsnt_custom_banner"),
    ]),

  # Party Morale: Move morale towards target value.
  (24,
   [
      (call_script, "script_get_player_party_morale_values"),
      (assign, ":target_morale", reg0),
      (party_get_morale, ":cur_morale", "p_main_party"),
      (store_sub, ":dif", ":target_morale", ":cur_morale"),
      (store_div, ":dif_to_add", ":dif", 5),
      (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
      (try_begin),#finding ceiling of the value
        (neq, ":dif_to_add_correction", ":dif"),
        (try_begin),
          (gt, ":dif", 0),
          (val_add, ":dif_to_add", 1),
        (else_try),
          (val_sub, ":dif_to_add", 1),
        (try_end),
      (try_end),
      (val_add, ":cur_morale", ":dif_to_add"),
      (party_set_morale, "p_main_party", ":cur_morale"),      
    ]),
  

#Party AI: pruning some of the prisoners in each center (once a week)
  (24*7,
   [
       (try_for_range, ":center_no", centers_begin, centers_end),
         (party_get_num_prisoner_stacks, ":num_prisoner_stacks",":center_no"),
         (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
           (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":stack_no"),
           (neg|troop_is_hero, ":stack_troop"),
           (party_prisoner_stack_get_size, ":stack_size",":center_no",":stack_no"),
           (store_random_in_range, ":rand_no", 0, 40),
           (val_mul, ":stack_size", ":rand_no"),
           (val_div, ":stack_size", 100),
           (party_remove_prisoners, ":center_no", ":stack_troop", ":stack_size"),
         (try_end),
       (try_end),
    ]),

  #Adding net incomes to heroes (once a week)
  #Increasing debts to heroes by 1% (once a week)
  #Adding net incomes to centers (once a week)
  (24*7,
   [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_get_slot, ":cur_debt", ":troop_no", slot_troop_player_debt),#Increasing debt
         (val_mul, ":cur_debt", 101),
         (val_div, ":cur_debt", 100),
         (troop_set_slot, ":troop_no", slot_troop_player_debt, ":cur_debt"),
         (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", ":troop_no"),#Adding net income
       (try_end),
	   
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         #If non-player center, adding income to wealth
         (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
         (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
         (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
         (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
         (store_mul, ":added_wealth", ":prosperity", 15),
         (val_add, ":added_wealth", 700),
         (try_begin),
           (party_slot_eq, ":center_no", slot_party_type, spt_town),
           (val_mul, ":added_wealth", 3),
           (val_div, ":added_wealth", 2),
         (try_end),
         (val_add, ":cur_wealth", ":added_wealth"),
         (call_script, "script_calculate_weekly_party_wage", ":center_no"),
         (val_sub, ":cur_wealth", reg0),
         (val_max, ":cur_wealth", 0),
         (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
       (try_end),
    ]),

  #Hiring men with hero wealths (once a day)
  #Hiring men with center wealths (once a day)
  (24,
   [
     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
       (ge, ":party_no", 1),
       (party_is_active, ":party_no"),
       (party_get_attached_to, ":cur_attached_party", ":party_no"),
       (is_between, ":cur_attached_party", centers_begin, centers_end),
       (party_slot_eq, ":cur_attached_party", slot_center_is_besieged_by, -1), #center not under siege
                       
       (store_faction_of_party, ":party_faction", ":party_no"),
       (try_begin),
         (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
         (eq, ":party_faction", "$players_kingdom"),        
         (assign, ":num_hiring_rounds", 1), 
         (store_random_in_range, ":random_value", 0, 2),         
         (val_add, ":num_hiring_rounds", ":random_value"),
       (else_try),
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
         (try_begin),
           (eq, ":reduce_campaign_ai", 0), #hard (2x reinforcing)
           (assign, ":num_hiring_rounds", 2),
         (else_try),
           (eq, ":reduce_campaign_ai", 1), #medium (1x or 2x reinforcing)
           (assign, ":num_hiring_rounds", 1), 
           (store_random_in_range, ":random_value", 0, 2),         
           (val_add, ":num_hiring_rounds", ":random_value"),
         (else_try),
           (eq, ":reduce_campaign_ai", 2), #easy (1x reinforcing)
           (assign, ":num_hiring_rounds", 1),          
         (try_end),                
       (try_end), 
       
       (try_begin),
         (faction_slot_eq,  ":party_faction", slot_faction_marshall, ":troop_no"),
         (val_add, ":num_hiring_rounds", 1),
       (try_end),
                
       (try_for_range, ":unused", 0, ":num_hiring_rounds"),         
         (call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"), #Hiring men with current wealth        
       (try_end),  
     (try_end),
       
     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
       (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
       (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.       
       (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #center not under siege
		 
       (store_faction_of_party, ":center_faction", ":center_no"),
       (try_begin),
         (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
         (eq, ":center_faction", "$players_kingdom"),        
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
       (else_try),
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
         (try_begin), 
           (eq, ":reduce_campaign_ai", 0), #hard (1x or 2x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_hard),
           (store_random_in_range, ":num_hiring_rounds", 0, 2),
           (val_add, ":num_hiring_rounds", 1),
         (else_try), 
           (eq, ":reduce_campaign_ai", 1), #moderate (1x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_moderate),
           (assign, ":num_hiring_rounds", 1),
         (else_try), 
           (eq, ":reduce_campaign_ai", 2), #easy (none or 1x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_easy),
           (store_random_in_range, ":num_hiring_rounds", 0, 2),
         (try_end),           
       (try_end),
       
       (try_for_range, ":unused", 0, ":num_hiring_rounds"), 		 
         (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
         (assign, ":hiring_budget", ":cur_wealth"),
         (val_div, ":hiring_budget", 2),
         (gt, ":hiring_budget", ":reinforcement_cost"),       
         (call_script, "script_cf_reinforce_party", ":center_no"),       
         (val_sub, ":cur_wealth", ":reinforcement_cost"),
         (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
       (try_end),  
     (try_end),

     #this is moved up from below , from a 24 x 15 slot to a 24 slot
     (try_for_range, ":center_no", centers_begin, centers_end),
       #(neg|is_between, ":center_no", castles_begin, castles_end),
       (store_random_in_range, ":random", 0, 30),
       (le, ":random", 10),
	   
       (call_script, "script_get_center_ideal_prosperity", ":center_no"),
       (assign, ":ideal_prosperity", reg0),
       (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),       
       (try_begin),
	     (eq, ":random", 0), #with 3% probability it will gain +10/-10 prosperity even it has higher prosperity than its ideal prosperity.
         (try_begin),
           (store_random_in_range, ":random", 0, 2),
           (try_begin),
             (eq, ":random", 0),
             (neg|is_between, ":center_no", castles_begin, castles_end), #castles always gain positive prosperity from surprise income to balance their prosperity.
             (call_script, "script_change_center_prosperity", ":center_no", -10),
             (val_add, "$newglob_total_prosperity_from_convergence", -10),
           (else_try),     
             (call_script, "script_change_center_prosperity", ":center_no", 10),
             (val_add, "$newglob_total_prosperity_from_convergence", 10),
           (try_end),
         (try_end),
	   (else_try),
         (gt, ":prosperity", ":ideal_prosperity"),		 
         (call_script, "script_change_center_prosperity", ":center_no", -1),
         (val_add, "$newglob_total_prosperity_from_convergence", -1),
       (else_try),
         (lt, ":prosperity", ":ideal_prosperity"),		 
         (call_script, "script_change_center_prosperity", ":center_no", 1),
         (val_add, "$newglob_total_prosperity_from_convergence", 1),
	   (try_end),
     (try_end),	   	   	   
    ]),

  #Converging center prosperity to ideal prosperity once in every 15 days
  (24*15,
   []),

  #Checking if the troops are resting at a half payment point
  (6,
   [(store_current_day, ":cur_day"),
    (try_begin),
      (neq, ":cur_day", "$g_last_half_payment_check_day"),
      (assign, "$g_last_half_payment_check_day", ":cur_day"),
      (try_begin),
        (eq, "$g_half_payment_checkpoint", 1),
        (val_add, "$g_cur_week_half_daily_wage_payments", 1), #half payment for yesterday
      (try_end),
      (assign, "$g_half_payment_checkpoint", 1),
    (try_end),
    (assign, ":resting_at_manor_or_walled_center", 0),
    (try_begin),
      (neg|map_free),
      (ge, "$g_last_rest_center", 0),
      (this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
      (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
      (assign, ":resting_at_manor_or_walled_center", 1),
    (try_end),
    (eq, ":resting_at_manor_or_walled_center", 0),
    (assign, "$g_half_payment_checkpoint", 0),
    ]),

#diplomatic indices
  (24,
   [
   (call_script, "script_randomly_start_war_peace_new", 1),

   (try_begin),
		(store_random_in_range, ":acting_village", villages_begin, villages_end),
		(store_random_in_range, ":target_village", villages_begin, villages_end),
		(store_faction_of_party, ":acting_faction", ":acting_village"),
		(store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
		(neq, ":acting_village", ":target_village"),
		(neq, ":acting_faction", ":target_faction"),
		
		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
		(eq, reg0, 0),

		(try_begin),
			(party_slot_eq, ":acting_village", slot_center_original_faction, ":target_faction"),
			
			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
		(else_try),
			(party_slot_eq, ":acting_village", slot_center_ex_faction, ":target_faction"),
			
			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
			
		(else_try),
			(set_fixed_point_multiplier, 1),
			(store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
			(lt, ":distance", 25),
			
			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", ":target_village"),
		(try_end),
   (try_end),
   
   (try_for_range, ":faction_1", kingdoms_begin, kingdoms_end),
		(faction_slot_eq, ":faction_1", slot_faction_state, sfs_active),
		(try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
			(neq, ":faction_1", ":faction_2"),
			(faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),
			
			#remove provocations
			(store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":slot_truce_days", kingdoms_begin),
			(faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
			(try_begin),
				(ge, ":truce_days", 1),
				(try_begin),
					(eq, ":truce_days", 1),
					(call_script, "script_update_faction_notes", ":faction_1"),
					(lt, ":faction_1", ":faction_2"),
					(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":faction_1", ":faction_2"),
				(try_end),
				(val_sub, ":truce_days", 1),
				(faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
			(try_end),
		
			(store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
			(val_sub, ":slot_provocation_days", kingdoms_begin),
			(faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
			(try_begin),
				(ge, ":provocation_days", 1),
				(try_begin),#factions already at war
					(store_relation, ":relation", ":faction_1", ":faction_2"),
					(lt, ":relation", 0),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
				(else_try), #Provocation expires
					(eq, ":provocation_days", 1),
					(call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", ":faction_1", ":faction_2"),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
				(else_try),
					(val_sub, ":provocation_days", 1), 
					(faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
				(try_end),
			(try_end),

			(try_begin), #at war
				(store_relation, ":relation", ":faction_1", ":faction_2"),
				(lt, ":relation", 0),
				(store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
				(val_sub, ":slot_war_damage", kingdoms_begin),
				(faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
				(val_add, ":war_damage", 1),
				(faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
			(try_end),	
			
		(try_end),
		(call_script, "script_update_faction_notes", ":faction_1"),
	(try_end),
    ]),
		
  # Give some xp to hero parties
   (48,
   [      
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),	     	     
	              
         (troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
         (gt, ":hero_party", centers_end),
         (party_is_active, ":hero_party"),
         
         (store_skill_level, ":trainer_level", skl_trainer, ":troop_no"),                  
         (val_add, ":trainer_level", 5), #average trainer level is 3 for npc lords, worst : 0, best : 6
         (store_mul, ":xp_gain", ":trainer_level", 1000), #xp gain in two days of period for each lord, average : 8000.
         
         (assign, ":max_accepted_random_value", 30),
         (try_begin),               
           (store_troop_faction, ":cur_troop_faction", ":troop_no"),
           (neq, ":cur_troop_faction", "$players_kingdom"),
           
           (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),
         
         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),

         (party_upgrade_with_xp, ":hero_party", ":xp_gain"),
       (try_end),
       
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),         
         (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
         (neq, ":center_lord", "trp_player"),
         
         (assign, ":xp_gain", 3000), #xp gain in two days of period for each center, average : 3000.
         
         (assign, ":max_accepted_random_value", 30),
         (try_begin),            
           (assign, ":cur_center_lord_faction", -1),
           (try_begin),
             (ge, ":center_lord", 0),
             (store_troop_faction, ":cur_center_lord_faction", ":center_lord"),
           (try_end),             
           (neq, ":cur_center_lord_faction", "$players_kingdom"),
           
           (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),

         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),
         
         (party_upgrade_with_xp, ":center_no", ":xp_gain"),
       (try_end),
    ]),

  # Process sieges
   (24,
   [
       (call_script, "script_process_sieges"),
    ]),

  # Process village raids
   (2,
   [
       (call_script, "script_process_village_raids"),
    ]),


  # Decide vassal ai
   (7,
    [
      (call_script, "script_init_ai_calculation"),
      #(call_script, "script_decide_kingdom_party_ais"),
      (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (call_script, "script_calculate_troop_ai", ":troop_no"),
      (try_end),
      ]),

  # Hold regular marshall elections for players_kingdom
   (24, #Disabled in favor of new system
    [
    #  (val_add, "$g_election_date", 1),
    #  (ge, "$g_election_date", 90), #elections holds once in every 90 days.
    #  (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
    #  (neq, "$players_kingdom", "fac_player_supporters_faction"),
    #  (assign, "$g_presentation_input", -1),
    #  (assign, "$g_presentation_marshall_selection_1_vote", 0),
    #  (assign, "$g_presentation_marshall_selection_2_vote", 0),

    #  (assign, "$g_presentation_marshall_selection_max_renown_1", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_2", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_3", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_1_troop", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_2_troop", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_3_troop", -10000),
    #  (assign, ":num_men", 0),
    #  (try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
    #    (assign, ":cur_troop", ":loop_var"),
    #    (assign, ":continue", 0),
    #    (try_begin),
    #      (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
    #      (assign, ":cur_troop", "trp_player"),
    #      (try_begin),
    #        (eq, "$g_player_is_captive", 0),
    #        (assign, ":continue", 1),
    #      (try_end),
    #    (else_try),
#		  (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
 #         (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
 #         (eq, "$players_kingdom", ":cur_troop_faction"),
  #        #(troop_slot_eq, ":cur_troop", slot_troop_is_prisoner, 0),
  #        (neg|troop_slot_ge, ":cur_troop", slot_troop_prisoner_of_party, 0),
   #       (troop_slot_ge, ":cur_troop", slot_troop_leaded_party, 1),
    #      (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
    #      (neg|faction_slot_eq, ":cur_troop_faction", slot_faction_leader, ":cur_troop"),
    #      (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
    #      (gt, ":cur_party", 0),
    #      (party_is_active, ":cur_party"),
    #      (call_script, "script_party_count_fit_for_battle", ":cur_party"),
    #      (assign, ":party_fit_for_battle", reg0),
    #      (call_script, "script_party_get_ideal_size", ":cur_party"),
    #      (assign, ":ideal_size", reg0),
    #      (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
    #      (val_div, ":relative_strength", ":ideal_size"),
    #      (ge, ":relative_strength", 25),
    #      (assign, ":continue", 1),
    #    (try_end),
    #    (eq, ":continue", 1),
    #    (val_add, ":num_men", 1),
    #    (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
    #    (try_begin),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_1"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_1"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_1", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_1_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_1_troop", ":cur_troop"),
    #    (else_try),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", ":cur_troop"),
    #    (else_try),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_3"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", ":cur_troop"),
    #    (try_end),
    #  (try_end),
    #  (ge, "$g_presentation_marshall_selection_max_renown_1_troop", 0),
    #  (ge, "$g_presentation_marshall_selection_max_renown_2_troop", 0),
    #  (ge, "$g_presentation_marshall_selection_max_renown_3_troop", 0),
    #  (gt, ":num_men", 2), #at least 1 voter
    #  (assign, "$g_election_date", 0),
    #  (assign, "$g_presentation_marshall_selection_ended", 0),
    #  (try_begin),
    #    (neq, "$g_presentation_marshall_selection_max_renown_1_troop", "trp_player"),
    #    (neq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
    #    (start_presentation, "prsnt_marshall_selection"),
    #  (else_try),
    #    (jump_to_menu, "mnu_marshall_selection_candidate_ask"),
    #  (try_end),
      ]),#

   (24,
    [	  
	(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":impatience", ":kingdom_hero", slot_troop_intrigue_impatience),
		(val_sub, ":impatience", 5),
		(val_max, ":impatience", 0),
		(troop_set_slot, ":kingdom_hero", slot_troop_intrigue_impatience, ":impatience"),
	(try_end),
	
	(store_random_in_range, ":controversy_deduction", 1, 3),
	(val_min, ":controversy_deduction", 2),
#	(assign, ":controversy_deduction", 1),
	
	#This reduces controversy by one each round
	(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":controversy", ":active_npc", slot_troop_controversy),
		(ge, ":controversy", 1),
		(val_sub, ":controversy", ":controversy_deduction"),
		(val_max, ":controversy", 0),
		(troop_set_slot, ":active_npc", slot_troop_controversy, ":controversy"),
	(try_end),
	
	(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
	(val_sub, ":controversy", ":controversy_deduction"),
	(val_max, ":controversy", 0),
	(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
	
	]),
		
    #POLITICAL TRIGGERS
	#POLITICAL TRIGGER #1`
   (8, #increased from 12
    [	  
	(call_script, "script_cf_random_political_event"),
	
	#Added Nov 2010 begins - do this twice
	(call_script, "script_cf_random_political_event"),
	#Added Nov 2010 ends
	
	#This generates quarrels and occasional reconciliations and interventions	
	]),
	
    #Individual lord political calculations
    #Check for lords without fiefs, auto-defections, etc
    (0.5,	
     [
        (val_add, "$g_lord_long_term_count", 1),
        (try_begin),
          (neg|is_between, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
          (assign, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin"),
        (try_end),

        (assign, ":troop_no", "$g_lord_long_term_count"),
	
        (try_begin),
          (eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),	
          (assign, ":troop_no", "trp_player"),
        (try_end),

        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_troop_name, s9, ":troop_no"),
          (display_message, "@{!}DEBUG -- Doing political calculations for {s9}"),
        (try_end),
	
        #Penalty for no fief
        (try_begin),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neq, ":troop_no", "trp_player"),
		  
          (assign, ":fief_found", -1),
          (try_for_range, ":center", centers_begin, centers_end),
            (party_slot_eq, ":center", slot_town_lord, ":troop_no"),
            (assign, ":fief_found", ":center"),
          (try_end),
		
          (try_begin),
            (eq, ":fief_found", -1),
                        			
            (store_faction_of_troop, ":original_faction", ":troop_no"),
            (faction_get_slot, ":faction_leader", ":original_faction", slot_faction_leader),
            (troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
			
            (try_begin),
              (neq, ":faction_leader", ":troop_no"),
              (try_begin),
                (this_or_next|eq, ":troop_reputation", lrep_quarrelsome),
                (this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
                (this_or_next|eq, ":troop_reputation", lrep_cunning),
                (eq, ":troop_reputation", lrep_debauched),
                (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -4),
                (val_add, "$total_no_fief_changes", -4),
              (else_try),
                (eq, ":troop_reputation", lrep_martial),
                (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -2),
                (val_add, "$total_no_fief_changes", -2),
              (try_end),
            (try_end),
          (try_end),
        (try_end),	
		
        #Auto-indictment or defection
        (try_begin),
          (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (eq, ":troop_no", "trp_player"),		
          (try_begin),
            (eq, ":troop_no", "trp_player"),
            (assign, ":faction", "$players_kingdom"),
          (else_try),
            (store_faction_of_troop, ":faction", ":troop_no"),
          (try_end),

          (faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
          (neq, ":troop_no", ":faction_leader"),
			
          #I don't know why these are necessary, but they appear to be
          (neg|is_between, ":troop_no", "trp_kingdom_1_lord", "trp_knight_1_1"),
          (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
		  
		  (assign, ":num_centers", 0),		  
		  (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),		    
		    (store_faction_of_party, ":faction_of_center", ":cur_center"),
			(eq, ":faction_of_center", ":faction"),			
			(val_add, ":num_centers", 1),
		  (try_end),

		  #we are counting num_centers to allow defection although there is high relation between faction leader and troop. 
		  #but this rule should not applied for player's faction and player_supporters_faction so thats why here 1 is added to num_centers in that case.
		  (try_begin), 
		    (this_or_next|eq, ":faction", "$players_kingdom"),
			(eq, ":faction", "fac_player_supporters_faction"),
			(val_add, ":num_centers", 1),
		  (try_end),
			
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
          (this_or_next|le, reg0, -50), #was -75
		  (eq, ":num_centers", 0), #if there is no walled centers that faction has defection happens 100%.

          (call_script, "script_cf_troop_can_intrigue", ":troop_no", 0), #Should include battle, prisoner, in a castle with others 
          (store_random_in_range, ":who_moves_first", 0, 2),
			
          (try_begin),
            (this_or_next|eq, ":num_centers", 0), #Thanks Caba`drin & Osviux
            (neq, ":who_moves_first", 0),
            (neq, ":troop_no", "trp_player"),
				
                        #do a defection
                        (try_begin), 
                          (neq, ":num_centers", 0), 
                          (assign, "$g_give_advantage_to_original_faction", 1), 
                        (try_end),
			#(assign, "$g_give_advantage_to_original_faction", 1),
        
			(store_faction_of_troop, ":orig_faction", ":troop_no"),
			(call_script, "script_lord_find_alternative_faction", ":troop_no"),
			(assign, ":new_faction", reg0),			
			(assign, "$g_give_advantage_to_original_faction", 0),
			(try_begin),
			  (neq, ":new_faction", ":orig_faction"),			  
            
              (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
              (str_store_troop_name_link, s1, ":troop_no"),
              (str_store_faction_name_link, s2, ":new_faction"),	
              (str_store_faction_name_link, s3, ":faction"),
              (call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
              (try_begin),
                (ge, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":troop_no"),
                (display_message, "@{!}DEBUG - {s4} faction changed in defection"), 
              (try_end),	
              (troop_get_type, reg4, ":troop_no"),
              (str_store_string, s4, "str_lord_defects_ordinary"),
              (display_log_message, "@{!}{s4}"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (this_or_next|eq, ":new_faction", "$players_kingdom"),
                (eq, ":faction", "$players_kingdom"),
                (call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":troop_no", ":faction"),
              (try_end),				
			(try_end),
          (else_try),	
            (neq, ":faction_leader", "trp_player"),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			(le, reg0, -50), #was -75
            (call_script, "script_indict_lord_for_treason", ":troop_no", ":faction"),
          (try_end),		  
        (else_try),  #Take a stand on an issue
          (neq, ":troop_no", "trp_player"),
          (store_faction_of_troop, ":faction", ":troop_no"),
          (faction_slot_ge, ":faction", slot_faction_political_issue, 1),
          #This bit of complication is needed for savegame compatibility -- if zero is in the slot, they'll choose anyway			
          (neg|troop_slot_ge, ":troop_no", slot_troop_stance_on_faction_issue, 1), 
          (this_or_next|troop_slot_eq, ":troop_no", slot_troop_stance_on_faction_issue, -1),
          (neq, "$players_kingdom", ":faction"),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (call_script, "script_npc_decision_checklist_take_stand_on_issue", ":troop_no"),
          (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, reg0),
        (try_end),

        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
          (lt, reg0, 0),
          (assign, ":relation", reg0),
          (store_sub, ":chance_of_convergence", 0, ":relation"),
          (store_random_in_range, ":random", 0, 300),
          (lt, ":random", ":chance_of_convergence"),
          (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
          (val_add, "$total_relation_changes_through_convergence", 1),
        (try_end),				
        ]),
	
#TEMPORARILY DISABLED, AS READINESS IS NOW A PRODUCT OF NPC_DECISION_CHECKLIST	
  # Changing readiness to join army
#   (10,
 #   [
 #     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#		(eq, 1, 0),
#	    (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#        (assign, ":modifier", 1),
#        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
#        (try_begin),
#          (gt, ":party_no", 0),
#          (party_get_slot, ":commander_party", ":party_no", slot_party_commander_party),
#          (ge, ":commander_party", 0),
#          (store_faction_of_party, ":faction_no", ":party_no"),
#          (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
#          (ge, ":faction_marshall", 0),
#          (troop_get_slot, ":marshall_party", ":faction_marshall", slot_troop_leaded_party),
#          (eq, ":commander_party", ":marshall_party"),
#          (assign, ":modifier", -1),
#        (try_end),
#        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_join_army),
#        (val_add, ":readiness", ":modifier"),
#        (val_clamp, ":readiness", 0, 100),
#        (troop_set_slot, ":troop_no", slot_troop_readiness_to_join_army, ":readiness"),
#        (assign, ":modifier", 1),
#        (try_begin),
#          (gt, ":party_no", 0),
#          (store_troop_faction, ":troop_faction", ":troop_no"),
#          (eq, ":troop_faction", "fac_player_supporters_faction"),
#          (neg|troop_slot_eq, ":troop_no", slot_troop_player_order_state, spai_undefined),
#          (party_get_slot, ":party_ai_state", ":party_no", slot_party_ai_state),
#          (party_get_slot, ":party_ai_object", ":party_no", slot_party_ai_object),
#          #Check if party is following player orders
#          (try_begin),
#            (troop_slot_eq, ":troop_no", slot_troop_player_order_state, ":party_ai_state"),
#            (troop_slot_eq, ":troop_no", slot_troop_player_order_object, ":party_ai_object"),
#            (assign, ":modifier", -1),
#          (else_try),
#            #Leaving following player orders if the current party order is not the same.
#            (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
#            (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
#          (try_end),
#        (try_end),
#        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_follow_orders),
#        (val_add, ":readiness", ":modifier"),
#        (val_clamp, ":readiness", 0, 100),
#        (troop_set_slot, ":troop_no", slot_troop_readiness_to_follow_orders, ":readiness"),
#        (try_begin),
#          (lt, ":readiness", 10),
#          (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
#          (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
#        (try_end),
#      (try_end),
 #     ]),
  
  # Process vassal ai
   (2,
   [
     #(call_script, "script_process_kingdom_parties_ai"), #moved to below trigger (per 1 hour) in order to allow it processed more frequent.
   ]),

  # Process alarms - perhaps break this down into several groups, with a modula
   (1, #this now calls 1/3 of all centers each time, thus hopefully lightening the CPU load
   [
     (call_script, "script_process_alarms"),

     (call_script, "script_allow_vassals_to_join_indoor_battle"),
     
     (call_script, "script_process_kingdom_parties_ai"),
   ]),

  # Process siege ai
   (3,
   [
      (store_current_hours, ":cur_hours"),
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
        (gt, ":besieger_party", 0),
        (party_is_active, ":besieger_party"),
        (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1),
        (party_get_slot, ":siege_begin_hours", ":center_no", slot_center_siege_begin_hours),
        (store_sub, ":siege_begin_hours", ":cur_hours", ":siege_begin_hours"),
        (assign, ":launch_attack", 0),
        (assign, ":call_attack_back", 0),
        (assign, ":attacker_strength", 0),
        (assign, ":marshall_attacking", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),
		  
          (store_troop_faction, ":troop_faction_no", ":troop_no"),
          (eq, ":troop_faction_no", ":besieger_faction"),
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_battle_opponent, ":opponent", ":party_no"),
          (this_or_next|lt, ":opponent", 0),
          (eq, ":opponent", ":center_no"),
          (try_begin),
            (faction_slot_eq, ":besieger_faction", slot_faction_marshall, ":troop_no"),
            (assign, ":marshall_attacking", 1),
          (try_end),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
          (val_add, ":attacker_strength", reg0),
        (try_end),
        (try_begin),
          (gt, ":attacker_strength", 0),
          (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"),
          (call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
          (assign, ":defender_strength", reg0),
          (try_begin),
            (eq, "$auto_enter_town", ":center_no"),
            (eq, "$g_player_is_captive", 0),
            (call_script, "script_party_calculate_regular_strength", "p_main_party"),
            (val_add, ":defender_strength", reg0),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
          (val_add, ":siege_hardness", 100),
          (val_mul, ":defender_strength", ":siege_hardness"),
          (val_div, ":defender_strength", 100),
          (val_max, ":defender_strength", 1),
          (try_begin),
            (eq, ":marshall_attacking", 1),
            (eq, ":besieger_faction", "$players_kingdom"),
            (check_quest_active, "qst_follow_army"),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (store_mul, ":strength_ratio", ":attacker_strength", 100),
          (val_div, ":strength_ratio", ":defender_strength"),
          (store_sub, ":random_up_limit", ":strength_ratio", 250), #was 300 (1.126)
                    
          (try_begin),
            (gt, ":random_up_limit", -100), #never attack if the strength ratio is less than 150%
            (store_div, ":siege_begin_hours_effect", ":siege_begin_hours", 2), #was 3 (1.126)
            (val_add, ":random_up_limit", ":siege_begin_hours_effect"),
          (try_end),

          (val_div, ":random_up_limit", 5),
          (val_max, ":random_up_limit", 0),
          (store_sub, ":random_down_limit", 175, ":strength_ratio"), #was 200 (1.126)
          (val_max, ":random_down_limit", 0),
          (try_begin),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_up_limit"),
            (gt, ":siege_begin_hours", 24),#initial preparation
            (assign, ":launch_attack", 1),
          (else_try),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_down_limit"),            
            (assign, ":call_attack_back", 1),
          (try_end),
        (else_try),
          (assign, ":call_attack_back", 1),
        (try_end),

        #Assault the fortress
        (try_begin),
          (eq, ":launch_attack", 1),
          (call_script, "script_begin_assault_on_center", ":center_no"),
        (else_try),
          (eq, ":call_attack_back", 1),
          (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),
			
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            #resetting siege begin time if at least 1 party retreats
            (party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
          (try_end),
        (try_end),
      (try_end),
    ]),

    # Decide faction ais
    (6, #it was 23
    [
      (assign, "$g_recalculate_ais", 1),
    ]),
	
    
  # Decide faction ai flag check
   (0,
   [
   

    (try_begin),
		(ge, "$cheat_mode", 1),
	
		(try_for_range, ":king", "trp_kingdom_1_lord", "trp_knight_1_1"),		
			(store_add, ":proper_faction", ":king", "fac_kingdom_1"),
			(val_sub, ":proper_faction", "trp_kingdom_1_lord"),
			(store_faction_of_troop, ":actual_faction", ":king"),
			
			(neq, ":proper_faction", ":actual_faction"),
			(neq, ":actual_faction", "fac_commoners"),
			(ge, "$cheat_mode", 2),
			(neq, ":king", "trp_kingdom_2_lord"),
			
			(str_store_troop_name, s4, ":king"),
			(str_store_faction_name, s5, ":actual_faction"),
			(str_store_faction_name, s6, ":proper_faction"),
			(str_store_string, s65, "@{!}DEBUG - {s4} is in {s5}, should be in {s6}, disabling political cheat mode"),
#			(display_message, "@{s65}"),
			(rest_for_hours, 0, 0, 0),
			
			#(assign, "$cheat_mode", 1),
			(jump_to_menu, "mnu_debug_alert_from_s65"),
		(try_end),
	
	
	(try_end),
   
     (eq, "$g_recalculate_ais", 1),
     (assign, "$g_recalculate_ais", 0),
     (call_script, "script_recalculate_ais"),
   ]),
	
    # Count faction armies
    (24,
    [
       (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
         (call_script, "script_faction_recalculate_strength", ":faction_no"),
       (try_end),
	   
	   (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
		(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
		(neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_default),
		(neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_feast),
		(neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_gathering_army),
		
		(troop_get_slot, ":active_npc_party", ":active_npc", slot_troop_leaded_party),
		(party_is_active, ":active_npc_party"),
		
		(val_add, "$total_vassal_days_on_campaign", 1),
		
	    (party_slot_eq, ":active_npc_party", slot_party_ai_state, spai_accompanying_army),
		(val_add, "$total_vassal_days_responding_to_campaign", 1),
		
	   
	   (try_end),
	   
    ]),

  # Reset hero quest status
  # Change hero relation
   (36,
   [
     (try_for_range, ":troop_no", heroes_begin, heroes_end),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
     (try_end),
     
     (try_for_range, ":troop_no", village_elders_begin, village_elders_end),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
     (try_end),
    ]),

  # Refresh merchant inventories
   (168,
   [
      (try_for_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
      (try_end),
    ]),

  #Refreshing village defenders
  #Clearing slot_village_player_can_not_steal_cattle flags
   (48,
   [
      (try_for_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_refresh_village_defenders", ":village_no"),
        (party_set_slot, ":village_no", slot_village_player_can_not_steal_cattle, 0),
      (try_end),
    ]),

  # Refresh number of cattle in villages
  (24 * 7,
   [
     (try_for_range, ":village_no", centers_begin, centers_end),
	   (neg|is_between, ":village_no", castles_begin, castles_end),
	   (party_get_slot, ":num_cattle", ":village_no", slot_center_head_cattle),
	   (party_get_slot, ":num_sheep", ":village_no", slot_center_head_sheep),
	   (party_get_slot, ":num_acres", ":village_no", slot_center_acres_pasture),
	   (val_max, ":num_acres", 1),
	   
	   (store_mul, ":grazing_capacity", ":num_cattle", 400),
	   (store_mul, ":sheep_addition", ":num_sheep", 200),
	   (val_add, ":grazing_capacity", ":sheep_addition"),
	   (val_div, ":grazing_capacity", ":num_acres"),
	   
	   (store_random_in_range, ":random_no", 0, 100),
	   (try_begin), #Disaster
	     (eq, ":random_no", 0),#1% chance of epidemic - should happen once every two years
		 (val_min, ":num_cattle", 10),
		 
       (else_try), #Overgrazing
         (gt, ":grazing_capacity", 100),
		
         (val_mul, ":num_sheep", 90), #10% decrease at number of cattles
         (val_div, ":num_sheep", 100),
		
         (val_mul, ":num_cattle", 90), #10% decrease at number of sheeps
         (val_div, ":num_cattle", 100),
		 
       (else_try), #superb grazing
         (lt, ":grazing_capacity", 30),

         (val_mul, ":num_cattle", 120), #20% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (val_add, ":num_cattle", 1),
		
         (val_mul, ":num_sheep", 120), #20% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (val_add, ":num_sheep", 1),
		
       (else_try), #very good grazing
         (lt, ":grazing_capacity", 60),

         (val_mul, ":num_cattle", 110), #10% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (val_add, ":num_cattle", 1),
		
         (val_mul, ":num_sheep", 110), #10% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (val_add, ":num_sheep", 1),

       (else_try), #good grazing
         (lt, ":grazing_capacity", 100),
         (lt, ":random_no", 50),

         (val_mul, ":num_cattle", 105), #5% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (try_begin), #if very low number of cattles and there is good grazing then increase number of cattles also by one
           (le, ":num_cattle", 20),
           (val_add, ":num_cattle", 1),
         (try_end),
		
         (val_mul, ":num_sheep", 105), #5% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (try_begin), #if very low number of sheeps and there is good grazing then increase number of sheeps also by one
           (le, ":num_sheep", 20),
           (val_add, ":num_sheep", 1),
         (try_end),		
       (try_end),

       (party_set_slot, ":village_no", slot_center_head_cattle, ":num_cattle"),
       (party_set_slot, ":village_no", slot_center_head_sheep, ":num_sheep"),	  	  	  
     (try_end),
    ]),

   #Accumulate taxes
   (24 * 7,
   [
      #Adding earnings to town lords' wealths.
      #Moved to troop does business
      #(try_for_range, ":center_no", centers_begin, centers_end),
      #  (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
      #  (neq, ":town_lord", "trp_player"),
      #  (is_between, ":town_lord", active_npcs_begin, active_npcs_end),
      #  (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
      #  (party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
      #  (troop_get_slot, ":troop_wealth", ":town_lord", slot_troop_wealth),
      #  (val_add, ":troop_wealth", ":accumulated_rents"),
      #  (val_add, ":troop_wealth", ":accumulated_tariffs"),
      #  (troop_set_slot, ":town_lord", slot_troop_wealth, ":troop_wealth"),				
      #  (party_set_slot, ":center_no", slot_center_accumulated_rents, 0),
      #  (party_set_slot, ":center_no", slot_center_accumulated_tariffs, 0),
      #  (try_begin),
      #    (eq, "$cheat_mode", 1),
      #    (assign, reg1, ":troop_wealth"),
      #    (add_troop_note_from_sreg, ":town_lord", 1, "str_current_wealth_reg1", 0),
      #  (try_end),
      #(try_end),
            
	  #Collect taxes for another week
      (try_for_range, ":center_no", centers_begin, centers_end),
        (try_begin),
          (party_slot_ge, ":center_no", slot_town_lord, 0), #unassigned centers do not accumulate rents	  
        
          (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),		  
		
          (assign, ":cur_rents", 0),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_village),
            (try_begin),
              (party_slot_eq, ":center_no", slot_village_state, svs_normal),
              (assign, ":cur_rents", 1200),
            (try_end),
          (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (assign, ":cur_rents", 1200),
          (else_try),  
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":cur_rents", 2400),
          (try_end),
		
          (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity), #prosperty changes between 0..100     
          (store_add, ":multiplier", 20, ":prosperity"), #multiplier changes between 20..120
          (val_mul, ":cur_rents", ":multiplier"), 
          (val_div, ":cur_rents", 120),#Prosperity of 100 gives the default values
          
          (try_begin),
            (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
            
            (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
            (try_begin),
              (eq, ":reduce_campaign_ai", 0), #hard (less money from rents)
              (val_mul, ":cur_rents", 3),
              (val_div, ":cur_rents", 4),
            (else_try),
              (eq, ":reduce_campaign_ai", 1), #medium (normal money from rents)
              #same
            (else_try),
              (eq, ":reduce_campaign_ai", 2), #easy (more money from rents)
              (val_mul, ":cur_rents", 4),
              (val_div, ":cur_rents", 3),
            (try_end),                
          (try_end),  
                    
          (val_add, ":accumulated_rents", ":cur_rents"), #cur rents changes between 23..1000
          (party_set_slot, ":center_no", slot_center_accumulated_rents, ":accumulated_rents"),
        (try_end),
        
		(try_begin),
		  (is_between, ":center_no", villages_begin, villages_end),
		  (party_get_slot, ":bound_castle", ":center_no", slot_village_bound_center),
		  (party_slot_ge, ":bound_castle", slot_town_lord, 0), #unassigned centers do not accumulate rents	  
		  (is_between, ":bound_castle", castles_begin, castles_end),
		  (party_get_slot, ":accumulated_rents", ":bound_castle", slot_center_accumulated_rents), #castle's accumulated rents
		  (val_add, ":accumulated_rents", ":cur_rents"), #add village's rent to castle rents
		  (party_set_slot, ":bound_castle", slot_center_accumulated_rents, ":accumulated_rents"),
		(try_end),		
      (try_end),
    ]),

#   (7 * 24,
#   [
##       (call_script, "script_get_number_of_unclaimed_centers_by_player"),
##       (assign, ":unclaimed_centers", reg0),
##       (gt, ":unclaimed_centers", 0),
# You are holding an estate without a lord.        
#       (try_for_range, ":troop_no", heroes_begin, heroes_end),
#         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#         (troop_get_slot, ":relation", ":troop_no", slot_troop_player_relation),
#         (val_sub, ":relation", 1),
#         (val_max, ":relation", -100),
#         (troop_set_slot, ":troop_no", slot_troop_player_relation, ":relation"),
#       (try_end),
# You relation with all kingdoms other than your own has decreased by 1.     
#       (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
#         (neq, ":faction_no", "$players_kingdom"),
#         (store_relation,":faction_relation",":faction_no","fac_player_supporters_faction"),
#         (val_sub, ":faction_relation", 1),
#         (val_max, ":faction_relation", -100),
#		  WARNING: Never use set_relation!
#         (set_relation, ":faction_no", "fac_player_supporters_faction", ":faction_relation"),
#       (try_end),
#    ]),

  
  # Offer player to join faction
  # Only if the player is male -- female characters will be told that they should seek out a faction through NPCs, possibly
   (32,
   [
     (eq, "$players_kingdom", 0),
     (le, "$g_invite_faction", 0),
     (eq, "$g_player_is_captive", 0),
	 (troop_get_type, ":type", "trp_player"),
	 (try_begin),
		(eq, ":type", 1),
		(eq, "$npc_with_sisterly_advice", 0),
		(try_for_range, ":npc", companions_begin, companions_end),
			(main_party_has_troop, ":npc"),
			(troop_get_type, ":npc_type", ":npc"),
			(eq, ":npc_type", 1),
			(troop_slot_ge, "trp_player", slot_troop_renown, 150),
			(troop_slot_ge, ":npc", slot_troop_woman_to_woman_string, 1),
			(assign, "$npc_with_sisterly_advice", ":npc"),
		(try_end),
	 (else_try),
	     (store_random_in_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
	     (assign, ":min_distance", 999999),
	     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
	       (store_faction_of_party, ":center_faction", ":center_no"),
	       (eq, ":center_faction", ":kingdom_no"),
	       (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center_no"),
	       (val_min, ":min_distance", ":cur_distance"),
	     (try_end),
	     (lt, ":min_distance", 30),
	     (store_relation, ":kingdom_relation", ":kingdom_no", "fac_player_supporters_faction"),
	     (faction_get_slot, ":kingdom_lord", ":kingdom_no", slot_faction_leader),
	     (call_script, "script_troop_get_player_relation", ":kingdom_lord"),
	     (assign, ":lord_relation", reg0),
	     #(troop_get_slot, ":lord_relation", ":kingdom_lord", slot_troop_player_relation),
	     (call_script, "script_get_number_of_hero_centers", "trp_player"),
	     (assign, ":num_centers_owned", reg0),
	     (eq, "$g_infinite_camping", 0),
	     	     
	     (assign, ":player_party_size", 0),	     
	     (try_begin),
	       (ge, "p_main_party", 0),
	       (store_party_size_wo_prisoners, ":player_party_size", "p_main_party"),	     
	     (try_end),  
	     
	     (try_begin),	       
	       (eq, ":num_centers_owned", 0),
	       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
	       (ge, ":player_renown", 160),
	       (ge, ":kingdom_relation", 0),
	       (ge, ":lord_relation", 0),
	       (ge, ":player_party_size", 45),
	       (store_random_in_range, ":rand", 0, 100),
	       (lt, ":rand", 50),
	       (call_script, "script_get_poorest_village_of_faction", ":kingdom_no"),
	       (assign, "$g_invite_offered_center", reg0),
	       (ge, "$g_invite_offered_center", 0),
	       (assign, "$g_invite_faction", ":kingdom_no"),
	       (jump_to_menu, "mnu_invite_player_to_faction"),
	     (else_try),
	       (gt, ":num_centers_owned", 0),
	       (neq, "$players_oath_renounced_against_kingdom", ":kingdom_no"),
	       (ge, ":kingdom_relation", -40),
	       (ge, ":lord_relation", -20),
	       (ge, ":player_party_size", 30),
	       (store_random_in_range, ":rand", 0, 100),
	       (lt, ":rand", 20),
	       (assign, "$g_invite_faction", ":kingdom_no"),
	       (assign, "$g_invite_offered_center", -1),
	       (jump_to_menu, "mnu_invite_player_to_faction_without_center"),
	     (try_end),
	 (try_end), 
    ]),

    #recalculate lord random decision seeds once in every week
	(24 * 7, 
	[
      (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (store_random_in_range, ":random", 0, 9999),
        (troop_set_slot, ":troop_no", slot_troop_temp_decision_seed, ":random"),
      (try_end),   		
	
	#npcs will only change their minds on issues at least 24 hours after speaking to the player
    #(store_current_hours, ":hours"),
    #(try_begin),
    #  (eq, 1, 0), #disabled
    #  (try_for_range, ":npc", active_npcs_begin, active_npcs_end),
    #    (troop_get_slot, ":last_talk", ":npc", slot_troop_last_talk_time),
    #    (val_sub, ":hours", ":last_talk"),
    #    (ge, ":hours", 24),
    #    (store_random_in_range, ":random", 0, 9999),
    #    (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":random"),
    #  (try_end),
    #(try_end),
	]),
		
  # During rebellion, removing troops from player faction randomly because of low relation points
  # Deprecated -- should be part of regular political events


  # Reset kingdom lady current centers
##   (28,
##   [
##       (try_for_range, ":troop_no", heroes_begin, heroes_end),
##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
##
##         # Find the active quest ladies
##         (assign, ":not_ok", 0),
##         (try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
##           (eq, ":not_ok", 0),
##           (check_quest_active, ":quest_no"),
##           (quest_slot_eq, ":quest_no", slot_quest_object_troop, ":troop_no"),
##           (assign, ":not_ok", 1),
##         (try_end),
##         (eq, ":not_ok", 0),
##
##         (troop_get_slot, ":troop_center", ":troop_no", slot_troop_cur_center),
##         (assign, ":is_under_siege", 0),
##         (try_begin),
##           (is_between, ":troop_center", walled_centers_begin, walled_centers_end),
##           (party_get_battle_opponent, ":besieger_party", ":troop_center"),
##           (gt, ":besieger_party", 0),
##           (assign, ":is_under_siege", 1),
##         (try_end),
##
##         (eq, ":is_under_siege", 0),# Omit ladies in centers under siege
##
##         (try_begin),
##           (store_random_in_range, ":random_num",0, 100),
##           (lt, ":random_num", 20),
##           (store_troop_faction, ":cur_faction", ":troop_no"),
##           (call_script, "script_cf_select_random_town_with_faction", ":cur_faction"),#Can fail
##           (troop_set_slot, ":troop_no", slot_troop_cur_center, reg0),
##         (try_end),
##       
##         (store_random_in_range, ":random_num",0, 100),
##         (lt, ":random_num", 50),
##         (troop_get_slot, ":lord_no", ":troop_no", slot_troop_father),
##         (try_begin),
##           (eq, ":lord_no", 0),
##           (troop_get_slot, ":lord_no", ":troop_no", slot_troop_spouse),
##         (try_end),
##         (gt, ":lord_no", 0),
##         (troop_get_slot, ":cur_party", ":lord_no", slot_troop_leaded_party),
##         (gt, ":cur_party", 0),
##         (party_get_attached_to, ":cur_center", ":cur_party"),
##         (gt, ":cur_center", 0),
##
##         (troop_set_slot, ":troop_no", slot_troop_cur_center, ":cur_center"),
##       (try_end),
##    ]),


  # Attach Lord Parties to the town they are in
  (0.1,
   [
       (try_for_range, ":troop_no", heroes_begin, heroes_end),
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_slot, ":troop_party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":troop_party_no", 1),
		 (party_is_active, ":troop_party_no"),
		 
         (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
         (lt, ":cur_attached_town", 1),
         (party_get_cur_town, ":destination", ":troop_party_no"),
         (is_between, ":destination", centers_begin, centers_end),
         (call_script, "script_get_relation_between_parties", ":destination", ":troop_party_no"),
         (try_begin),
           (ge, reg0, 0),
           (party_attach_to_party, ":troop_party_no", ":destination"),
         (else_try),
           (party_set_ai_behavior, ":troop_party_no", ai_bhvr_hold),
         (try_end),
         
         (try_begin),
           (this_or_next|party_slot_eq, ":destination", slot_party_type, spt_town),
           (party_slot_eq, ":destination", slot_party_type, spt_castle),
           (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
           (store_faction_of_party, ":destination_faction_no", ":destination"),
           (eq, ":troop_faction_no", ":destination_faction_no"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
           (gt, ":num_stacks", 0),
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),#Moving prisoners to the center
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
         (try_end),
       (try_end),
	   	   
	   (try_for_parties, ":bandit_camp"),
	 	 (gt, ":bandit_camp", "p_spawn_points_end"),
		 #Can't have party is active here, because it will fail for inactive parties
		 (party_get_template_id, ":template", ":bandit_camp"),
		 (ge, ":template", "pt_steppe_bandit_lair"),
		
		 (store_distance_to_party_from_party, ":distance", "p_main_party", ":bandit_camp"),
	     (lt, ":distance", 3), 
	     (party_set_flags, ":bandit_camp", pf_disabled, 0),
	     (party_set_flags, ":bandit_camp", pf_always_visible, 1),	   
	   (try_end),
    ]),

  # Check escape chances of hero prisoners.
  (48,
   [
       (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", 50),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
##         (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
         (assign, ":chance", 30),
         (try_begin),
           (party_slot_eq, ":center_no", slot_center_has_prisoner_tower, 1),
           (assign, ":chance", 5),
         (try_end),
         (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":center_no", ":chance"),
       (try_end),
    ]),

  # Asking the ownership of captured centers to the player
#  (3,
#   [
#    (assign, "$g_center_taken_by_player_faction", -1),
#    (try_for_range, ":center_no", centers_begin, centers_end),
#      (eq, "$g_center_taken_by_player_faction", -1),
#      (store_faction_of_party, ":center_faction", ":center_no"),
#      (eq, ":center_faction", "fac_player_supporters_faction"),
#      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
#      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_unassigned),
#      (party_slot_eq, ":center_no", slot_town_lord, stl_rejected_by_player),
#      (assign, "$g_center_taken_by_player_faction", ":center_no"),
#    (try_end),
#    (faction_get_slot, ":leader", "fac_player_supporters_faction", slot_faction_leader),

#	(try_begin),
#		(ge, "$g_center_taken_by_player_faction", 0),
		
#		(eq, "$cheat_mode", 1),
#		(str_store_party_name, s14, "$g_center_taken_by_player_faction"),
#		(display_message, "@{!}{s14} should be assigned to lord"),
#	(try_end),
	
#    ]),


  # Respawn hero party after kingdom hero is released from captivity.
  (48, 
   [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

         (str_store_troop_name, s1, ":troop_no"),
       
         (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),

         (store_troop_faction, ":cur_faction", ":troop_no"),
         (try_begin),
           (eq, ":cur_faction", "fac_outlaws"), #Do nothing
         (else_try),         
           (try_begin),
             (eq, "$cheat_mode", 2),
             (str_store_troop_name, s4, ":troop_no"),
             (display_message, "str_debug__attempting_to_spawn_s4"),
           (try_end),
           
           (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", ":troop_no"),#Can fail
           (assign, ":center_no", reg0),

           (try_begin),
             (eq, "$cheat_mode", 2),             
             (str_store_party_name, s7, ":center_no"),
			 (str_store_troop_name, s0, ":troop_no"),
             (display_message, "str_debug__s0_is_spawning_around_party__s7"),
           (try_end),
       
           (call_script, "script_create_kingdom_hero_party", ":troop_no", ":center_no"),

		   (try_begin),
		     (eq, "$g_there_is_no_avaliable_centers", 0),
             (party_attach_to_party, "$pout_party", ":center_no"),
           (try_end),
           
           #new
           #(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
		   #(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties		
		   #(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
		   #new end

           (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
           (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),           
           
         (else_try),
           (neg|faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (try_begin),
             (is_between, ":troop_no", kings_begin, kings_end),
             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_commoners"),
           (else_try),
             (store_random_in_range, ":random_no", 0, 100),
             (lt, ":random_no", 10),
             (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":cur_faction"),
             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, reg0),
           (try_end),
         (try_end),
       (try_end),
    ]),

  # Spawn merchant caravan parties
##  (3,
##   [
##       (try_for_range, ":troop_no", merchants_begin, merchants_end),
##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_merchant),
##         (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
##
##         (call_script, "script_cf_create_merchant_party", ":troop_no"),
##       (try_end),
##    ]),

  # Spawn village farmer parties
  (24,
   [
       (try_for_range, ":village_no", villages_begin, villages_end),
         (party_slot_eq, ":village_no", slot_village_state, svs_normal),
         (party_get_slot, ":farmer_party", ":village_no", slot_village_farmer_party),
         (this_or_next|eq, ":farmer_party", 0),
         (neg|party_is_active, ":farmer_party"),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 60),
         (call_script, "script_create_village_farmer_party", ":village_no"),
         (party_set_slot, ":village_no", slot_village_farmer_party, reg0),
#         (str_store_party_name, s1, ":village_no"),
#         (display_message, "@Village farmers created at {s1}."),
       (try_end),
    ]),

  
   (72,
   [
  # Updating trade good prices according to the productions
       (call_script, "script_update_trade_good_prices"),
 # Updating player odds
       (try_for_range, ":cur_center", centers_begin, centers_end),
         (party_get_slot, ":player_odds", ":cur_center", slot_town_player_odds),
         (try_begin),
           (gt, ":player_odds", 1000),
           (val_mul, ":player_odds", 95),
           (val_div, ":player_odds", 100),
           (val_max, ":player_odds", 1000),
         (else_try),
           (lt, ":player_odds", 1000),
           (val_mul, ":player_odds", 105),
           (val_div, ":player_odds", 100),
           (val_min, ":player_odds", 1000),
         (try_end),
         (party_set_slot, ":cur_center", slot_town_player_odds, ":player_odds"),
       (try_end),
    ]),


  #Troop AI: Merchants thinking
  (8,
   [
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
         (party_is_in_any_town, ":party_no"),

         (store_faction_of_party, ":merchant_faction", ":party_no"),
         (faction_get_slot, ":num_towns", ":merchant_faction", slot_faction_num_towns),
         (try_begin),
           (le, ":num_towns", 0),
           (remove_party, ":party_no"),
         (else_try),
           (party_get_cur_town, ":cur_center", ":party_no"),
           
           (store_random_in_range, ":random_no", 0, 100),                               
           
           (try_begin),
             (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
             
             (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
             (try_begin),
               (eq, ":reduce_campaign_ai", 0), #hard (less money from tariffs)
               (assign, ":tariff_succeed_limit", 35),
             (else_try),
               (eq, ":reduce_campaign_ai", 1), #medium (normal money from tariffs)
               (assign, ":tariff_succeed_limit", 45),
             (else_try),
               (eq, ":reduce_campaign_ai", 2), #easy (more money from tariffs)
               (assign, ":tariff_succeed_limit", 60),
             (try_end),                
           (else_try),  
             (assign, ":tariff_succeed_limit", 45),
           (try_end),
                      
           (lt, ":random_no", ":tariff_succeed_limit"),                  

           (assign, ":can_leave", 1),
           (try_begin),
             (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
             (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
             (assign, ":can_leave", 0),
           (try_end),
           (eq, ":can_leave", 1),

           (assign, ":do_trade", 0),
           (try_begin),
             (party_get_slot, ":cur_ai_state", ":party_no", slot_party_ai_state),
             (eq, ":cur_ai_state", spai_trading_with_town),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),
             (assign, ":do_trade", 1),
           (try_end),

           (assign, ":target_center", -1),
           
           (try_begin), #Make sure escorted caravan continues to its original destination.
             (eq, "$caravan_escort_party_id", ":party_no"),
             (neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
             (assign, ":target_center", "$caravan_escort_destination_town"),
           (else_try),         
             (call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction"),
             (assign, ":target_center", reg0),
           (try_end),
           (is_between, ":target_center", towns_begin, towns_end),
           (neg|party_is_in_town, ":party_no", ":target_center"),
       
           (try_begin),
             (eq, ":do_trade", 1),
             (str_store_party_name, s7, ":cur_center"),             
             (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
           (try_end),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":target_center"),
           (party_set_flags, ":party_no", pf_default_behavior, 0),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
         (try_end),
       (try_end),
    ]),

  #Troop AI: Village farmers thinking
  (8,
   [
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_village_farmer),
         (party_is_in_any_town, ":party_no"),
         (party_get_slot, ":home_center", ":party_no", slot_party_home_center),
         (party_get_cur_town, ":cur_center", ":party_no"),

         (assign, ":can_leave", 1),
         (try_begin),
           (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
           (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
           (assign, ":can_leave", 0),
         (try_end),
         (eq, ":can_leave", 1),

         (try_begin),
           (eq, ":cur_center", ":home_center"),
		   
		   #Peasants trade in their home center
		   (call_script, "script_do_party_center_trade", ":party_no", ":home_center", 3), #this needs to be the same as the center		   
		   (store_faction_of_party, ":center_faction", ":cur_center"),
           (party_set_faction, ":party_no", ":center_faction"),           		   
           (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":market_town"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":market_town"),
         (else_try),
           (try_begin),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),

             (call_script, "script_do_party_center_trade", ":party_no", ":cur_ai_object", 3), #raised from 10
             (assign, ":total_change", reg0),
		     #This is roughly 50% of what a caravan would pay
			 
             #Adding tariffs to the town
             (party_get_slot, ":accumulated_tariffs", ":cur_ai_object", slot_center_accumulated_tariffs),
             (party_get_slot, ":prosperity", ":cur_ai_object", slot_town_prosperity),
			 
			 (assign, ":tariffs_generated", ":total_change"),
			 (val_mul, ":tariffs_generated", ":prosperity"),
			 (val_div, ":tariffs_generated", 100),
			 (val_div, ":tariffs_generated", 20), #10 for caravans, 20 for villages
			 (val_add, ":accumulated_tariffs", ":tariffs_generated"),
	  
			 (try_begin),
				(ge, "$cheat_mode", 3),
				(assign, reg4, ":tariffs_generated"),
				(str_store_party_name, s4, ":cur_ai_object"),
				(assign, reg5, ":accumulated_tariffs"),
				(display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
			 (try_end),
			 
             (party_set_slot, ":cur_ai_object", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
			 
             #Increasing food stocks of the town
             (party_get_slot, ":town_food_store", ":cur_ai_object", slot_party_food_store),
             (call_script, "script_center_get_food_store_limit", ":cur_ai_object"),
             (assign, ":food_store_limit", reg0),
             (val_add, ":town_food_store", 1000),
             (val_min, ":town_food_store", ":food_store_limit"),
             (party_set_slot, ":cur_ai_object", slot_party_food_store, ":town_food_store"),

             #Adding 1 to village prosperity
             (try_begin),
               (store_random_in_range, ":rand", 0, 100),
               (lt, ":rand", 5), #was 35
               (call_script, "script_change_center_prosperity", ":home_center", 1),
			   (val_add, "$newglob_total_prosperity_from_village_trade", 1),
             (try_end),
           (try_end),

           #Moving farmers to their home village
           (party_set_slot, ":party_no", slot_party_ai_object, ":home_center"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":home_center"),
         (try_end),
       (try_end),
    ]),

 #Increase castle food stores
  (2,
   [
       (try_for_range, ":center_no", castles_begin, castles_end),
         (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #castle is not under siege
         (party_get_slot, ":center_food_store", ":center_no", slot_party_food_store),
         (val_add, ":center_food_store", 100),
         (call_script, "script_center_get_food_store_limit", ":center_no"),
         (assign, ":food_store_limit", reg0),
         (val_min, ":center_food_store", ":food_store_limit"),
         (party_set_slot, ":center_no", slot_party_food_store, ":center_food_store"),
       (try_end),
    ]),

 #cache party strengths (to avoid re-calculating)
##  (2,
##   [
##       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
##         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
##         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
##         (ge, ":cur_party", 0),
##         (call_script, "script_party_calculate_strength", ":cur_party", 0), #will update slot_party_cached_strength
##       (try_end),
##    ]),
##  
##  (6,
##   [
##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
##         (call_script, "script_party_calculate_strength", ":cur_center", 0), #will update slot_party_cached_strength
##       (try_end),
##    ]),

##  (1,
##   [
##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
##         (store_random_in_range, ":rand", 0, 100),
##         (lt, ":rand", 10),
##         (store_faction_of_party, ":center_faction", ":cur_center"),
##         (assign, ":friend_strength", 0),
##         (try_for_range, ":cur_troop", heroes_begin, heroes_end),
##           (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
##           (troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
##           (gt, ":cur_troop_party", 0),
##           (store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":cur_center"),
##           (lt, ":distance", 10),
##           (store_troop_faction, ":army_faction", ":cur_troop"),
##           (store_relation, ":rel", ":army_faction", ":center_faction"),
##           (try_begin),
##             (gt, ":rel", 10),
##             (party_get_slot, ":str", ":cur_troop_party", slot_party_cached_strength),
##             (val_add, ":friend_strength", ":str"),
##           (try_end),
##         (try_end),
##         (party_set_slot, ":cur_center", slot_party_nearby_friend_strength, ":friend_strength"),
##       (try_end),
##    ]),

  # Make heroes running away from someone retreat to friendly centers
  (0.5,
   [
       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
         (gt, ":cur_party", 0),
         (try_begin),
           (party_is_active, ":cur_party"),
           (try_begin),
             (get_party_ai_current_behavior, ":ai_bhvr", ":cur_party"),
             (eq, ":ai_bhvr", ai_bhvr_avoid_party),
			 
			 #Certain lord personalities will not abandon a battlefield to flee to a fortress
			 (assign, ":continue", 1),
			 (try_begin),
				(this_or_next|troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_upstanding),
					(troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_martial),
				(get_party_ai_current_object, ":ai_object", ":cur_party"),
				(party_is_active, ":ai_object"),
				(party_get_battle_opponent, ":battle_opponent", ":ai_object"),
				(party_is_active, ":battle_opponent"),
				(assign, ":continue", 0),
			 (try_end),
			 (eq, ":continue", 1),
			 
			 
             (store_faction_of_party, ":party_faction", ":cur_party"),
             (party_get_slot, ":commander_party", ":cur_party", slot_party_commander_party),
             (faction_get_slot, ":faction_marshall", ":party_faction", slot_faction_marshall),
             (neq, ":faction_marshall", ":cur_troop"),
             (assign, ":continue", 1),
             (try_begin),
               (ge, ":faction_marshall", 0),
               (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
               (party_is_active, ":faction_marshall_party", 0),
               (eq, ":commander_party", ":faction_marshall_party"),
               (assign, ":continue", 0),
             (try_end),
             (eq, ":continue", 1),
             (assign, ":done", 0),
             (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
               (eq, ":done", 0),
               (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
               (store_faction_of_party, ":center_faction", ":cur_center"),
               (store_relation, ":cur_relation", ":center_faction", ":party_faction"),
               (gt, ":cur_relation", 0),
               (store_distance_to_party_from_party, ":cur_distance", ":cur_party", ":cur_center"),
               (lt, ":cur_distance", 20),
               (party_get_position, pos1, ":cur_party"),
               (party_get_position, pos2, ":cur_center"),
               (neg|position_is_behind_position, pos2, pos1),
               (call_script, "script_party_set_ai_state", ":cur_party", spai_retreating_to_center, ":cur_center"),
               (assign, ":done", 1),
             (try_end),
           (try_end),
         (else_try),
           (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
         (try_end),
       (try_end),
    ]),

  # Centers give alarm if the player is around
  (0.5,
   [
     (store_current_hours, ":cur_hours"),
     (store_mod, ":cur_hours_mod", ":cur_hours", 11),
     (store_sub, ":hour_limit", ":cur_hours", 5),
     (party_get_num_companions, ":num_men", "p_main_party"),
     (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
     (val_add, ":num_men", ":num_prisoners"),
     (convert_to_fixed_point, ":num_men"),
     (store_sqrt, ":num_men_effect", ":num_men"),
     (convert_from_fixed_point, ":num_men_effect"),
     (try_begin),
       (eq, ":cur_hours_mod", 0),
       #Reduce alarm by 2 in every 11 hours.
       (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
         (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
         (val_sub, ":player_alarm", 1),
         (val_max, ":player_alarm", 0),
         (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
       (try_end),
     (try_end),
     (eq, "$g_player_is_captive", 0),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (store_faction_of_party, ":cur_faction", ":cur_center"),
       (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
       (lt, ":reln", 0),
       (store_distance_to_party_from_party, ":dist", "p_main_party", ":cur_center"),
       (lt, ":dist", 5),
       (store_mul, ":dist_sqr", ":dist", ":dist"),
       (store_sub, ":dist_effect", 20, ":dist_sqr"),
       (store_sub, ":reln_effect", 20, ":reln"),
       (store_mul, ":total_effect", ":dist_effect", ":reln_effect"),
       (val_mul, ":total_effect", ":num_men_effect"),
       (store_div, ":spot_chance", ":total_effect", 10),
       (store_random_in_range, ":random_spot", 0, 1000),
       (lt, ":random_spot", ":spot_chance"),
       (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
       (val_add, ":player_alarm", 1),
       (val_min, ":player_alarm", 100),
       (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
       (try_begin),
         (neg|party_slot_ge, ":cur_center", slot_center_last_player_alarm_hour, ":hour_limit"),
         (str_store_party_name_link, s1, ":cur_center"),
         (display_message, "@Your party is spotted by {s1}."),
         (party_set_slot, ":cur_center", slot_center_last_player_alarm_hour, ":cur_hours"),
       (try_end),
     (try_end),
    ]),
  
  # Consuming food at every 14 hours
  (14,
   [
    (eq, "$g_player_is_captive", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
    (val_div, ":num_men", 3),
    (try_begin),
      (eq, ":num_men", 0),
      (val_add, ":num_men", 1),
    (try_end),
    
    (try_begin),
      (assign, ":number_of_foods_player_has", 0),
      (try_for_range, ":cur_edible", food_begin, food_end),      
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
        (val_add, ":number_of_foods_player_has", 1),
      (try_end),
      (try_begin),
        (ge, ":number_of_foods_player_has", 6),
        (unlock_achievement, ACHIEVEMENT_ABUNDANT_FEAST),        
      (try_end),
    (try_end),
    
    (assign, ":consumption_amount", ":num_men"),
    (assign, ":no_food_displayed", 0),
    (try_for_range, ":unused", 0, ":consumption_amount"),
      (assign, ":available_food", 0),
      (try_for_range, ":cur_food", food_begin, food_end),
        (item_set_slot, ":cur_food", slot_item_is_checked, 0),
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten),
        (val_add, ":available_food", 1),
      (try_end),
      (try_begin),
        (gt, ":available_food", 0),
        (store_random_in_range, ":selected_food", 0, ":available_food"),
        (call_script, "script_consume_food", ":selected_food"),
      (else_try),
        (eq, ":no_food_displayed", 0),
        (display_message, "@Party has nothing to eat!", 0xFF0000),
        (call_script, "script_change_player_party_morale", -3),
        (assign, ":no_food_displayed", 1),
#NPC companion changes begin
        (try_begin),
            (call_script, "script_party_count_fit_regulars", "p_main_party"),
            (gt, reg0, 0),
            (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
        (try_end),
#NPC companion changes end
      (try_end),
    (try_end),
    ]),

  # Setting item modifiers for food
  (24,
   [
     (troop_get_inventory_capacity, ":inv_size", "trp_player"),
     (try_for_range, ":i_slot", 0, ":inv_size"),
       (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
       (this_or_next|eq, ":item_id", "itm_cattle_meat"),
       (this_or_next|eq, ":item_id", "itm_chicken"),
		(eq, ":item_id", "itm_pork"),
		
       (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
       (try_begin),
         (ge, ":modifier", imod_fresh),
         (lt, ":modifier", imod_rotten),
         (val_add, ":modifier", 1),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":modifier"),
       (else_try),
         (lt, ":modifier", imod_fresh),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", imod_fresh),
       (try_end),
     (try_end),
    ]),

  # Assigning lords to centers with no leaders
  (72,
   [
   #(call_script, "script_assign_lords_to_empty_centers"),
    ]),
  
  # Updating player icon in every frame
  (0,
   [(troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
    (assign, ":new_icon", -1),
    (try_begin),
      (eq, "$g_player_icon_state", pis_normal),
      (try_begin),
        (ge, ":cur_horse", 0),
        (assign, ":new_icon", "icon_player_horseman"),
      (else_try),
        (assign, ":new_icon", "icon_player"),
      (try_end),
    (else_try),
      (eq, "$g_player_icon_state", pis_camping),
      (assign, ":new_icon", "icon_camp"),
    (else_try),
      (eq, "$g_player_icon_state", pis_ship),
      (assign, ":new_icon", "icon_ship"),
    (try_end),
    (neq, ":new_icon", "$g_player_party_icon"),
    (assign, "$g_player_party_icon", ":new_icon"),
    (party_set_icon, "p_main_party", ":new_icon"),
    ]),
  
 #Update how good a target player is for bandits
  (2,
   [
       (store_troop_gold, ":total_value", "trp_player"),
       (store_div, ":bandit_attraction", ":total_value", (10000/100)), #10000 gold = excellent_target

       (troop_get_inventory_capacity, ":inv_size", "trp_player"),
       (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
       (try_end),
       (val_clamp, ":bandit_attraction", 0, 100),
       (party_set_bandit_attraction, "p_main_party", ":bandit_attraction"),
    ]),


	#This is a backup script to activate the player faction if it doesn't happen automatically, for whatever reason
  (3,
	[
	(try_for_range, ":center", walled_centers_begin, walled_centers_end),
		(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
		(store_faction_of_party, ":center_faction", ":center"),
		(eq, ":center_faction", "fac_player_supporters_faction"),
		(call_script, "script_activate_player_faction", "trp_player"),
	(try_end),
	]),
	
  # Checking escape chances of prisoners that joined the party recently.
  (6,
   [(gt, "$g_prisoner_recruit_troop_id", 0),
    (gt, "$g_prisoner_recruit_size", 0),
    (gt, "$g_prisoner_recruit_last_time", 0),
    (is_currently_night),
    (try_begin),
      (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
      (val_mul, ":leadership", 5),
      (store_sub, ":chance", 66, ":leadership"),
      (gt, ":chance", 0),
      (assign, ":num_escaped", 0),
      (try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", ":chance"),
        (val_add, ":num_escaped", 1),
      (try_end),
      (party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (assign, ":num_escaped", reg0),
      (gt, ":num_escaped", 0),
      (try_begin),
        (gt, ":num_escaped", 1),
        (assign, reg2, 1),
      (else_try),
        (assign, reg2, 0),
      (try_end),
      (assign, reg1, ":num_escaped"),
      (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night."),
    (try_end),
    (assign, "$g_prisoner_recruit_troop_id", 0),
    (assign, "$g_prisoner_recruit_size", 0),
    ]),

  # Offering ransom fees for player's prisoner heroes
  (24,
   [(neq, "$g_ransom_offer_rejected", 1),
    (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
    (eq, reg0, 0),#no prisoners offered
    (assign, ":end_cond", walled_centers_end),
    (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
      (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
      (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":center_no"),
      (eq, reg0, 1),#a prisoner is offered
      (assign, ":end_cond", 0),#break
    (try_end),
    ]), 

  # Exchanging hero prisoners between factions and clearing old ransom offers
  (72,
   [(assign, "$g_ransom_offer_rejected", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
      (gt, ":town_lord", 0),
      (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
      (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop", ":center_no", ":i_stack"),
        (troop_is_hero, ":stack_troop"),
        (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
        (store_random_in_range, ":random_no", 0, 100),
        (try_begin),
          (le, ":random_no", 10),
          (call_script, "script_calculate_ransom_amount_for_troop", ":stack_troop"),
          (assign, ":ransom_amount", reg0),
          (troop_get_slot, ":wealth", ":town_lord", slot_troop_wealth),
          (val_add, ":wealth", ":ransom_amount"),
          (troop_set_slot, ":town_lord", slot_troop_wealth, ":wealth"),
          (party_remove_prisoners, ":center_no", ":stack_troop", 1),
          (call_script, "script_remove_troop_from_prison", ":stack_troop"),
          (store_troop_faction, ":faction_no", ":town_lord"),
          (store_troop_faction, ":troop_faction", ":stack_troop"),
          (str_store_troop_name, s1, ":stack_troop"),
          (str_store_faction_name, s2, ":faction_no"),
          (str_store_faction_name, s3, ":troop_faction"),
          (display_log_message, "@{s1} of {s3} has been released from captivity."),
        (try_end),
      (try_end),
    (try_end),
    ]),
  
  # Adding mercenary troops to the towns
  (72,
   [
     (call_script, "script_update_mercenary_units_of_towns"),
     #NPC changes begin
     # removes   (call_script, "script_update_companion_candidates_in_taverns"),
     #NPC changes end
     (call_script, "script_update_ransom_brokers"),
     (call_script, "script_update_tavern_travellers"),
     (call_script, "script_update_tavern_minstrels"),
     (call_script, "script_update_booksellers"),
     (call_script, "script_update_villages_infested_by_bandits"),
     (try_for_range, ":village_no", villages_begin, villages_end),
       (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
       (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
     (try_end),
    ]),

  (24,
   [	
    (call_script, "script_update_other_taverngoers"),
	]),
	
  # Setting random walker types
  (36,
   [(try_for_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
      (             party_slot_eq, ":center_no", slot_party_type, spt_village),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money_helped),
      (store_random_in_range, ":rand", 0, 100),
      (try_begin),
        (lt, ":rand", 70),
        (neg|party_slot_ge, ":center_no", slot_town_prosperity, 60),
        (call_script, "script_cf_center_get_free_walker", ":center_no"),
        (call_script, "script_center_set_walker_to_type", ":center_no", reg0, walkert_needs_money),
      (try_end),
    (try_end),
    ]),

  # Checking center upgrades
  (12,
   [(try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot, ":cur_improvement", ":center_no", slot_center_current_improvement),
      (gt, ":cur_improvement", 0),
      (party_get_slot, ":cur_improvement_end_time", ":center_no", slot_center_improvement_end_hour),
      (store_current_hours, ":cur_hours"),
      (ge, ":cur_hours", ":cur_improvement_end_time"),
      (party_set_slot, ":center_no", ":cur_improvement", 1),
      (party_set_slot, ":center_no", slot_center_current_improvement, 0),
      (call_script, "script_get_improvement_details", ":cur_improvement"),
      (try_begin),
        (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
        (str_store_party_name, s4, ":center_no"),
        (display_log_message, "@Building of {s0} in {s4} has been completed."),
      (try_end),
      (try_begin),
        (is_between, ":center_no", villages_begin, villages_end),
        (eq, ":cur_improvement", slot_center_has_fish_pond),
        (call_script, "script_change_center_prosperity", ":center_no", 5),
      (try_end),
    (try_end),
    ]),

  # Adding tournaments to towns
  # Adding bandits to towns and villages
  (24,
   [(assign, ":num_active_tournaments", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament),
      (try_begin),
        (eq, ":has_tournament", 1),#tournament ended, simulate
        (call_script, "script_fill_tournament_participants_troop", ":center_no", 0),
        (call_script, "script_sort_tournament_participant_troops"),#may not be needed
        (call_script, "script_get_num_tournament_participants"),
        (store_sub, ":needed_to_remove_randomly", reg0, 1),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (try_begin),
          (is_between, ":winner_troop", active_npcs_begin, active_npcs_end),
          (str_store_troop_name_link, s1, ":winner_troop"),
          (str_store_party_name_link, s2, ":center_no"),
          (display_message, "@{s1} has won the tournament at {s2}."),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
        (try_end),
      (try_end),
      (val_sub, ":has_tournament", 1),
      (val_max, ":has_tournament", 0),
      (party_set_slot, ":center_no", slot_town_has_tournament, ":has_tournament"),
      (try_begin),
        (gt, ":has_tournament", 0),
        (val_add, ":num_active_tournaments", 1),
      (try_end),
    (try_end),
    
    (try_for_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
      (party_slot_eq, ":center_no", slot_party_type, spt_village),
      (party_get_slot, ":has_bandits", ":center_no", slot_center_has_bandits),
      (try_begin),
        (le, ":has_bandits", 0),
        (assign, ":continue", 0),
        (try_begin),
          (check_quest_active, "qst_deal_with_night_bandits"),
          (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, ":center_no"),
          (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
          (assign, ":continue", 1),
        (else_try),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 3),
          (assign, ":continue", 1),
        (try_end),
        (try_begin),
          (eq, ":continue", 1),
          (store_random_in_range, ":random_no", 0, 3),
          (try_begin),
            (eq, ":random_no", 0),
            (assign, ":bandit_troop", "trp_bandit"),
          (else_try),
            (eq, ":random_no", 1),
            (assign, ":bandit_troop", "trp_mountain_bandit"),
          (else_try),
            (assign, ":bandit_troop", "trp_forest_bandit"),
          (try_end),
          (party_set_slot, ":center_no", slot_center_has_bandits, ":bandit_troop"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (display_message, "@{!}{s1} is infested by bandits (at night)."),
          (try_end),
        (try_end),
      (else_try),
        (try_begin),
          (assign, ":random_chance", 40),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":random_chance", 20),
          (try_end),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":random_chance"),
          (party_set_slot, ":center_no", slot_center_has_bandits, 0),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (display_message, "@{s1} is no longer infested by bandits (at night)."),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
	
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
	  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
		
	  (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
	  (is_between, ":faction_object", towns_begin, towns_end),
	  
	  (party_slot_ge, ":faction_object", slot_town_has_tournament, 1),
	  #continue holding tournaments during the feast
      (party_set_slot, ":faction_object", slot_town_has_tournament, 2),
    (try_end),
	
	(try_begin),
      (lt, ":num_active_tournaments", 3),
      (store_random_in_range, ":random_no", 0, 100),
      #Add new tournaments with a 30% chance if there are less than 3 tournaments going on
      (lt, ":random_no", 30),
      (store_random_in_range, ":random_town", towns_begin, towns_end),
      (store_random_in_range, ":random_days", 12, 15),
      (party_set_slot, ":random_town", slot_town_has_tournament, ":random_days"),
      (try_begin),
        (eq, "$cheat_mode", 1),
        (str_store_party_name, s1, ":random_town"),
        (display_message, "@{!}{s1} is holding a tournament."),
      (try_end),
    (try_end),
    ]),

  (3,
[
	(assign, "$g_player_tournament_placement", 0),
]),  


#(0.1,

#	[
#	(try_begin),
#		(troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
#		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#		(store_faction_of_troop, ":spouse_faction", ":spouse"),
#		(neq, ":spouse_faction", "$players_kingdom"),
#		(display_message, "@{!}ERROR! Player and spouse are separate factions"),
#	(try_end),
#	]
#),
	
  # Asking to give center to player
  (8,
   [
#    (assign, ":done", 0),
#    (try_for_range, ":center_no", centers_begin, centers_end),
#      (eq, ":done", 0),
#      (party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
#      (assign, "$g_center_to_give_to_player", ":center_no"),
 #     (try_begin),
  #      (eq, "$g_center_to_give_to_player", "$g_castle_requested_by_player"),
   #     (assign, "$g_castle_requested_by_player", 0),
	#	(try_begin),
	#		(eq, "$g_castle_requested_for_troop", "trp_player"),
	#		(jump_to_menu, "mnu_requested_castle_granted_to_player"),
	#	(else_try),
	#		(jump_to_menu, "mnu_requested_castle_granted_to_player_husband"),
	#	(try_end),	
    #  (else_try),
    #    (jump_to_menu, "mnu_give_center_to_player"),
    # (try_end),
    #  (assign, ":done", 1),
    #(else_try),
    #  (eq, ":center_no", "$g_castle_requested_by_player"),
    #  (party_slot_ge, ":center_no", slot_town_lord, active_npcs_begin),
    #  (assign, "$g_castle_requested_by_player", 0),
    #  (store_faction_of_party, ":faction", ":center_no"),
    #  (eq, ":faction", "$players_kingdom"),
    #  (assign, "$g_center_to_give_to_player", ":center_no"),
	#  (try_begin),
#		(eq, "$player_has_homage", 1),
#		(jump_to_menu, "mnu_requested_castle_granted_to_another"),
#	  (else_try),	
#		(jump_to_menu, "mnu_requested_castle_granted_to_another_female"),
#	  (try_end),	
 #     (assign, ":done", 1),
  #  (try_end),
    ]),
  
  # Taking denars from player while resting in not owned centers
  (1,
   [(neg|map_free),
    (is_currently_night),
#    (ge, "$g_last_rest_center", 0),
    (is_between, "$g_last_rest_center", centers_begin, centers_end),
    (neg|party_slot_eq, "$g_last_rest_center", slot_town_lord, "trp_player"),
    (store_faction_of_party, ":last_rest_center_faction", "$g_last_rest_center"),
    (neq, ":last_rest_center_faction", "fac_player_supporters_faction"),
    (store_current_hours, ":cur_hours"),
    (ge, ":cur_hours", "$g_last_rest_payment_until"),
    (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
    (store_troop_gold, ":gold", "trp_player"),
    (party_get_num_companions, ":num_men", "p_main_party"),
    (store_div, ":total_cost", ":num_men", 4),
    (val_add, ":total_cost", 1),
    (try_begin),
      (ge, ":gold", ":total_cost"),
      (display_message, "@You pay for accommodation."),
      (troop_remove_gold, "trp_player", ":total_cost"),
    (else_try),
      (gt, ":gold", 0),
      (troop_remove_gold, "trp_player", ":gold"),
    (try_end),
    ]),
    
  # Spawn some bandits.
  (36,
   [
       (call_script, "script_spawn_bandits"),
    ]),

  # Make parties larger as game progresses.
  (24,
   [
       (call_script, "script_update_party_creation_random_limits"),
    ]),
  
  # Check if a faction is defeated every day
  (24,
   [
    (assign, ":num_active_factions", 0),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_set_slot, ":cur_kingdom", slot_faction_number_of_parties, 0),
    (try_end),
    (try_for_parties, ":cur_party"),
      (store_faction_of_party, ":party_faction", ":cur_party"),
      (is_between, ":party_faction", kingdoms_begin, kingdoms_end),
      (this_or_next|is_between, ":cur_party", centers_begin, centers_end),
	  (party_slot_eq, ":cur_party", slot_party_type, spt_kingdom_hero_party),
      (faction_get_slot, ":kingdom_num_parties", ":party_faction", slot_faction_number_of_parties),
      (val_add, ":kingdom_num_parties", 1),
      (faction_set_slot, ":party_faction", slot_faction_number_of_parties, ":kingdom_num_parties"), 
    (try_end),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      #(try_begin),
        #(eq, "$cheat_mode", 1),
        #(str_store_faction_name, s1, ":cur_kingdom"),
        #(faction_get_slot, reg1, ":cur_kingdom", slot_faction_number_of_parties),        
        #(display_message, "@{!}Number of parties belonging to {s1}: {reg1}"),
      #(try_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      (val_add, ":num_active_factions", 1),
      (faction_slot_eq, ":cur_kingdom", slot_faction_number_of_parties, 0),
      (assign, ":faction_removed", 0),
      (try_begin),
        (eq, ":cur_kingdom", "fac_player_supporters_faction"),
        (try_begin),
          (le, "$supported_pretender", 0),
          (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_inactive),
          (assign, ":faction_removed", 1),
        (try_end),
      (else_try),
        (neq, "$players_kingdom", ":cur_kingdom"),
        (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_defeated),
        (try_for_parties, ":cur_party"),
          (store_faction_of_party, ":party_faction", ":cur_party"),
          (eq, ":party_faction", ":cur_kingdom"),
          (party_get_slot, ":home_center", ":cur_party", slot_party_home_center),
          (store_faction_of_party, ":home_center_faction", ":home_center"),
          (party_set_faction, ":cur_party", ":home_center_faction"),
        (try_end),
        (assign, ":kingdom_pretender", -1),
        (try_for_range, ":cur_pretender", pretenders_begin, pretenders_end),
          (troop_slot_eq, ":cur_pretender", slot_troop_original_faction, ":cur_kingdom"),
          (assign, ":kingdom_pretender", ":cur_pretender"),
        (try_end),
        (try_begin),
          (is_between, ":kingdom_pretender", pretenders_begin, pretenders_end),
          (neq, ":kingdom_pretender", "$supported_pretender"),
          (troop_set_slot, ":kingdom_pretender", slot_troop_cur_center, 0), #remove pretender from the world
        (try_end),
        (assign, ":faction_removed", 1),
        (try_begin),
          (eq, "$players_oath_renounced_against_kingdom", ":cur_kingdom"),
          (assign, "$players_oath_renounced_against_kingdom", 0),
          (assign, "$players_oath_renounced_given_center", 0),
          (assign, "$players_oath_renounced_begin_time", 0),
          (call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":cur_kingdom", 0),
        (try_end),
        #This menu must be at the end because faction banner will change after this menu if the player's supported pretender's original faction is cur_kingdom
        (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":cur_kingdom", 0),
      (try_end),
      (try_begin),
        (eq, ":faction_removed", 1),
        (val_sub, ":num_active_factions", 1),
        #(call_script, "script_store_average_center_value_per_faction"),
      (try_end),
      (try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom_2"),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":num_active_factions", 1),
      (eq, "$g_one_faction_left_notification_shown", 0),
      (assign, "$g_one_faction_left_notification_shown", 1),
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
        (call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":cur_kingdom", 0),
      (try_end),
    (try_end),
    ]),

  (3, #check to see if player's court has been captured
   [
     (try_begin), #The old court has been lost
       (is_between, "$g_player_court", centers_begin, centers_end),
       (store_faction_of_party, ":court_faction", "$g_player_court"),
       (neq, ":court_faction", "fac_player_supporters_faction"),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),	#At least one new court has been found
       (lt, "$g_player_court", centers_begin),
       #Will by definition not active until a center is taken by the player faction
       #Player minister must have been appointed at some point
       (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
		(gt, "$g_player_minister", 0),
		
       (assign, ":center_found", 0),
       (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
         (eq, ":center_found", 0),
         (store_faction_of_party, ":court_faction", ":walled_center"),
         (eq, ":court_faction", "fac_player_supporters_faction"),
         (assign, ":center_found", ":walled_center"),
       (try_end),
       (ge, ":center_found", 1),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (try_end),
     #Also, piggy-backing on this -- having bandits go to lairs and back
     (try_for_parties, ":bandit_party"),
       (gt, ":bandit_party", "p_spawn_points_end"),
       (party_get_template_id, ":bandit_party_template", ":bandit_party"),
       (is_between, ":bandit_party_template", "pt_steppe_bandits", "pt_deserters"),
       (party_template_get_slot, ":bandit_lair", ":bandit_party_template", slot_party_template_lair_party),
       (try_begin),#If party is active and bandit is far away, then move to location
         (gt, ":bandit_lair", "p_spawn_points_end"),
         (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"), #this is the cause of the error
         (gt, ":distance", 30),
         #All this needs checking
         (party_set_ai_behavior, ":bandit_party", ai_bhvr_travel_to_point),
         (party_get_position, pos5, ":bandit_lair"),
         (party_set_ai_target_position, ":bandit_party", pos5),
       (else_try), #Otherwise, act freely
         (get_party_ai_behavior, ":behavior", ":bandit_party"),
         (eq, ":behavior", ai_bhvr_travel_to_point),
         (try_begin),
           (gt, ":bandit_lair", "p_spawn_points_end"),
           (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"),
           (lt, ":distance", 3),
           (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
           (party_template_get_slot, ":spawnpoint", ":bandit_party_template", slot_party_template_lair_spawnpoint),
           (party_set_ai_object, ":bandit_party", ":spawnpoint"),
           (party_set_ai_patrol_radius, ":bandit_party", 45),
         (else_try),
           (lt, ":bandit_lair", "p_spawn_points_end"),
           (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
           (party_template_get_slot, ":spawnpoint", ":bandit_party_template", slot_party_template_lair_spawnpoint),
           (party_set_ai_object, ":bandit_party", ":spawnpoint"),
           (party_set_ai_patrol_radius, ":bandit_party", 45),
         (try_end),
       (try_end),
     (try_end),
     #Piggybacking on trigger:
     (try_begin),
       (troop_get_slot, ":betrothed", "trp_player", slot_troop_betrothed),
       (gt, ":betrothed", 0),
       (neg|check_quest_active, "qst_wed_betrothed"),
       (neg|check_quest_active, "qst_wed_betrothed_female"),
       (str_store_troop_name, s5, ":betrothed"),
       (display_message, "@Betrothal to {s5} expires"),
       (troop_set_slot, "trp_player", slot_troop_betrothed, -1),
       (troop_set_slot, ":betrothed", slot_troop_betrothed, -1),
     (try_end),
     ]),
		
  # Reduce renown slightly by 0.5% every week
  (7 * 24,
   [
       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
       (store_div, ":renown_decrease", ":player_renown", 200),
       (val_sub, ":player_renown", ":renown_decrease"),
       (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
    ]),

  # Read books if player is resting.
  (1, [(neg|map_free),
       (gt, "$g_player_reading_book", 0),
       (player_has_item, "$g_player_reading_book"),
       (store_attribute_level, ":int", "trp_player", ca_intelligence),
       (item_get_slot, ":int_req", "$g_player_reading_book", slot_item_intelligence_requirement),
       (le, ":int_req", ":int"),
       (item_get_slot, ":book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
       (item_get_slot, ":book_read", "$g_player_reading_book", slot_item_book_read),
       (eq, ":book_read", 0),
       (val_add, ":book_reading_progress", 7),
       (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":book_reading_progress"),
       (ge, ":book_reading_progress", 1000),
       (item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
       (str_store_item_name, s1, "$g_player_reading_book"),
       (str_clear, s2),
       (try_begin),
         (eq, "$g_player_reading_book", "itm_book_tactics"),
         (troop_raise_skill, "trp_player", "skl_tactics", 1),
         (str_store_string, s2, "@ Your tactics skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_persuasion"),
         (troop_raise_skill, "trp_player", "skl_persuasion", 1),
         (str_store_string, s2, "@ Your persuasion skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_leadership"),
         (troop_raise_skill, "trp_player", "skl_leadership", 1),
         (str_store_string, s2, "@ Your leadership skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_intelligence"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 1),
         (str_store_string, s2, "@ Your intelligence has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_trade"),
         (troop_raise_skill, "trp_player", "skl_trade", 1),
         (str_store_string, s2, "@ Your trade skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
         (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
         (str_store_string, s2, "@ Your weapon master skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_engineering"),
         (troop_raise_skill, "trp_player", "skl_engineer", 1),
         (str_store_string, s2, "@ Your engineer skill has increased by 1."),
       (try_end),
       
       (unlock_achievement, ACHIEVEMENT_BOOK_WORM),

       (try_begin),
         (eq, "$g_infinite_camping", 0),
         (dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
       (try_end),  
              
       (assign, "$g_player_reading_book", 0),	   	   
       ]),

# Removing cattle herds if they are way out of range
  (12, [(try_for_parties, ":cur_party"),
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist",":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              #Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd"),
              (neg|check_quest_concluded, "qst_move_cattle_herd"),
              (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", slot_cattle_driven_by_player, 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),
    ]),

  
#####!!!!!

# Village upgrade triggers

# School
  (30 * 24,
   [(try_for_range, ":cur_village", villages_begin, villages_end),
      (party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
      (party_slot_eq, ":cur_village", slot_center_has_school, 1),
      (party_get_slot, ":cur_relation", ":cur_village", slot_center_player_relation),
      (val_add, ":cur_relation", 1),
      (val_min, ":cur_relation", 100),
      (party_set_slot, ":cur_village", slot_center_player_relation, ":cur_relation"),
    (try_end),
    ]),

# Quest triggers:

# Remaining days text update
  (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", slot_quest_expiration_days, 1),
              (quest_get_slot, ":exp_days", ":cur_quest", slot_quest_expiration_days),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 1),
              (else_try),
                (quest_set_slot, ":cur_quest", slot_quest_expiration_days, ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
          (else_try),
            (quest_slot_ge, ":cur_quest", slot_quest_dont_give_again_remaining_days, 1),
            (quest_get_slot, ":value", ":cur_quest", slot_quest_dont_give_again_remaining_days),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", slot_quest_dont_give_again_remaining_days, ":value"),
          (try_end),
        (try_end),
    ]),

# Report to army quest 
  (2,
   [
     (eq, "$g_infinite_camping", 0),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
     (eq, "$g_player_is_captive", 0),
     	 
	 (try_begin),
		(check_quest_active, "qst_report_to_army"),
		(faction_slot_eq, "$players_kingdom", slot_faction_marshall, -1),
		(call_script, "script_abort_quest", "qst_report_to_army", 0),
	 (try_end),
	 
	 (faction_get_slot, ":faction_object", "$players_kingdom", slot_faction_ai_object),         
	 
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),     
          
     (assign, ":continue", 1),
     (try_begin),     
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_enemies_around_center),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
       (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_raiding_village),                            
       (neg|is_between, ":faction_object", walled_centers_begin, walled_centers_end),
       (assign, ":continue", 0),
     (try_end),       
     (eq, ":continue", 1),
                            	 
	 (assign, ":kingdom_is_at_war", 0),
	 (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		(neq, ":faction", "$players_kingdom"),
		(store_relation, ":relation", ":faction", "$players_kingdom"),
		(lt, ":relation", 0),
		(assign, ":kingdom_is_at_war", 1),
	 (try_end),
	 (eq, ":kingdom_is_at_war", 1),
	 	 
     (neg|check_quest_active, "qst_report_to_army"),
     (neg|check_quest_active, "qst_follow_army"),
     
     (neg|quest_slot_ge, "qst_report_to_army", slot_quest_dont_give_again_remaining_days, 1),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     
     (store_distance_to_party_from_party, ":distance_to_marshal", ":faction_marshall_party", "p_main_party"),
     (le, ":distance_to_marshal", 96),
     
     (assign, ":has_no_quests", 1),     
     (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     
     (try_for_range, ":cur_quest", lord_quests_begin_2, lord_quests_end_2),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     
     (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
       (check_quest_active, ":cur_quest"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     
     (store_character_level, ":level", "trp_player"),
     (ge, ":level", 8),
     (assign, ":cur_target_amount", 2),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
       (try_begin),
         (party_slot_eq, ":cur_center", slot_party_type, spt_town),
         (val_add, ":cur_target_amount", 3),
       (else_try),
         (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
         (val_add, ":cur_target_amount", 1),
       (else_try),
         (val_add, ":cur_target_amount", 1),
       (try_end),
     (try_end),
     
     (val_mul, ":cur_target_amount", 4),
     (val_min, ":cur_target_amount", 60),
     (quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":cur_target_amount"),
     (quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
     (quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 22),     
     (jump_to_menu, "mnu_kingdom_army_quest_report_to_army"),
   ]),


# Army quest initializer
  (3,
   [
     (assign, "$g_random_army_quest", -1),
     (check_quest_active, "qst_follow_army", 1),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
#Rebellion changes begin
#     (neg|is_between, "$players_kingdom", rebel_factions_begin, rebel_factions_end),
#Rebellion changes end
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (neq, ":faction_marshall", "trp_player"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     (store_distance_to_party_from_party, ":dist", ":faction_marshall_party", "p_main_party"),
     (try_begin),
       (lt, ":dist", 15),
       (assign, "$g_player_follow_army_warnings", 0),
       (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":last_offensive_time", "$players_kingdom", slot_faction_last_offensive_concluded),
       (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),

       (assign, ":result", -1),
       (try_begin),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (troop_slot_eq, ":faction_marshall", slot_troop_does_not_give_quest, 0),
         (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
           (eq, ":result", -1),
           (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
           (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
           (try_begin),
             (eq, ":quest_no", "qst_deliver_cattle_to_army"),
			# (eq, 1, 0), #disables temporarily			 
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (gt, ":passed_time", 120),#5 days
               (store_random_in_range, ":quest_target_amount", 5, 10),
               (assign, ":result","qst_deliver_cattle_to_army"),
               (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 10),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 30),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_join_siege_with_army"),
			 (eq, 1, 0),
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (faction_get_slot, ":ai_object", "$players_kingdom", slot_faction_ai_object),
               (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
               (party_get_battle_opponent, ":besieged_center", ":faction_marshall_party"),
               (eq, ":besieged_center", ":ai_object"),
               #army is assaulting the center
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_target_center, ":ai_object"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 2),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 15),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_scout_waypoints"),
             (try_begin),
               (assign, ":end_cond", 100),
               (assign, "$qst_scout_waypoints_wp_1", -1),
               (assign, "$qst_scout_waypoints_wp_2", -1),
               (assign, "$qst_scout_waypoints_wp_3", -1),
               (assign, ":continue", 0),
               (try_for_range, ":unused", 0, ":end_cond"),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_1", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (assign, "$qst_scout_waypoints_wp_1", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_2", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (assign, "$qst_scout_waypoints_wp_2", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_3", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (neq, "$qst_scout_waypoints_wp_2", reg0),
                   (assign, "$qst_scout_waypoints_wp_3", reg0),
                 (try_end),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                 (ge, "$qst_scout_waypoints_wp_1", 0),
                 (ge, "$qst_scout_waypoints_wp_2", 0),
                 (ge, "$qst_scout_waypoints_wp_3", 0),
                 (assign, ":end_cond", 0),
                 (assign, ":continue", 1),
               (try_end),
               (eq, ":continue", 1),
               (assign, "$qst_scout_waypoints_wp_1_visited", 0),
               (assign, "$qst_scout_waypoints_wp_2_visited", 0),
               (assign, "$qst_scout_waypoints_wp_3_visited", 0),
               (assign, ":result", "qst_scout_waypoints"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 7),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 25),
             (try_end),
           (try_end),
         (try_end),
		 
         (try_begin),
           (neq, ":result", -1),
           (quest_set_slot, ":result", slot_quest_current_state, 0),
           (quest_set_slot, ":result", slot_quest_giver_troop, ":faction_marshall"),
           (try_begin),
             (eq, ":result", "qst_join_siege_with_army"),
             (jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
           (else_try),
             (assign, "$g_random_army_quest", ":result"),
             (quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":faction_marshall"),
             (jump_to_menu, "mnu_kingdom_army_quest_messenger"),
           (try_end),
         (try_end),
       (try_end),
     (else_try),
       (val_add, "$g_player_follow_army_warnings", 1),
       (try_begin),
         (lt, "$g_player_follow_army_warnings", 15),
         (try_begin),
           (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 3),
           (eq, ":follow_mod", 0),
           (str_store_troop_name_link, s1, ":faction_marshall"),
           (try_begin),
             (lt, "$g_player_follow_army_warnings", 8),
#             (display_message, "str_marshal_warning"),
           (else_try),
             (display_message, "str_marshal_warning"),
           (try_end),
         (try_end),
       (else_try),
         (jump_to_menu, "mnu_kingdom_army_follow_failed"),
       (try_end),
     (try_end),
    ]),

# Move cattle herd
  (0.5, [(check_quest_active,"qst_move_cattle_herd"),
         (neg|check_quest_concluded,"qst_move_cattle_herd"),
         (quest_get_slot, ":target_party", "qst_move_cattle_herd", slot_quest_target_party),
         (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
         (store_distance_to_party_from_party, ":dist",":target_party", ":target_center"),
         (lt, ":dist", 3),
         (remove_party, ":target_party"),
         (call_script, "script_succeed_quest", "qst_move_cattle_herd"),
    ]),

  (2, [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		 (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		 (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":party_no", 1),
		 (party_is_active, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_following_player, 1),
         (store_current_hours, ":cur_time"),
         (neg|party_slot_ge, ":party_no", slot_party_follow_player_until_time, ":cur_time"),
         (party_set_slot, ":party_no", slot_party_commander_party, -1),
         (party_set_slot, ":party_no", slot_party_following_player, 0),
         (assign,  ":dont_follow_period", 200),
         (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
         (party_set_slot, ":party_no", slot_party_dont_follow_player_until_time,  ":dont_follow_time"),
       (try_end),
    ]),

# Deliver cattle and deliver cattle to army
  (0.5,
   [
     (try_begin),
       (check_quest_active,"qst_deliver_cattle"),
       (neg|check_quest_succeeded, "qst_deliver_cattle"),
       (quest_get_slot, ":target_center", "qst_deliver_cattle", slot_quest_target_center),
       (quest_get_slot, ":target_amount", "qst_deliver_cattle", slot_quest_target_amount),
       (quest_get_slot, ":cur_amount", "qst_deliver_cattle", slot_quest_current_state),
       (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
       (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
       (val_add, ":cur_amount", reg0),
       (quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":cur_amount"),
       (le, ":target_amount", ":cur_amount"),
       (call_script, "script_succeed_quest", "qst_deliver_cattle"),
     (try_end),
     (try_begin),
       (check_quest_active, "qst_deliver_cattle_to_army"),
       (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
       (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
       (troop_get_slot, ":target_party", ":giver_troop", slot_troop_leaded_party),
       (try_begin),
         (gt, ":target_party", 0),
         (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
         (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", slot_quest_current_state),
         (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
         (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
         (val_add, ":cur_amount", reg0),
         (quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":cur_amount"),
         (try_begin),
           (le, ":target_amount", ":cur_amount"),
           (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
         (try_end),
       (else_try),
         (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
       (try_end),
     (try_end),
     ]),

# Train peasants against bandits
  (1,
   [
     (neg|map_free),
     (check_quest_active, "qst_train_peasants_against_bandits"),
     (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
     (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
     (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
     (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":trainer_skill", reg0),
     (store_sub, ":needed_hours", 20, ":trainer_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
     (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
     (rest_for_hours, 0, 0, 0), #stop resting
     (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
     ]),

# Scout waypoints
  (1,
   [
     (check_quest_active,"qst_scout_waypoints"),
     (neg|check_quest_succeeded, "qst_scout_waypoints"),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_1_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_1_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_2_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_2_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_3_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_3_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (eq, "$qst_scout_waypoints_wp_1_visited", 1),
     (eq, "$qst_scout_waypoints_wp_2_visited", 1),
     (eq, "$qst_scout_waypoints_wp_3_visited", 1),
     (call_script, "script_succeed_quest", "qst_scout_waypoints"),
     ]),
  
# Kill local merchant
  
  (3, [(neg|map_free),
       (check_quest_active, "qst_kill_local_merchant"),
       (quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
       (quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
       (rest_for_hours, 0, 0, 0), #stop resting
       (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
       (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
       ]),

# Collect taxes
  (1, [(neg|map_free),
       (check_quest_active, "qst_collect_taxes"),
       (eq, "$g_player_is_captive", 0),
       (eq, "$qst_collect_taxes_currently_collecting", 1),
       (quest_get_slot, ":quest_current_state", "qst_collect_taxes", slot_quest_current_state),
       (this_or_next|eq, ":quest_current_state", 1),
       (this_or_next|eq, ":quest_current_state", 2),
       (eq, ":quest_current_state", 3),
       (quest_get_slot, ":left_hours", "qst_collect_taxes", slot_quest_target_amount),
       (val_sub, ":left_hours", 1),
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":left_hours"),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
       
       (try_begin),
         (lt, ":left_hours", 0),
         (assign, ":quest_current_state", 4),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
         (rest_for_hours, 0, 0, 0), #stop resting
         (jump_to_menu, "mnu_collect_taxes_complete"),
       (else_try),
         #Continue collecting taxes
         (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
         (party_get_slot, ":prosperity", "$g_encountered_party", slot_town_prosperity),
         (store_add, ":multiplier", 30, ":prosperity"),
         (val_mul, ":max_collected_tax", ":multiplier"),
         (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values
       
         (try_begin),
           (eq, "$qst_collect_taxes_halve_taxes", 1),
           (val_div, ":max_collected_tax", 2),
         (try_end),
         (val_max, ":max_collected_tax", 2),
         (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
         (quest_get_slot, ":cur_collected", "qst_collect_taxes", slot_quest_gold_reward),
         (val_add, ":cur_collected", ":collected_tax"),
         (quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":cur_collected"),
         (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
       (try_end),
       (try_begin),
         (eq, ":quest_current_state", 1),
         (val_sub, "$qst_collect_taxes_menu_counter", 1),
         (le, "$qst_collect_taxes_menu_counter", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
         (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
       (else_try), #Chance of revolt against player
         (eq, ":quest_current_state", 2),
         (val_sub, "$qst_collect_taxes_unrest_counter", 1),
         (le, "$qst_collect_taxes_unrest_counter", 0),
         (eq, "$qst_collect_taxes_halve_taxes", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),

         (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
         (val_add, ":unrest_chance",30),
       
         (store_random_in_range, ":unrest_roll", 0, 1000),
         (try_begin),
           (lt, ":unrest_roll", ":unrest_chance"),
           (jump_to_menu, "mnu_collect_taxes_revolt"),
         (try_end),
       (try_end),
       ]),

#persuade_lords_to_make_peace begin
  (72, [(gt, "$g_force_peace_faction_1", 0),
        (gt, "$g_force_peace_faction_2", 0),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
        (try_end),
        (assign, "$g_force_peace_faction_1", 0),
        (assign, "$g_force_peace_faction_2", 0),
       ]),  

#NPC changes begin
#Resolve one issue each hour
(1, 
   [           
		(str_store_string, s51, "str_no_trigger_noted"),
		
		# Rejoining party
        (try_begin),
            (gt, "$npc_to_rejoin_party", 0),
            (eq, "$g_infinite_camping", 0),
            (try_begin),
                (neg|main_party_has_troop, "$npc_to_rejoin_party"),
                (neq, "$g_player_is_captive", 1),

				(str_store_string, s51, "str_triggered_by_npc_to_rejoin_party"),
				
                (assign, "$npc_map_talk_context", slot_troop_days_on_mission),
                (start_map_conversation, "$npc_to_rejoin_party", -1),
			(else_try),
				(troop_set_slot, "$npc_to_rejoin_party", slot_troop_current_mission, npc_mission_rejoin_when_possible),
				(assign, "$npc_to_rejoin_party", 0),
            (try_end),			
		# Here do NPC that is quitting
		(else_try),
            (gt, "$npc_is_quitting", 0),
            (eq, "$g_infinite_camping", 0),
            (try_begin),
                (main_party_has_troop, "$npc_is_quitting"),
                (neq, "$g_player_is_captive", 1),

				(str_store_string, s51, "str_triggered_by_npc_is_quitting"),
                (start_map_conversation, "$npc_is_quitting", -1),
            (else_try),
                (assign, "$npc_is_quitting", 0),
            (try_end),
		#NPC with grievance	
        (else_try), #### Grievance
            (gt, "$npc_with_grievance", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_grievance"),
                (neq, "$g_player_is_captive", 1),

				(str_store_string, s51, "str_triggered_by_npc_has_grievance"),
				
                (assign, "$npc_map_talk_context", slot_troop_morality_state),
                (start_map_conversation, "$npc_with_grievance", -1),
            (else_try),
                (assign, "$npc_with_grievance", 0),
            (try_end),
        (else_try),
            (gt, "$npc_with_personality_clash", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (troop_get_slot, ":object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
            (try_begin),
                (main_party_has_troop, "$npc_with_personality_clash"),
                (main_party_has_troop, ":object"),
                (neq, "$g_player_is_captive", 1),
				
                (assign, "$npc_map_talk_context", slot_troop_personalityclash_state),
				(str_store_string, s51, "str_triggered_by_npc_has_personality_clash"),
                (start_map_conversation, "$npc_with_personality_clash", -1),
            (else_try),
                (assign, "$npc_with_personality_clash", 0),
            (try_end),
        (else_try), #### Political issue
            (gt, "$npc_with_political_grievance", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_political_grievance"),
                (neq, "$g_player_is_captive", 1),
				
				(str_store_string, s51, "str_triggered_by_npc_has_political_grievance"),
                (assign, "$npc_map_talk_context", slot_troop_kingsupport_objection_state),
                (start_map_conversation, "$npc_with_political_grievance", -1),
			(else_try),
				(assign, "$npc_with_political_grievance", 0),
            (try_end),
		(else_try),	
            (eq, "$disable_sisterly_advice", 0),
            (eq, "$g_infinite_camping", 0),
            (gt, "$npc_with_sisterly_advice", 0),
            (try_begin),
				(main_party_has_troop, "$npc_with_sisterly_advice"),
                (neq, "$g_player_is_captive", 1),
				
				(assign, "$npc_map_talk_context", slot_troop_woman_to_woman_string), #was npc_with_sisterly advice
	            (start_map_conversation, "$npc_with_sisterly_advice", -1),
			(else_try),
				(assign, "$npc_with_sisterly_advice", 0),
            (try_end),
		(else_try), #check for regional background
            (eq, "$disable_local_histories", 0),
            (eq, "$g_infinite_camping", 0),
            (try_for_range, ":npc", companions_begin, companions_end),
                (main_party_has_troop, ":npc"),           
                (troop_slot_eq, ":npc", slot_troop_home_speech_delivered, 0),
                (troop_get_slot, ":home", ":npc", slot_troop_home),
                (gt, ":home", 0),
                (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
                (lt, ":distance", 7),
                (assign, "$npc_map_talk_context", slot_troop_home),
				
				(str_store_string, s51, "str_triggered_by_local_histories"),
				
                (start_map_conversation, ":npc", -1),
            (try_end),
        (try_end),
		
		#add pretender to party if not active
		(try_begin),
			(check_quest_active, "qst_rebel_against_kingdom"),
			(is_between, "$supported_pretender", pretenders_begin, pretenders_end),
			(neg|main_party_has_troop, "$supported_pretender"),
			(neg|troop_slot_eq, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
			(party_add_members, "p_main_party", "$supported_pretender", 1),
		(try_end),
		
		#make player marshal of rebel faction
		(try_begin),
			(check_quest_active, "qst_rebel_against_kingdom"),
			(is_between, "$supported_pretender", pretenders_begin, pretenders_end),
			(main_party_has_troop, "$supported_pretender"),
			(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),
			(call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
		(try_end),
		
		
]),
#NPC changes end

(4, 
   [(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
      (troop_slot_ge, ":troop_no", slot_troop_change_to_faction, 1),
      (store_troop_faction, ":faction_no", ":troop_no"),
      (troop_get_slot, ":new_faction_no", ":troop_no", slot_troop_change_to_faction),
      (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
      (assign, ":continue", 0),
      (try_begin),
        (le, ":party_no", 0),
        #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (assign, ":continue", 1),
      (else_try),
        (gt, ":party_no", 0),

        #checking if the party is outside the centers
        (party_get_attached_to, ":cur_center_no", ":party_no"),
        (try_begin),
          (lt, ":cur_center_no", 0),
          (party_get_cur_town, ":cur_center_no", ":party_no"),
        (try_end),
        (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
        (party_slot_eq, ":cur_center_no", slot_town_lord, ":troop_no"),
    
        #checking if the party is away from his original faction parties
        (assign, ":end_cond", active_npcs_end),
        (try_for_range, ":enemy_troop_no", active_npcs_begin, ":end_cond"),
		  (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", slot_troop_leaded_party),
          (party_is_active, ":enemy_party_no"),
          (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
          (eq, ":enemy_faction_no", ":faction_no"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
          (lt, ":dist", 4),
          (assign, ":end_cond", 0),
        (try_end),
        (neq, ":end_cond", 0),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),
	  
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":troop_no"),
			(display_message, "@{!}DEBUG - {s4} faction changed from slot_troop_change_to_faction"), 
		(try_end),	  
		
      (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
      (troop_set_slot, ":troop_no", slot_troop_change_to_faction, 0),
      (try_begin),
        (is_between, ":new_faction_no", kingdoms_begin, kingdoms_end),
        (str_store_troop_name_link, s1, ":troop_no"),
        (str_store_faction_name_link, s2, ":faction_no"),
        (str_store_faction_name_link, s3, ":new_faction_no"),
        (display_message, "@{s1} has switched from {s2} to {s3}."),
        (try_begin),
          (eq, ":faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
        (else_try),
          (eq, ":new_faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),


(1,
   [
     (eq, "$cheat_mode", 1),
     (try_for_range, ":center_no", centers_begin, centers_end),
       (party_get_battle_opponent, ":besieger_party", ":center_no"),
       (try_begin),
         (gt, ":besieger_party", 0),
         (str_store_party_name, s2, ":center_no"),
         (str_store_party_name, s3, ":besieger_party"),
         (display_message, "@{!}DEBUG : {s2} is besieging by {s3}"),
       (try_end),
     (try_end),    
     ]),

(1, 
   [
     (store_current_day, ":cur_day"),
     (gt, ":cur_day", "$g_last_report_control_day"),
     (store_time_of_day, ":cur_hour"),
     (ge, ":cur_hour", 18),

     (store_random_in_range, ":rand_no", 0, 4),
     (this_or_next|ge, ":cur_hour", 22),
     (eq, ":rand_no", 0),
     
     (assign, "$g_last_report_control_day", ":cur_day"),
     
     (store_troop_gold, ":gold", "trp_player"),
     
     (try_begin),
       (lt, ":gold", 0),
       (store_sub, ":gold_difference", 0, ":gold"),
       (troop_add_gold, "trp_player", ":gold_difference"),
     (try_end),

     (party_get_morale, ":main_party_morale", "p_main_party"),     
     
     #(assign, ":swadian_soldiers_are_upset_message_showed", 0),
     #(assign, ":vaegir_soldiers_are_upset_message_showed", 0),
     #(assign, ":khergit_soldiers_are_upset_message_showed", 0),
     #(assign, ":nord_soldiers_are_upset_message_showed", 0),
     #(assign, ":rhodok_soldiers_are_upset_message_showed", 0),
    
     (try_begin),
       (str_store_string, s1, "str_party_morale_is_low"),            
       (str_clear, s2),

       (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
       (assign, ":num_deserters_total", 0),
       (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
         (neg|troop_is_hero, ":stack_troop"),
         (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
         
         (store_troop_faction, ":faction_no", ":stack_troop"),
      
         (assign, ":troop_morale", ":main_party_morale"),         
         (try_begin),
           (ge, ":faction_no", npc_kingdoms_begin),
           (lt, ":faction_no", npc_kingdoms_end),
        
           (faction_get_slot, ":troop_morale_addition", ":faction_no",  slot_faction_morale_of_player_troops),
           (val_div, ":troop_morale_addition", 100),
           (val_add, ":troop_morale", ":troop_morale_addition"),
         (try_end),

         (lt, ":troop_morale", 32),
         (store_sub, ":desert_prob", 36, ":troop_morale"),
         (val_div, ":desert_prob", 4),

         (assign, ":num_deserters_from_that_troop", 0),
         (try_for_range, ":unused", 0, ":stack_size"),
           (store_random_in_range, ":rand_no", 0, 100),
           (lt, ":rand_no", ":desert_prob"),
           (val_add, ":num_deserters_from_that_troop", 1),
           #p.remove_members_from_stack(i_stack,cur_deserters, &main_party_instances);
           (remove_member_from_party, ":stack_troop", "p_main_party"),
         (try_end),
         (try_begin),
           (ge, ":num_deserters_from_that_troop", 1),           
           (str_store_troop_name, s2, ":stack_troop"),
           (assign, reg0, ":num_deserters_from_that_troop"),
           
#           (try_begin),           
#             (lt, ":troop_morale_addition", -2),
#             (ge, ":main_party_morale", 28),
#             (try_begin),
#               (eq, ":faction_no", "fac_kingdom_1"),  
#               (eq, ":swadian_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_swadian_soldiers_are_upset"),
#               (assign, ":swadian_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_2"),  
#               (eq, ":vaegir_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_vaegir_soldiers_are_upset"),
#               (assign, ":vaegir_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_3"),  
#               (eq, ":khergit_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_khergit_soldiers_are_upset"),
#               (assign, ":khergit_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_4"),  
#               (eq, ":nord_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_nord_soldiers_are_upset"),
#               (assign, ":nord_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_5"),  
#               (eq, ":rhodok_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_rhodok_soldiers_are_upset"),
#               (assign, ":rhodok_soldiers_are_upset_message_showed", 1),
#             (try_end),
#             (str_store_string, s1, "@{!}{s1} {s3}"),
#           (try_end),
           
           (try_begin),
             (ge, ":num_deserters_total", 1),
             (str_store_string, s1, "str_s1_reg0_s2"),
           (else_try),
             (str_store_string, s3, s1),
             (str_store_string, s1, "str_s3_reg0_s2"),
           (try_end),
           (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
         (try_end),
       (try_end),

       (try_begin),
         (ge, ":num_deserters_total", 1),
  
         (try_begin),
           (ge, ":num_deserters_total", 2),
           (str_store_string, s2, "str_have_deserted_the_party"),
         (else_try),
           (str_store_string, s2, "str_has_deserted_the_party"),
         (try_end),          

         (str_store_string, s1, "str_s1_s2"),

         (eq, "$g_infinite_camping", 0),
         
         (tutorial_box, s1, "str_weekly_report"),
       (try_end), 
     (try_end),
 ]),
 # reserved for future use. For backward compatibility, we need to use these triggers instead of creating new ones.
  
  (1,
   [
     (call_script, "script_calculate_castle_prosperities_by_using_its_villages"),

     (store_add, ":fac_kingdom_6_plus_one", "fac_kingdom_6", 1),

     (try_for_range, ":faction_1", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
       (try_for_range, ":faction_2", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
         (store_relation, ":faction_relation", ":faction_1", ":faction_2"),
         (str_store_faction_name, s7, ":faction_1"),
         (str_store_faction_name, s8, ":faction_2"),
         (neq, ":faction_1", ":faction_2"),
         (assign, reg1, ":faction_relation"),
         #(display_message, "@{s7}-{s8}, relation is {reg1}"),
       (try_end),
     (try_end),          
   ]),
   
  (1,
   [   
     (try_begin),
       (eq, "$g_player_is_captive", 1),
       (neg|party_is_active, "$capturer_party"),
       (rest_for_hours, 0, 0, 0),
     (try_end),            
     
     (assign, ":village_no", "$next_center_will_be_fired"),
     (party_get_slot, ":is_there_already_fire", ":village_no", slot_village_smoke_added),
     (eq, ":is_there_already_fire", 0),
	 
	 
     (try_begin),
       (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),  
       (party_get_slot, ":last_nearby_fire_time", ":bound_center", slot_town_last_nearby_fire_time),
       (store_current_hours, ":cur_hours"),
	   
	   (try_begin),
		(eq, "$cheat_mode", 1),
		(is_between, ":village_no", centers_begin, centers_end),
		(is_between, ":bound_center", centers_begin, centers_end),
		(str_store_party_name, s4, ":village_no"),
		(str_store_party_name, s5, ":bound_center"),
		(store_current_hours, reg3),
        (party_get_slot, reg4, ":bound_center", slot_town_last_nearby_fire_time),
		(display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
	   (try_end),
	   
	   
       (eq, ":cur_hours", ":last_nearby_fire_time"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),       
     (else_try),  
       (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
       (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
       (party_clear_particle_systems, ":village_no"),
     (try_end),  
     

   ]),
   
  (24,
   [
   (val_sub, "$g_dont_give_fief_to_player_days", 1),
   (val_max, "$g_dont_give_fief_to_player_days", -1),
   (val_sub, "$g_dont_give_marshalship_to_player_days", 1),
   (val_max, "$g_dont_give_marshalship_to_player_days", -1),

   #this to correct string errors in games started in 1.104 or before
   (party_set_name, "p_steppe_bandit_spawn_point", "str_the_steppes"),
   (party_set_name, "p_taiga_bandit_spawn_point", "str_the_tundra"),
   (party_set_name, "p_forest_bandit_spawn_point", "str_the_forests"),
   (party_set_name, "p_mountain_bandit_spawn_point", "str_the_highlands"),
   (party_set_name, "p_sea_raider_spawn_point_1", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_2", "str_the_coast"),
   (party_set_name, "p_desert_bandit_spawn_point", "str_the_deserts"),

   
   #this to correct inappropriate home strings - Katrin to Uxkhal, Matheld to Fearichen
   (troop_set_slot, "trp_npc11", slot_troop_home, "p_town_7"),
   (troop_set_slot, "trp_npc8", slot_troop_home, "p_village_35"),
   
   (troop_set_slot, "trp_npc15", slot_troop_town_with_contacts, "p_town_20"), #durquba
   
   #this to correct linen production at villages of durquba 
   (party_set_slot, "p_village_93", slot_center_linen_looms, 0), #mazigh
   (party_set_slot, "p_village_94", slot_center_linen_looms, 0), #sekhtem
   (party_set_slot, "p_village_95", slot_center_linen_looms, 0), #qalyut
   (party_set_slot, "p_village_96", slot_center_linen_looms, 0), #tilimsal
   (party_set_slot, "p_village_97", slot_center_linen_looms, 0), #shibal zumr
   (party_set_slot, "p_village_102", slot_center_linen_looms, 0), #tamnuh
   (party_set_slot, "p_village_109", slot_center_linen_looms, 0), #habba

   (party_set_slot, "p_village_67", slot_center_fishing_fleet, 0), #Tebandra
   (party_set_slot, "p_village_5", slot_center_fishing_fleet, 15), #Kulum
   
   
   #The following scripts are to end quests which should have cancelled, but did not because of a bug
   (try_begin),
	(check_quest_active, "qst_formal_marriage_proposal"),
	(check_quest_failed, "qst_formal_marriage_proposal"),
    (call_script, "script_end_quest", "qst_formal_marriage_proposal"),
   (try_end),
   
   (try_begin),
	(check_quest_active, "qst_lend_companion"),
	(quest_get_slot, ":giver_troop", "qst_lend_companion", slot_quest_giver_troop),
	(store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
    (store_relation, ":faction_relation", ":giver_troop_faction", "$players_kingdom"),
    (this_or_next|lt, ":faction_relation", 0),
    (neg|is_between, ":giver_troop_faction", kingdoms_begin, kingdoms_end),
    (call_script, "script_abort_quest", "qst_lend_companion", 0),
   (try_end),


   
   (try_begin),
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(neq, "$players_kingdom", "fac_player_supporters_faction"),
    (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
    (val_add, "$g_player_days_as_marshal", 1),
   (else_try),
    (assign, "$g_player_days_as_marshal", 0),
   (try_end),
   
   (try_for_range, ":town", towns_begin, towns_end),
	(party_get_slot, ":days_to_completion", ":town", slot_center_player_enterprise_days_until_complete),
    (ge, ":days_to_completion", 1),
	(val_sub, ":days_to_completion", 1),
	(party_set_slot, ":town", slot_center_player_enterprise_days_until_complete, ":days_to_completion"), 
   (try_end),
    ]),
  (24,
   [
	  # Setting food bonuses in every 6 hours again and again because of a bug (we could not find its reason) which decreases especially slot_item_food_bonus slots of items to 0.
	  #Staples
      (item_set_slot, "itm_bread", slot_item_food_bonus, 8), #brought up from 4
      (item_set_slot, "itm_grain", slot_item_food_bonus, 2), #new - can be boiled as porridge
	  
	  #Fat sources - preserved
      (item_set_slot, "itm_smoked_fish", slot_item_food_bonus, 4),
      (item_set_slot, "itm_dried_meat", slot_item_food_bonus, 5),
      (item_set_slot, "itm_cheese", slot_item_food_bonus, 5),
      (item_set_slot, "itm_sausages", slot_item_food_bonus, 5),
      (item_set_slot, "itm_butter", slot_item_food_bonus, 4), #brought down from 8

	  #Fat sources - perishable
      (item_set_slot, "itm_chicken", slot_item_food_bonus, 8), #brought up from 7
      (item_set_slot, "itm_cattle_meat", slot_item_food_bonus, 7), #brought down from 7
      (item_set_slot, "itm_pork", slot_item_food_bonus, 6), #brought down from 6
	  
	  #Produce
      (item_set_slot, "itm_raw_olives", slot_item_food_bonus, 1),
      (item_set_slot, "itm_cabbages", slot_item_food_bonus, 2),
      (item_set_slot, "itm_raw_grapes", slot_item_food_bonus, 3),
      (item_set_slot, "itm_apples", slot_item_food_bonus, 4), #brought down from 5

	  #Sweet items
      (item_set_slot, "itm_raw_date_fruit", slot_item_food_bonus, 4), #brought down from 8
      (item_set_slot, "itm_honey", slot_item_food_bonus, 6), #brought down from 12
      
      (item_set_slot, "itm_wine", slot_item_food_bonus, 5),
      (item_set_slot, "itm_ale", slot_item_food_bonus, 4),
   ]),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
]
