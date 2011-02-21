from module_constants import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick|imodbit_hardened
imodbits_armor  = imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_thick|imodbit_reinforced|imodbit_lordly
imodbits_plate  = imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_thick|imodbit_reinforced|imodbit_lordly
imodbits_polearm = imodbit_cracked|imodbit_bent|imodbit_balanced
imodbits_shield  = imodbit_cracked|imodbit_battered|imodbit_thick|imodbit_reinforced
imodbits_sword   = imodbit_rusty|imodbit_chipped|imodbit_balanced|imodbit_tempered
imodbits_sword_high   = imodbit_rusty|imodbit_chipped|imodbit_balanced|imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty|imodbit_chipped|imodbit_heavy
imodbits_mace   = imodbit_rusty|imodbit_chipped|imodbit_heavy
imodbits_pick   = imodbit_rusty|imodbit_chipped|imodbit_balanced|imodbit_heavy
imodbits_bow = imodbit_cracked|imodbit_bent|imodbit_strong|imodbit_masterwork
imodbits_crossbow = imodbit_cracked|imodbit_bent|imodbit_masterwork
imodbits_missile   = imodbit_bent|imodbit_large_bag
imodbits_thrown   = imodbit_bent|imodbit_heavy|imodbit_balanced|imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent|imodbit_balanced|imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy|imodbit_thick|imodbit_hardened|imodbit_reinforced
imodbits_bad    = imodbit_rusty|imodbit_chipped|imodbit_tattered|imodbit_ragged|imodbit_cracked|imodbit_bent

items = [
["no_item", "INVALID ITEM", [("invalid_item", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword,
 3, weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16, blunt)|thrust_damage(10, blunt), imodbits_none],

]
