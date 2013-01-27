from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track.
#  3) Track flags. See header_music.py for a list of available flags.
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags.
####################################################################################################################

# You must add mtf_module_track flag to the flags of the tracks located under module directory.

# Changed meanings of the different flags in PW:

# mtf_sit_victorious: after your faction captured a castle
# mtf_sit_encounter_hostile: after your faction lost a castle
# mtf_sit_fight: when many human agents have been recently killed nearby
# mtf_sit_killed: after the player was killed
# mtf_sit_ambushed: when in a faction hostile to any other, while near a friendly castle
# mtf_sit_siege: when in a faction hostile to any other, while near an enemy castle
# mtf_sit_tavern: when in a faction at peace with everyone, while near a friendly castle; or when near a tavern processing scene prop
# mtf_sit_town: when in a faction at peace with everyone, while near a castle owned by another faction; or somewhere not directly on terrain (probably a town)
# mtf_sit_town_infiltrate: after being outlawed, and when in town with a lock pick or poison dagger
# mtf_sit_travel: for all other situations, mostly when in alone in the countryside

# mtf_culture_1: as a commoner
# mtf_culture_2: as an outlaw
# mtf_culture_3: as a member of a faction

tracks = [
 ("ambushed_by_neutral", "ambushed_by_neutral.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_khergit", "ambushed_by_khergit.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_nord", "ambushed_by_nord.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_rhodok", "ambushed_by_rhodok.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_swadian", "ambushed_by_swadian.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_vaegir", "ambushed_by_vaegir.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("ambushed_by_sarranid", "middle_eastern_action.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight),
 ("arena_1", "arena_1.ogg", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
 ("armorer", "armorer.ogg", mtf_sit_town, mtf_sit_tavern|mtf_sit_travel),
 ("calm_night_2", "calm_night_2.ogg", mtf_sit_travel|mtf_sit_night, mtf_sit_town|mtf_sit_tavern),
 ("captured", "capture.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("coronation", "coronation.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("crazy_battle_music", "crazy_battle_music.ogg", mtf_sit_fight|mtf_sit_siege, mtf_sit_ambushed),
 ("defeated_by_neutral", "defeated_by_neutral.ogg", mtf_sit_encounter_hostile|mtf_persist_until_finished, 0),
 ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_sit_encounter_hostile|mtf_persist_until_finished, 0),
 ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_sit_encounter_hostile|mtf_persist_until_finished, 0),
 ("empty_village", "empty_village.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished, 0),
 ("enter_the_juggernaut", "enter_the_juggernaut.ogg", mtf_sit_fight|mtf_sit_siege, mtf_sit_ambushed),
 ("escape", "escape.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("fight_1", "fight_1.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_2", "fight_2.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_3", "fight_3.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_4", "percussion_battery.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_khergit", "fight_as_khergit.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_nord", "fight_as_nord.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_rhodok", "fight_as_rhodok.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_as_vaegir", "fight_as_vaegir.ogg", mtf_culture_3|mtf_sit_fight, mtf_culture_all|mtf_sit_siege|mtf_sit_ambushed),
 ("fight_while_mounted_1", "fight_while_mounted_1.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("fight_while_mounted_2", "fight_while_mounted_2.ogg", mtf_sit_fight, mtf_sit_siege|mtf_sit_ambushed),
 ("hearth_and_brotherhood", "hearth_and_brotherhood.ogg", mtf_sit_night|mtf_sit_travel, mtf_sit_town),
 ("infiltration_khergit", "infiltration_khergit.ogg", mtf_sit_town_infiltrate, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_fight),
 ("killed_by_khergit", "killed_by_khergit.ogg", mtf_culture_3|mtf_sit_killed|mtf_persist_until_finished, 0),
 ("killed_by_swadian", "killed_by_swadian.ogg", mtf_culture_3|mtf_sit_killed|mtf_persist_until_finished, 0),
 ("lords_hall_khergit", "lords_hall_khergit.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_nord", "lords_hall_nord.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_swadian", "lords_hall_swadian.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_rhodok", "lords_hall_rhodok.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("lords_hall_vaegir", "lords_hall_vaegir.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
 ("mounted_snow_terrain_calm", "mounted_snow_terrain_calm.ogg", mtf_sit_travel, mtf_sit_night|mtf_sit_town|mtf_sit_tavern),
 ("neutral_infiltration", "neutral_infiltration.ogg", mtf_sit_town_infiltrate, mtf_sit_travel|mtf_sit_town|mtf_sit_tavern|mtf_sit_fight),
 ("outdoor_beautiful_land", "outdoor_beautiful_land.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern),
 ("retreat", "retreat.ogg", mtf_sit_killed|mtf_persist_until_finished, 0),
 ("siege_attempt", "siege_attempt.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_ambushed),
 ("tavern_1", "tavern_1.ogg", mtf_sit_tavern, mtf_sit_town|mtf_sit_travel),
 ("tavern_2", "tavern_2.ogg", mtf_sit_tavern, mtf_sit_town|mtf_sit_travel),
 ("town_khergit", "town_khergit.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_neutral", "town_neutral.ogg", mtf_sit_town, mtf_sit_tavern|mtf_sit_travel),
 ("town_nord", "town_nord.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_rhodok", "town_rhodok.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_swadian", "town_swadian.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("town_vaegir", "town_vaegir.ogg", mtf_culture_3|mtf_sit_town, mtf_culture_all|mtf_sit_tavern|mtf_sit_travel),
 ("tragic_village", "tragic_village.ogg", mtf_culture_1|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_khergit", "travel_khergit.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_neutral", "travel_neutral.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_nord",    "travel_nord.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_rhodok",  "travel_rhodok.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_swadian", "travel_swadian.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_vaegir",  "travel_vaegir.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("travel_sarranid",  "middle_eastern_travel.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("uncertain_homestead", "uncertain_homestead.ogg", mtf_culture_1|mtf_culture_2|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("victorious_evil", "victorious_evil.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_swadian", "victorious_swadian.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_vaegir", "victorious_vaegir.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_sit_victorious|mtf_persist_until_finished, 0),
 ("warband_action", "warband_action.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
 ("warband_siege", "warband_siege.ogg", mtf_culture_3|mtf_sit_travel, mtf_culture_all|mtf_sit_tavern|mtf_sit_town),
 ("wedding", "wedding.ogg", mtf_culture_3|mtf_sit_tavern, mtf_culture_all|mtf_sit_town|mtf_sit_travel),
]
