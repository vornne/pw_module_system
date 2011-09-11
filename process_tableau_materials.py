import process_operations as po
import module_tableau_materials

def process_entry(processor, txt_file, entry, index):
  output_list = ["tab_%s %d %s %d %d %d %d %d %d" % entry[0:9]]
  output_list.extend(processor.process_block(entry[9], entry[0]))
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_tableau_materials.tableaus, data_name="tableau_materials",
    tag="tableau", header_format="%d\r\n", process_entry=process_entry)
