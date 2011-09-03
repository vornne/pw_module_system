#!/bin/bash

MODULE_PATH=`grep -e "^export_dir = " module_info.py | cut -d '"' -f 2`
cd "${MODULE_PATH}"
CHANGED_FILES=`git di --name-only`
FILE_NAMES="
  actions.txt
  conversation.txt
  dialog_states.txt
  factions.txt
  info_pages.txt
  item_kinds1.txt
  map_icons.txt
  menus.txt
  meshes.txt
  mission_templates.txt
  music.txt
  particle_systems.txt
  parties.txt
  party_templates.txt
  postfx.txt
  presentations.txt
  quests.txt
  quick_strings.txt
  scene_props.txt
  scenes.txt
  scripts.txt
  simple_triggers.txt
  skills.txt
  skins.txt
  sounds.txt
  strings.txt
  tableau_materials.txt
  triggers.txt
  troops.txt
  variable_uses.txt
  variables.txt"

for TEXTFILE in ${CHANGED_FILES}; do
  if echo "${FILE_NAMES}" | grep -q "${TEXTFILE}" > /dev/null 2>&1; then
    sed -i -e 's/$/\r/' "./${TEXTFILE}"
  fi
done
