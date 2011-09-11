import process_common as pc
import process_operations as po
import module_parties

def process_list(processor, txt_file):
  party_count = len(module_parties.parties)
  txt_file.write("partiesfile version 1\r\n%d %d\r\n" % (party_count, party_count))

def process_entry(processor, txt_file, entry, index):
  icon_flags = (entry[2][1] if po.block_len(entry[2]) > 1 else 0) | processor.process_id(entry[2][0], "icon") if entry[2] else 0
  menu = processor.process_id(entry[3], "mnu")
  template = processor.process_id(entry[4], "pt")
  faction = processor.process_id(entry[5], "fac")
  pos = entry[9]
  txt_file.write(" 1 %d %d p_%s %s %d %d %d %d %d %d %d %d %d %f %f %f %f %f %f 0.0 %d " % (index, index, entry[0],
      pc.replace_spaces(entry[1]), icon_flags, menu, template, faction, entry[6], entry[6], entry[7], entry[8], entry[8],
      pos[0], pos[1], pos[0], pos[1], pos[0], pos[1], len(entry[10])))
  txt_file.write("".join("%d %d 0 %d " % (processor.process_id(member[0], "trp"), member[1], member[2]) for member in entry[10]))
  txt_file.write("\r\n%f\r\n" % ((3.1415926 / 180.0) * entry[11] if len(entry) > 11 else 0.0))

export = po.make_export(data=module_parties.parties, data_name="parties", tag="p",
    process_list=process_list, process_entry=process_entry)
