import process_operations as po
import module_presentations

def process_entry(processor, txt_file, entry, index):
  output_list = ["prsnt_%s %d %d " % (entry[0], entry[1], processor.process_id(entry[2], "mesh"))]
  output_list.extend(processor.process_triggers(entry[3], entry[0]))
  output_list.append("\r\n\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_presentations.presentations, data_name="presentations", tag="prsnt",
    header_format="presentationsfile version 1\r\n %d\r\n", process_entry=process_entry)
