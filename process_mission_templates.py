import process_common as pc
import process_operations as po
from header_triggers import *
import module_mission_templates

def process_entry(processor, txt_file, entry, index):
  spawn_records = entry[4]
  output_list = ["mst_%s %s %d  %d\r\n%s \r\n\r\n%d " % (entry[0], entry[0], entry[1], entry[2],
      pc.replace_spaces(entry[3]), po.block_len(spawn_records))]
  for spawn_record in spawn_records:
    item_override_len = po.block_len(spawn_record[5])
    if item_override_len > 8:
      pc.ERROR("the maximum number of spawn item overrides is 8")
    output_list.append("%d %d %d %d %d %d  "% (spawn_record[0:5] + (item_override_len,)))
    output_list.extend("%d " % processor.process_id(item, "itm") for item in spawn_record[5])
    output_list.append("\r\n")
  output_list.append("%d\r\n" % po.block_len(entry[5]))
  txt_file.write("".join(output_list))
  for i, trigger in enumerate(entry[5]):
    txt_file.write("%f %f %f " % trigger[0:3])
    if trigger[0] < 0.0:
      name = "%s: %s" % (entry[0], get_trigger_name(trigger[0]))
    else:
      name = "%s: trigger #%d" % (entry[0], i)
    txt_file.write("".join(processor.process_block(trigger[3], name + " conditions")))
    txt_file.write("".join(processor.process_block(trigger[4], name + " consequences")))
    txt_file.write("\r\n")
  txt_file.write("\r\n\r\n")

export = po.make_export(data=module_mission_templates.mission_templates, data_name="mission_templates", tag="mt",
    header_format="missionsfile version 1\r\n %d\r\n", process_entry=process_entry)
