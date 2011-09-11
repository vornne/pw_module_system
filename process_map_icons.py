import process_operations as po
import module_map_icons

def process_entry(processor, txt_file, entry, index):
  entry_len = len(entry)
  output_list = ["%s %d %s %f %d " % (entry[0], entry[1], entry[2], entry[3], processor.process_id(entry[4], "snd"))]
  triggers = []
  if entry_len >= 8:
    output_list.append("%f %f %f " % entry[5:8])
    if entry_len > 8:
      triggers = entry[8]
  else:
    output_list.append("0 0 0 ")
    if entry_len > 5:
      triggers = entry[5]
  output_list.extend(processor.process_triggers(triggers, entry[0]))
  output_list.append("\r\n\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_map_icons.map_icons, data_name="map_icons", tag="icon",
    header_format="map_icons_file version 1\r\n%d\r\n", process_entry=process_entry)
