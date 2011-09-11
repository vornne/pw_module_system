import process_operations as po
import module_scripts
import module_generated_scripts

def process_entry(processor, txt_file, entry, index):
  output_list = ["%s -1\r\n" % entry[0]]
  output_list.extend(processor.process_block(entry[1], entry[0], check_can_fail=True))
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_scripts.scripts, data_name="scripts", tag="script",
    header_format="scriptsfile version 1\r\n%d\r\n", process_entry=process_entry)
