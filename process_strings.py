import process_common as pc
import process_operations as po
import module_strings

def process_entry(processor, txt_file, entry, index):
  txt_file.write("str_%s %s\r\n" % (entry[0], pc.replace_spaces(entry[1])))

export = po.make_export(data=module_strings.strings, data_name="strings", tag="str",
    header_format="stringsfile version 1\r\n%d\r\n", process_entry=process_entry)
