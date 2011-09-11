import process_common as pc
import process_operations as po
import module_factions

faction_relations = []

def compile_relations(processor, txt_file):
  global faction_relations
  factions_len = len(module_factions.factions)
  faction_relations = [[0.0 for j in xrange(factions_len)] for i in xrange(factions_len)]
  for i, faction in enumerate(module_factions.factions):
    faction_relations[i][i] = faction[3]
    for relation in faction[4]:
      other_faction = processor.identifier_map.get_id("fac", relation[0]) & 0xffffffff
      faction_relations[other_faction][i] = relation[1]
      faction_relations[i][other_faction] = relation[1]

def process_entry(processor, txt_file, faction, index):
  global faction_relations
  faction_len = len(faction)
  color = faction[6] if faction_len > 6 else 0xaaaaaa
  txt_file.write("fac_%s %s %d %d \r\n" % (faction[0], pc.replace_spaces(faction[1]), faction[2], color))
  map(txt_file.write, (" %f " % relation for relation in faction_relations[index]))
  ranks = faction[5] if faction_len > 5 else []
  txt_file.write("\r\n%d " % len(ranks))
  map(txt_file.write, (" %s " % pc.replace_spaces(rank) for rank in ranks))
  txt_file.write("\r\n")

export = po.make_export(data=module_factions.factions, data_name="factions", tag="fac",
    header_format="factionsfile version 1\r\n%d\r\n", process_entry=process_entry, process_list=compile_relations)
