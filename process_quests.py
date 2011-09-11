import process_common as pc
import process_operations as po
import module_quests

def process_entry(processor, txt_file, entry, index):
  txt_file.write("qst_%s %s %d %s \r\n" % (entry[0], pc.replace_spaces(entry[1]), entry[2], pc.replace_spaces(entry[3])))

export = po.make_export(data=module_quests.quests, data_name="quests", tag="qst",
    header_format="questsfile version 1\r\n%d\r\n", process_entry=process_entry)
