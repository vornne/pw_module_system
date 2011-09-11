import process_common as pc
import process_operations as po
from header_troops import *
from header_skills import *
import module_troops

def process_entry(processor, txt_file, troop, index):
  troop.extend(0 for i in xrange(16 - len(troop)))
  image = "0" if troop[13] == 0 else pc.replace_spaces(str(troop[13]))
  scene_entry = 0 if not troop[4] else processor.process_id(troop[4][0], "scn") | troop[4][1]
  output_list = ["\r\ntrp_%s %s %s %s %d %d %d %d %d %d\r\n  " % (troop[0], pc.replace_spaces(troop[1]), pc.replace_spaces(troop[2]),
      image, troop[3], scene_entry, troop[5], processor.process_id(troop[6], "fac"), troop[14], troop[15])]
  output_list.extend("%d 0 " % processor.process_id(i, "itm") for i in troop[7])
  output_list.extend("-1 0 " for i in xrange(64 - len(troop[7])))
  output_list.append("\r\n ")
  output_list.append(" %d %d %d %d %d\r\n" % tuple((troop[8] >> (i * 8)) & 0xff for i in xrange(5)))
  output_list.append(" %d %d %d %d %d %d %d\r\n" % tuple((troop[9] >> (i * 10)) & 0x3ff for i in xrange(num_weapon_proficiencies)))
  output_list.append("%d %d %d %d %d %d \r\n  " % tuple((troop[10] >> (i * 32)) & 0xffffffff for i in xrange(num_skill_words)))
  output_list.extend("%d %d %d %d " % tuple((face_key >> (64 * i)) & 0xffffffffffffffff for i in reversed(xrange(4))) for face_key in troop[11:13])
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_troops.troops, data_name="troops", tag="trp",
    header_format="troopsfile version 2\r\n%d ", process_entry=process_entry)
