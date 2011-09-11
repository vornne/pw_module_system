import process_common as pc
import process_operations as po
from header_items import *
import module_items

def process_entry(processor, txt_file, item, index):
  visible_name = pc.replace_spaces(item[1])
  item_meshes = item[2]
  output_list = [" itm_%s %s %s %d " % (item[0], visible_name, visible_name, po.block_len(item_meshes))]
  output_list.extend([" %s %d " % mesh_imod for mesh_imod in item_meshes])
  stats = item[6]
  output_list.append(" %d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\r\n" % (item[3], item[4], item[5], item[7],
      get_weight(stats), get_abundance(stats), get_head_armor(stats), get_body_armor(stats), get_leg_armor(stats),
      get_difficulty(stats), get_hit_points(stats), get_speed_rating(stats), get_missile_speed(stats),
      get_weapon_length(stats), get_max_ammo(stats), get_thrust_damage(stats), get_swing_damage(stats)))
  item_len = len(item)
  if item_len > 9:
    output_list.append(" %d\r\n" % po.block_len(item[9]))
    output_list.extend([" %d" % processor.process_id(item_faction, "fac") for item_faction in item[9]])
    output_list.append("\r\n")
  else:
    output_list.append(" 0\r\n")
  txt_file.write("".join(output_list))
  triggers = item[8] if item_len > 8 else []
  triggers = processor.process_triggers(triggers, item[0])
  triggers.append("\r\n")
  txt_file.write("".join(triggers))

export = po.make_export(data=module_items.items, data_name="items", tag="itm", file_name="item_kinds1",
    header_format="itemsfile version 3\r\n%d\r\n", process_entry=process_entry)
