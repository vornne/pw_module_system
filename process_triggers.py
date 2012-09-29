import process_operations as po
import module_triggers

def process_entry(processor, txt_file, entry, index):
  output_list = ["%f %f %f " % entry[0:3]]
  name = "#%d" % index
  output_list.extend(processor.process_block(entry[3], name + " conditions"))
  output_list.extend(processor.process_block(entry[4], name + " consequences"))
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_triggers.triggers, data_name="triggers",
    header_format="triggersfile version 1\r\n%d\r\n", process_entry=process_entry)
