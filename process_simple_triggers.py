import process_operations as po
import module_simple_triggers

def process_entry(processor, txt_file, entry, index):
  output_list = ["%f " % entry[0]]
  output_list.extend(processor.process_block(entry[1], "#%d" % index))
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_simple_triggers.simple_triggers, data_name="simple_triggers",
    header_format="simple_triggers_file version 1\r\n%d\r\n", process_entry=process_entry)
