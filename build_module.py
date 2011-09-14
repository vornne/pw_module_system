#!/usr/bin/python -tt

import sys
import traceback
import argparse

parser = argparse.ArgumentParser(description="Build the Mount&Blade Warband module system.")
parser.add_argument("-i", "--write-ids", action="store_true", help="write ID_*.py files")
parser.add_argument("-d", "--build-data", action="store_true", help="build data *.txt files")
parser.add_argument("-t", "--show-backtrace", action="store_true", help="show full backtrace for errors")
group = parser.add_mutually_exclusive_group()
group.add_argument("-w", "--warnings-fatal", action="store_true", help="treat all warnings as fatal errors")
group.add_argument("-e", "--errors-non-fatal", action="store_true", help="treat all errors as non fatal")
args = parser.parse_args()

import process_common as pc
import process_operations as po

if args.warnings_fatal:
  pc.set_warnings_as_errors()
elif args.errors_non_fatal:
  pc.set_errors_non_fatal()

def exit():
  if args.show_backtrace:
    raise
  else:
    sys.exit(1)

from header_common import *
try:
  import module_strings
  import module_skills
  import module_music
  import module_animations
  import module_meshes
  import module_sounds
  import module_map_icons
  import module_factions
  import module_items
  import module_scenes
  import module_troops
  import module_particle_systems
  import module_scene_props
  import module_tableau_materials
  import module_presentations
  import module_party_templates
  import module_parties
  import module_quests
  import module_scripts
  import module_mission_templates
  import module_game_menus
  import module_info

  tags_data = [
    ("str", module_strings.strings, tag_string),
    ("skl", module_skills.skills, tag_skill),
    ("track", module_music.tracks, tag_track),
    ("anim", module_animations.animations, tag_animation),
    ("mesh", module_meshes.meshes, tag_mesh),
    ("snd", module_sounds.sounds, tag_sound),
    ("icon", module_map_icons.map_icons, tag_map_icon),
    ("fac", module_factions.factions, tag_faction),
    ("itm", module_items.items, tag_item),
    ("scn", module_scenes.scenes, tag_scene),
    ("trp", module_troops.troops, tag_troop),
    ("psys", module_particle_systems.particle_systems, tag_particle_sys),
    ("spr", module_scene_props.scene_props, tag_scene_prop),
    ("tableau", module_tableau_materials.tableaus, tag_tableau),
    ("prsnt", module_presentations.presentations, tag_presentation),
    ("pt", module_party_templates.party_templates, tag_party_tpl),
    ("p", module_parties.parties, tag_party),
    ("qst", module_quests.quests, tag_quest),
    ("script", module_scripts.scripts, tag_script),
    ("mt", module_mission_templates.mission_templates, tag_mission_tpl),
    ("mnu", module_game_menus.game_menus, tag_menu),
  ]

  id_map = po.IdentifierMap()
  for (tag, data, o) in tags_data:
    id_map.load_ids(tag, data, o << op_num_value_bits)

  global_variables = po.GlobalVariables()
  global_variables.load_old()

  quick_strings = po.QuickStrings()
  quick_strings.load_old()

  processor = po.Processor(global_variables, quick_strings, id_map, args.write_ids, args.show_backtrace)

  import process_strings
  process_strings.export(processor)
  import process_skills
  process_skills.export(processor)
  import process_music
  process_music.export(processor)
  import process_animations
  process_animations.export(processor)
  import process_meshes
  process_meshes.export(processor)
  import process_sounds
  process_sounds.export(processor)
  import process_skins
  process_skins.export(processor)
  import process_map_icons
  process_map_icons.export(processor)
  import process_factions
  process_factions.export(processor)
  import process_items
  process_items.export(processor)
  import process_scenes
  process_scenes.export(processor)
  import process_troops
  process_troops.export(processor)
  import process_particle_systems
  process_particle_systems.export(processor)
  import process_scene_props
  process_scene_props.export(processor)
  import process_tableau_materials
  process_tableau_materials.export(processor)
  import process_presentations
  process_presentations.export(processor)
  import process_party_templates
  process_party_templates.export(processor)
  import process_parties
  process_parties.export(processor)
  import process_quests
  process_quests.export(processor)
  import process_info_pages
  process_info_pages.export(processor)
  import process_scripts
  process_scripts.export(processor)
  import process_mission_templates
  process_mission_templates.export(processor)
  import process_game_menus
  process_game_menus.export(processor)
  import process_simple_triggers
  process_simple_triggers.export(processor)
  import process_triggers
  process_triggers.export(processor)
  import process_dialogs
  process_dialogs.export(processor)
  import process_postfx
  process_postfx.export(processor)

  if args.build_data:
    import os
    data_path = module_info.export_path("Data")
    if not os.path.isdir(data_path):
      os.mkdir(data_path)
    import module_flora_kinds
    module_flora_kinds.export(processor)
    import module_ground_specs
    module_ground_specs.export(processor)
    import module_skyboxes
    module_skyboxes.export(processor)

  global_variables.warn_unused(None)
  global_variables.write()
  quick_strings.write()

except pc.ModuleSystemError as e:
  print e
  exit()
except TypeError as e:
  msg = e.args[0]
  if "object is not callable" in msg or "indices must be integers, not" in msg:
    print "ERROR: missing comma in or near this line:"
    for line in traceback.format_exc().splitlines()[-3:-1]:
      print line
  else:
    raise
  exit()
except SyntaxError as e:
  print "ERROR: invalid syntax, probably missing or extra brackets or commas:"
  for line in traceback.format_exc().splitlines()[-4:-1]:
    print line
  exit()
