import process_operations as po
import module_postfx

def process_entry(processor, txt_file, entry, index):
  output_list = ["pfx_%s %d %d" % entry[0:3]]
  output_list.extend("  %f %f %f %f" % tuple(e) for e in entry[3:6])
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_postfx.postfx_params, data_name="postfx", tag="pfx",
    header_format="postfx_paramsfile version 1\r\n%d\r\n", process_entry=process_entry)
