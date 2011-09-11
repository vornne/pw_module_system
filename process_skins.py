import process_common as pc
import process_operations as po
import module_skins

def check_count(processor, txt_file):
  if len(module_skins.skins) > 16:
    raise pc.ERROR("the maximum number of skins is 16")

def process_entry(processor, txt_file, entry, index):
  face_keys = entry[6]
  output_list = ["%s %d\r\n %s %s %s\r\n %s %d " % (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], len(face_keys))]
  output_list.extend("skinkey_%s %d %d %f %f %s " % (pc.convert_to_identifier(key[4]).lower(),
          key[0], key[1], key[2], key[3], pc.replace_spaces(key[4])) for key in face_keys)
  hair_meshes = entry[7]
  output_list.append("\r\n%d\r\n" % po.block_len(hair_meshes))
  output_list.extend(" %s " % e for e in hair_meshes)
  beard_meshes = entry[8]
  output_list.append("\r\n %d\r\n" % po.block_len(beard_meshes))
  output_list.extend("  %s\r\n" % e for e in beard_meshes)
  hair_textures = entry[9]
  output_list.append("\r\n %d " % po.block_len(hair_textures))
  output_list.extend(" %s " % e for e in hair_textures)
  beard_textures = entry[10]
  output_list.append("\r\n %d " % po.block_len(beard_textures))
  output_list.extend(" %s " % e for e in beard_textures)
  face_textures = entry[11]
  output_list.append("\r\n %d " % po.block_len(face_textures))
  for face in face_textures:
    hair_textures = face[2]
    hair_colors = face[3] if len(face) > 3 else []
    output_list.append(" %s %d %d %d " % (face[0], face[1], po.block_len(hair_textures), po.block_len(hair_colors)))
    output_list.extend(" %s " % e for e in hair_textures)
    output_list.extend(" %d " % e for e in hair_colors)
  voices = entry[12]
  output_list.append("\r\n %d " % po.block_len(voices))
  output_list.extend(" %d %s " % e for e in voices)
  output_list.append("\r\n %s %f \r\n" % (entry[13], entry[14]))
  entry_len = len(entry)
  blood_1 = processor.process_id(entry[15], "psys") if entry_len > 15 else 0
  blood_2 = processor.process_id(entry[16], "psys") if entry_len > 16 else 0
  constraints = entry[17] if entry_len > 17 else []
  output_list.append("%d %d\r\n%d\r\n" % (blood_1, blood_2, po.block_len(constraints)))
  for constraint in constraints:
    output_list.append("\r\n%f %d %d " % (constraint[0], constraint[1], len(constraint) - 2))
    output_list.extend(" %f %d" % e for e in constraint[2:])
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_skins.skins, data_name="skins", tag="skin",
    header_format="skins_file version 1\r\n%d\r\n", process_entry=process_entry, process_list=check_count)
