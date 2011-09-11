import process_common as pc
import process_operations as po
import module_skills

def process_entry(processor, txt_file, entry, index):
  txt_file.write("skl_%s %s %d %d %s\r\n" % (entry[0], pc.replace_spaces(entry[1]), entry[2], entry[3], pc.replace_spaces(entry[4])))

export = po.make_export(data=module_skills.skills, data_name="skills", tag="skl",
    header_format="%d\r\n", process_entry=process_entry)
