import process_operations as po
import module_animations

def process_entry(processor, txt_file, entry, index):
  txt_file.write(" %s %d %d  %d\r\n" % (entry[0], entry[1], entry[2], len(entry) - 3))
  for anim in entry[3:]:
    output_list = ["  %f %s %d %d %d " % tuple(anim[0:5])]
    anim_len = len(anim)
    output_list.append("%d " % anim[5] if anim_len > 5 else "0 ")
    output_list.append("%f %f %f  " % anim[6] if anim_len > 6 else "0.0 0.0 0.0 ")
    output_list.append("%f " % anim[7] if anim_len > 7 else "0.0 ")
    output_list.append("\r\n")
    txt_file.write("".join(output_list))

export = po.make_export(data=module_animations.animations, data_name="animations", tag="anim", file_name="actions",
    header_format="%d\r\n", process_entry=process_entry)
