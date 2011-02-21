import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
####################################################################################################################

def wp(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

reserved = 0
no_scene = 0

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,0, [], str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0, 0, [], 0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0, 0, [], 0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved, 0,[],0,0,0,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
]
