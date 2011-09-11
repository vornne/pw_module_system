import process_operations as po
from header_scene_props import *
import module_scene_props

def process_entry(processor, txt_file, entry, index):
  output_list = ["spr_%s %d %d %s %s " % (entry[0], entry[1], get_spr_hit_points(entry[1]), entry[2], entry[3])]
  output_list.extend(processor.process_triggers(entry[4], entry[0]))
  output_list.append("\r\n\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_scene_props.scene_props, data_name="scene_props", tag="spr",
    header_format="scene_propsfile version 1\r\n %d\r\n", process_entry=process_entry)
