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

item_class = -100.0

def init_heraldic_item(tableau):
  return [(ti_on_init_item,
   [(store_trigger_param_1, ":agent_id"),
    (store_trigger_param_2, ":troop_id"),
    (call_script, "script_item_set_banner", tableau, ":agent_id", ":troop_id"),
    ])]

items = [
["no_item", "INVALID ITEM", [("invalid_item", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger,
 0, weight(1)|spd_rtng(1)|weapon_length(1)|swing_damage(1, blunt)|thrust_damage(1, blunt), imodbits_none],
["no_head", "INVALID HEAD", [("invalid_item", 0)], itp_type_head_armor, 0,
 0, weight(1)|head_armor(1)|difficulty(0), imodbits_none],
["no_body", "INVALID BODY", [("invalid_item", 0)], itp_type_body_armor, 0,
 0, weight(1)|body_armor(1)|difficulty(0), imodbits_none],
["no_foot", "INVALID FOOT", [("invalid_item", 0)], itp_type_foot_armor, 0,
 0, weight(1)|leg_armor(1)|difficulty(0), imodbits_none],
["no_hand", "INVALID HAND", [("invalid_item", 0)], itp_type_hand_armor, 0,
 0, weight(1)|body_armor(1)|difficulty(0), imodbits_none],
["no_horse", "INVALID HORSE", [("invalid_item", 0)], itp_type_horse, 0,
 0, hit_points(1)|body_armor(1)|difficulty(0)|horse_speed(10)|horse_maneuver(40)|horse_charge(1)|horse_scale(1), imodbits_none],

["straw_hat", "Straw Hat", [("straw_hat_new", 0)], itp_type_head_armor, 0,
 29, weight(1)|head_armor(2)|difficulty(0), imodbits_cloth],
["head_wrappings", "Head Wrapping", [("head_wrapping", 0)], itp_type_head_armor|itp_fit_to_head, 0,
 26, weight(0.25)|head_armor(3), imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick],
["headcloth", "Headcloth", [("headcloth_a_new", 0)], itp_type_head_armor, 0,
 80, weight(0.5)|head_armor(4)|difficulty(0), imodbits_cloth],
["woolen_cap", "Woolen Cap", [("woolen_cap_new", 0)], itp_type_head_armor, 0,
 62, weight(1)|head_armor(6)|difficulty(0), imodbits_cloth],
["arming_cap", "Arming Cap", [("arming_cap_a_new", 0)], itp_type_head_armor, 0,
 78, weight(1)|head_armor(7)|difficulty(0), imodbits_cloth],
["woolen_hood", "Woolen Hood", [("woolen_hood", 0)], itp_type_head_armor, 0,
 120, weight(1)|head_armor(8)|difficulty(0), imodbits_cloth],
["fur_hat", "Fur Hat", [("fur_hat_a_new", 0)], itp_type_head_armor, 0,
 110, weight(0.5)|head_armor(8)|difficulty(0), imodbits_cloth],
["felt_hat", "Felt Hat", [("felt_hat_a_new", 0)], itp_type_head_armor, 0,
 74, weight(1)|head_armor(8)|difficulty(0), imodbits_cloth],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new", 0)], itp_type_head_armor, 0,
 85, weight(1)|head_armor(8)|difficulty(0), imodbits_cloth],
["leather_cap", "Leather Cap", [("leather_cap_a_new", 0)], itp_type_head_armor, 0,
 106, weight(1)|head_armor(10)|difficulty(0), imodbits_cloth],
["common_hood", "Hood", [("hood_new", 0)], itp_type_head_armor, 0,
 129, weight(1)|head_armor(10)|difficulty(0), imodbits_cloth],
["hood_b", "Hood", [("hood_b", 0)], itp_type_head_armor, 0,
 116, weight(1)|head_armor(10)|difficulty(0), imodbits_cloth],
["hood_c", "Hood", [("hood_c", 0)], itp_type_head_armor, 0,
 124, weight(1)|head_armor(10)|difficulty(0), imodbits_cloth],
["hood_d", "Hood", [("hood_d", 0)], itp_type_head_armor, 0,
 131, weight(1)|head_armor(10)|difficulty(0), imodbits_cloth],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new", 0)], itp_type_head_armor, 0,
 132, weight(0.75)|head_armor(10)|difficulty(0), imodbits_cloth],
["padded_coif", "Padded Coif", [("padded_coif_a_new", 0)], itp_type_head_armor, 0,
 116, weight(1)|head_armor(11)|difficulty(0), imodbits_cloth],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new", 0)], itp_type_head_armor, 0,
 145, weight(1)|head_armor(16)|difficulty(0), imodbits_cloth],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_type_head_armor, 0,
 60, weight(1.0)|head_armor(20)|difficulty(7), imodbits_plate],

["shirt", "Shirt", [("shirt", 0)], itp_type_body_armor|itp_covers_legs, 0,
 45, weight(1)|body_armor(5)|difficulty(0), imodbits_cloth],
["linen_tunic", "Linen Tunic", [("shirt_a", 0)], itp_type_body_armor|itp_covers_legs, 0,
 60, weight(1)|body_armor(6)|leg_armor(1)|difficulty(0), imodbits_cloth],
["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_type_body_armor|itp_covers_legs, 0,
 122, weight(1)|body_armor(6)|leg_armor(2)|difficulty(0), imodbits_cloth],
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)], itp_type_body_armor|itp_covers_legs, 0,
 193, weight(2)|body_armor(9)|leg_armor(1)|difficulty(0), imodbits_cloth],
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b", 0)], itp_type_body_armor|itp_covers_legs, 0,
 220, weight(5)|body_armor(10)|difficulty(0), imodbits_cloth],
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a", 0)], itp_type_body_armor|itp_covers_legs, 0,
 87, weight(2)|body_armor(11)|leg_armor(6)|difficulty(0), imodbits_cloth],
["leather_apron", "Leather Apron", [("leather_apron", 0)], itp_type_body_armor|itp_covers_legs, 0,
 95, weight(3)|body_armor(12)|leg_armor(7)|difficulty(0), imodbits_cloth],
["fur_coat", "Fur Coat", [("fur_coat", 0)], itp_type_body_armor|itp_covers_legs, 0,
 357, weight(6)|body_armor(13)|leg_armor(6)|difficulty(0), imodbits_armor],
["tabard", "Tabard", [("tabard_b", 0)], itp_type_body_armor|itp_covers_legs, 0,
 230, weight(3)|body_armor(14)|leg_armor(6)|difficulty(0), imodbits_cloth],
["khergit_armor", "Khergit Armor", [("khergit_armor_new", 0)], itp_type_body_armor|itp_covers_legs, 0,
 380, weight(2)|body_armor(14)|difficulty(0), imodbits_cloth],
["leather_vest", "Leather Vest", [("leather_vest_a", 0)], itp_type_body_armor|itp_covers_legs, 0,
 377, weight(4)|body_armor(15)|leg_armor(7)|difficulty(0), imodbits_cloth],
["leather_jacket", "Leather Jacket", [("leather_jacket_new", 0)], itp_type_body_armor|itp_covers_legs, 0,
 400, weight(3)|body_armor(15)|difficulty(0), imodbits_cloth],
["nomad_vest", "Nomad Vest", [("nomad_vest_new", 0)], itp_type_body_armor|itp_covers_legs, 0,
 360, weight(7)|body_armor(22)|leg_armor(8)|difficulty(0), imodbits_cloth],
["nomad_armor", "Nomad Armor", [("nomad_armor_new", 0)], itp_type_body_armor|itp_covers_legs, 0,
 550, weight(2)|body_armor(24)|difficulty(0), imodbits_cloth],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new", 0)], itp_type_body_armor|itp_covers_legs, 0,
 520, weight(14)|body_armor(30)|leg_armor(10)|difficulty(6), imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf", 0)], itp_type_body_armor|itp_covers_legs, 0,
 1320, weight(4)|body_armor(24)|leg_armor(10)|difficulty(9), imodbits_cloth],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new", 0)], itp_type_body_armor|itp_covers_legs, 0,
 1348, weight(4)|body_armor(25)|leg_armor(12)|difficulty(9), imodbits_cloth],
["light_heraldic_mail", "Light Heraldic Mail", [("heraldic_armor_new_c",0)], itp_type_body_armor|itp_covers_legs, 0,
 3130, weight(12)|body_armor(30)|leg_armor(5)|difficulty(9), imodbits_armor, init_heraldic_item("tableau_heraldic_armor_c")],
["heraldic_mail_with_tunic", "Heraldic Mail with Tunic", [("heraldic_armor_new_b",0)], itp_type_body_armor|itp_covers_legs, 0,
 5045, weight(15)|body_armor(35)|leg_armor(8)|difficulty(10), imodbits_armor, init_heraldic_item("tableau_heraldic_armor_b")],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_type_body_armor|itp_covers_legs, 0,
 6970, weight(20)|body_armor(40)|leg_armor(10)|difficulty(12), imodbits_armor, init_heraldic_item("tableau_heraldic_armor_d")],
["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor|itp_covers_legs, 0,
 10400, weight(25)|body_armor(45)|leg_armor(15)|difficulty(15), imodbits_armor, init_heraldic_item("tableau_heraldic_armor_a")],

["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 30, weight(1)|leg_armor(3)|difficulty(0), imodbits_cloth],
["woolen_hose", "Woolen Hose", [("woolen_hose_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 60, weight(1)|leg_armor(4)|difficulty(0), imodbits_cloth],
["blue_hose", "Blue Hose", [("blue_hose_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 110, weight(1)|leg_armor(5)|difficulty(0), imodbits_cloth],
["hunter_boots", "Hunter Boots", [("hunter_boots_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 190, weight(1.25)|leg_armor(9)|difficulty(0), imodbits_cloth],
["hide_boots", "Hide Boots", [("hide_boots_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 240, weight(1)|leg_armor(10)|difficulty(0), imodbits_cloth],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 270, weight(1)|leg_armor(12)|difficulty(0), imodbits_cloth],
["nomad_boots", "Nomad Boots", [("nomad_boots_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 310, weight(1.25)|leg_armor(14)|difficulty(0), imodbits_cloth],
["leather_boots", "Leather Boots", [("leather_boots_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,
 400, weight(1.25)|leg_armor(16)|difficulty(0), imodbits_cloth],

["leather_gloves", "Leather Gloves", [("leather_gloves_L",0)], itp_type_hand_armor, 0,
 545, weight(0.25)|body_armor(2)|difficulty(0), imodbits_cloth],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_type_hand_armor, 0,
 2303, weight(0.75)|body_armor(5)|difficulty(9), imodbits_armor],

["club", "Club", [("club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar|itcf_carry_mace_left_hip,
 35, weight(2.5)|difficulty(0)|spd_rtng(92)|weapon_length(70)|swing_damage(10, blunt)|thrust_damage(0, pierce), imodbits_none],
["old_knife", "Old Knife", [("peasant_knife",0)], itp_type_one_handed_wpn|itp_primary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
 78, weight(0.5)|difficulty(0)|spd_rtng(100)|weapon_length(43)|swing_damage(12, cut)|thrust_damage(7, pierce), imodbits_sword],
["crude_spear", "Crude Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 374 , weight(2.0)|difficulty(6)|spd_rtng(92)|weapon_length(120)|swing_damage(6, cut)|thrust_damage(22, pierce), imodbits_polearm],
["blunt_falchion", "Blunt Falchion", [("falchion",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 314, weight(2.5)|difficulty(5)|spd_rtng(95)|weapon_length(72)|swing_damage(23, cut)|thrust_damage(0, pierce), imodbits_sword],
["rusty_sword", "Rusty Sword", [("sword_rusty_a",0),("sword_rusty_a_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 321 , weight(1.5)|difficulty(5)|spd_rtng(97)|weapon_length(95)|swing_damage(20, cut)|thrust_damage(15, pierce), imodbits_sword],
["worn_sword", "Worn Sword", [("sword_norman_rusty",0),("sword_norman_rusty_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 355, weight(1.25)|difficulty(5)|spd_rtng(98)|weapon_length(91)|swing_damage(22, cut)|thrust_damage(16, pierce), imodbits_sword],
["bent_lance", "Bent Lance", [("spear",0)], itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear|itcf_carry_spear,
 364 , weight(4.5)|difficulty(7)|spd_rtng(87)|weapon_length(156)|swing_damage(0, cut)|thrust_damage(17, pierce), imodbits_polearm],
["falchion", "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 635, weight(2.5)|difficulty(5)|spd_rtng(96)|weapon_length(73)|swing_damage(30, cut)|thrust_damage(0, pierce), imodbits_sword],
["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 763, weight(1.5)|difficulty(5)|spd_rtng(99)|weapon_length(95)|swing_damage(27, cut)|thrust_damage(22, pierce), imodbits_sword_high],
["curved_sword", "Curved Sword", [("khergit_sword",0),("khergit_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 954, weight(1.25)|difficulty(8)|spd_rtng(97)|weapon_length(99)|swing_damage(25, cut)|thrust_damage(14, pierce), imodbits_sword],
["sword_two_handed_a", "Great Sword", [("sword_two_handed_a", 0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 4134, weight(2.75)|difficulty(10)|spd_rtng(96)|weapon_length(120)|swing_damage(42, cut)|thrust_damage(29, pierce), imodbits_sword_high],

["crude_bow", "Crude Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back,
 260, weight(1)|difficulty(1)|spd_rtng(82)|shoot_speed(42)|thrust_damage(10, pierce), imodbits_bow],
["bent_arrows", "Bent Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back,
 61, weight(3)|weapon_length(95)|thrust_damage(0, pierce)|max_ammo(10), imodbits_missile],
["flimsy_crossbow", "Flimsy Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_crossbow|itcf_carry_crossbow_back,
 284, weight(3)|difficulty(9)|spd_rtng(35)|shoot_speed(57)|thrust_damage(20, pierce)|max_ammo(1), imodbits_crossbow],
["crude_bolts","Crude Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical,
 47, weight(2.25)|weapon_length(55)|max_ammo(8), imodbits_missile],
["hunting_bow", "Hunting Bow", [("hunting_bow", 0), ("hunting_bow_carry", ixmesh_carry)], itp_type_bow|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_shoot_bow|itcf_carry_bow_back,
 260, weight(1)|difficulty(1)|spd_rtng(100)|shoot_speed(52)|thrust_damage(15, pierce), imodbits_bow],
["arrows", "Arrows", [("arrow", 0), ("flying_missile", ixmesh_flying_ammo), ("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back,
 72, weight(3)|weapon_length(95)|thrust_damage(1, pierce)|max_ammo(30), imodbits_missile],

["old_shield", "Old Shield", [("shield_heater_c",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 577, weight(3.5)|hit_points(210)|body_armor(2)|spd_rtng(70)|shield_width(50), imodbits_shield],
["steel_shield", "Steel Shield", [("shield_dragon", 0)], itp_type_shield, itcf_carry_round_shield,
 2120, weight(4)|difficulty(1)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40), imodbits_shield],

["cart_horse", "Cart Horse", [("sumpter_horse",0)], itp_type_horse, 0,
 5100, hit_points(150)|body_armor(10)|difficulty(1)|horse_speed(25)|horse_maneuver(20)|horse_charge(20)|horse_scale(120), imodbits_none],

["stick", "Stick", [("wooden_stick",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee, itcf_throw_axe|itcf_carry_quiver_back,
 23, weight(5)|spd_rtng(90)|shoot_speed(8)|thrust_damage(1,blunt)|max_ammo(1)|weapon_length(63), imodbits_none, [(item_class, item_class_wood, 100)]],
["stick_melee", "Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_quiver_back,
 23, weight(5)|spd_rtng(90)|swing_damage(5,blunt)|weapon_length(63), imodbits_none, [(item_class, item_class_wood, 100)]],
["branch", "Branch", [("pw_branch_a",0),("pw_branch_b",imodbit_cracked),("pw_branch_c",imodbit_bent)], itp_type_polearm|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_thrust_polearm|itcf_overswing_polearm|itcf_carry_spear,
 54, weight(25)|spd_rtng(30)|weapon_length(250)|swing_damage(20,blunt)|thrust_damage(10,blunt), imodbit_cracked|imodbit_bent, [(item_class, item_class_wood, 500)]],
["wood_pole", "Wooden Pole", [("pw_wood_pole",0)], itp_type_polearm|itp_primary|itp_two_handed|itp_cant_use_on_horseback, itcf_thrust_polearm|itcf_overswing_polearm|itcf_carry_spear,
 85, weight(15)|spd_rtng(70)|weapon_length(150)|swing_damage(20,blunt)|thrust_damage(10,blunt), imodbits_none, [(item_class, item_class_wood, 400)]],
["wood_block", "Wood Block", [("pw_wood_block",0)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_sword_back,
 74, weight(30)|spd_rtng(50)|weapon_length(32)|swing_damage(5,blunt)|thrust_damage(5,blunt), imodbits_none, [(item_class, item_class_wood, 800)]],
["board", "Board", [("pw_board",0)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_sword_back,
 103, weight(10)|spd_rtng(80)|weapon_length(50)|swing_damage(10,blunt)|thrust_damage(10,blunt), imodbits_none, [(item_class, item_class_wood, 200)]],
["iron_bar", "Short Iron Bar", [("pw_iron_bar",0)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_sword_back,
 320, weight(35)|spd_rtng(70)|swing_damage(10,blunt)|thrust_damage(10,blunt)|weapon_length(17), imodbits_none, [(item_class, item_class_iron, 100)]],
["iron_bar_med", "Iron Bar", [("pw_iron_bar_med",0)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_sword_back,
 640, weight(50)|spd_rtng(60)|swing_damage(10,blunt)|thrust_damage(10,blunt)|weapon_length(35), imodbits_none, [(item_class, item_class_iron, 200)]],
["iron_bar_long", "Long Iron Bar", [("pw_iron_bar_long",0)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_sword_back,
 1280, weight(100)|spd_rtng(50)|swing_damage(10,blunt)|thrust_damage(10,blunt)|weapon_length(53), imodbits_none, [(item_class, item_class_iron, 400)]],

["woodcutter_axe", "Woodcutter's Axe", [("pw_wood_axe",0)], itp_type_two_handed_wpn|itp_two_handed|itp_bonus_against_shield|itp_primary|itp_wooden_parry|itp_unbalanced|itp_cant_use_on_horseback, itc_nodachi|itcf_carry_axe_back,
 245, weight(4)|spd_rtng(80)|weapon_length(72)|swing_damage(20,cut)|thrust_damage(0,pierce), imodbits_none, [(item_class, item_class_wood_cutting)]],
["mining_pick", "Mining Pick", [("pw_mining_pick",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_unbalanced|itp_cant_use_on_horseback, itc_parry_polearm|itcf_overswing_polearm|itcf_carry_axe_back,
 423, weight(5)|spd_rtng(70)|weapon_length(100)|swing_damage(30,pierce)|thrust_damage(0,pierce), imodbits_none, [(item_class, item_class_mining)]],
["repair_hammer", "Repair Hammer", [("pw_repair_hammer",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_bow_back,
 634, weight(3)|spd_rtng(92)|weapon_length(120)|swing_damage(5,blunt)|thrust_damage(0,pierce), imodbits_none, [(item_class, item_class_repair)]],

["test_horse", "Test Horse", [("giant_horse",0)], itp_type_horse, 0,
 0, hit_points(500)|body_armor(100)|difficulty(0)|horse_speed(400)|horse_maneuver(100)|horse_charge(50)|horse_scale(130), imodbit_spirited],

["all_items_end", "all_items_end", [("shield_round_a", 0)], 0, 0, 1, 0, 0],
]

item_class_list = []
def fill_item_class_list():
  for item_id, item in enumerate(items):
    if len(item) <= 8:
      continue
    trigger_list = item[8]
    for i, trigger in enumerate(trigger_list):
      if trigger[0] == item_class:
        list_entry = [item_id]
        list_entry.extend(trigger[1:])
        item_class_list.append(list_entry)
        trigger_list.pop(i)
        break
fill_item_class_list()
