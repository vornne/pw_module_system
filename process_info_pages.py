import process_common as pc
import process_operations as po
import module_info_pages

def process_entry(processor, txt_file, entry, index):
  txt_file.write("ip_%s %s %s\r\n" % (entry[0], pc.replace_spaces(entry[1]), pc.replace_spaces(entry[2])))

export = po.make_export(data=module_info_pages.info_pages, data_name="info_pages", tag="info",
    header_format="infopagesfile version 1\r\n%d\r\n", process_entry=process_entry)
