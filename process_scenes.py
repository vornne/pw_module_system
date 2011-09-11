import process_common as pc
import process_operations as po
import module_scenes

def process_entry(processor, txt_file, entry, index):
  passages = entry[8]
  txt_file.write("scn_%s %s %d %s %s %f %f %f %f %f %s \r\n  %d " % (entry[0], pc.replace_spaces(entry[0]), entry[1],
      entry[2], entry[3], entry[4][0], entry[4][1], entry[5][0], entry[5][1], entry[6], entry[7], po.block_len(passages)))
  output_list = [" %d " % (100000 if p == "exit" else 0 if p == "" else processor.identifier_map.get_id("scn", p)) for p in passages]
  chest_troops = entry[9]
  output_list.append("\r\n  %d " % po.block_len(chest_troops))
  output_list.extend(" %d " % processor.identifier_map.get_id("trp", troop) for troop in chest_troops)
  output_list.append("\r\n %s \r\n" % entry[10] if len(entry) > 10 else "\r\n 0 \r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_scenes.scenes, data_name="scenes", tag="scn",
    header_format="scenesfile version 1\r\n %d\r\n", process_entry=process_entry)
