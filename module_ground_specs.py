####################################################################################################################
# Ground specs are dependent on the module system and the engine c++ code; you cannot add new ground types.
# Make sure you have updated your module's header_ground_types.py file.
#
# Each ground spec contains the following fields:
# 1) Spec name.
# 2) Flags.
# 3) Material.
# 4) UV scale.
# 5) Multitexture material.
# 6) Tuple containing red, green, blue values used with gtf_has_color
####################################################################################################################

gtf_overlay   = 0x00000001 # depreciated
gtf_dusty     = 0x00000002 # controls dustiness of the ground for foot dust particle systems
gtf_has_color = 0x00000004 # you can overwrite the ambient color of the ground spec (default: 0.61, 0.72, 0.15)

ground_specs = [
  ("gray_stone",gtf_has_color,"stone_a",4.0,"none",(0.7,0.7,0.7)),
  ("brown_stone",gtf_has_color,"patch_rock",2,"none",(0.7,0.7,0.7)),
  ("turf",gtf_overlay|gtf_has_color,"grassy_ground",3.3,"ground_earth_under_grass",(0.42,0.59,0.17)),
  ("steppe",gtf_overlay|gtf_dusty|gtf_has_color,"ground_steppe",3.0,"ground_earth_under_steppe",(0.85,0.73,0.36)),
  ("snow",gtf_overlay|gtf_has_color,"snow",5.2,"none",(1.4,1.4,1.4)),
  ("earth",gtf_overlay|gtf_dusty|gtf_has_color,"ground_earth",4.5,"none",(0.7,0.5,0.23)),
  ("desert",gtf_overlay|gtf_dusty|gtf_has_color,"ground_desert", 2.5,"none",(1.4,1.2,0.4)),
  ("forest",gtf_overlay|gtf_has_color,"ground_forest",4.2,"ground_forest_under_grass",(0.6,0.42,0.28)),
  ("pebbles",gtf_overlay|gtf_has_color,"pebbles",4.1,"none",(0.7,0.7,0.7)),
  ("village",gtf_overlay|gtf_has_color,"ground_village",7.0,"none",(1.0,0.9,0.59)),
  ("path",gtf_overlay|gtf_dusty|gtf_has_color,"ground_path",6.0,"none",(0.93,0.68,0.34)),
]

import process_operations as po

def save_python_header(processor, txt_file):
  if not processor.write_id:
    return
  with open("header_ground_types.py", "w") as py_file:
    for i, entry in enumerate(ground_specs):
      py_file.write("ground_%s = %d\n" % (entry[0], i))

def process_entry(processor, txt_file, entry, index):
  txt_file.write(" %s %d %s %f %s" % entry[0:5])
  if entry[1] & gtf_has_color and po.block_len(entry[5]) >= 3:
    txt_file.write(" %f %f %f" % entry[5])
  txt_file.write("\r\n")

export = po.make_export(data=ground_specs, data_name="ground_specs", file_name="Data/ground_specs",
    process_entry=process_entry, process_list=save_python_header)
