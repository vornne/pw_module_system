import process_common as pc
import process_operations as po
import module_game_menus

def process_entry(processor, txt_file, entry, index):
  output_list = ["menu_%s %d %s %s" % (entry[0], entry[1], pc.replace_spaces(entry[2]), entry[3])]
  output_list.extend(processor.process_block(entry[4], entry[0]))
  output_list.append("%d\r\n" % po.block_len(entry[5]))
  for menu in entry[5]:
    output_list.append(" mno_%s " % menu[0])
    name = "%s: %s" % (entry[0], menu[0])
    output_list.extend(processor.process_block(menu[1], name + " conditions"))
    output_list.append(" %s " % pc.replace_spaces(menu[2]))
    output_list.extend(processor.process_block(menu[3], name + " consequences"))
    output_list.append(" %s " % pc.replace_spaces(menu[4]) if len(menu) > 4 else " . ")
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_game_menus.game_menus, data_name="game_menus", tag="menu", file_name="menus",
    header_format="menusfile version 1\r\n %d\r\n", process_entry=process_entry)
