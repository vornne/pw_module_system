import process_common as pc
import process_operations as po
import module_meshes

def process_entry(processor, txt_file, entry, index):
  txt_file.write("mesh_%s %d %s %f %f %f %f %f %f %f %f %f\r\n" % (entry[0:2] +
      (pc.replace_spaces(entry[2]),) + entry[3:12]))

export = po.make_export(data=module_meshes.meshes, data_name="meshes", tag="mesh",
    header_format="%d\r\n", process_entry=process_entry)
