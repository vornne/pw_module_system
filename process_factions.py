from module_info import *
from module_factions import *

from process_common import *

faction_name_pos = 0
faction_flags_pos = 2
faction_coherence_pos = 3
faction_relations_pos = 4
faction_ranks_pos = 5

def compile_relations():
  relations = []
  for i in xrange(len(factions)):
    r = [0.0 for j in range(len(factions))]
    relations.append(r)
  for i, faction in enumerate(factions):
    relations[i][i] = faction[faction_coherence_pos]
    rels = faction[faction_relations_pos]
    for rel in rels:
      rel_name = rel[0]
      other_pos = -1
      for j, faction_j in enumerate(factions):
        if faction_j[faction_name_pos] == rel_name:
          other_pos = j
      if other_pos == -1:
        print "ERROR faction not found: "+ rel_name
      else:
        relations[other_pos][i] = rel[1]
        relations[i][other_pos] = rel[1]
  return relations

def save_factions(relations):
  file = open(export_dir + "factions.txt","w")
  file.write("factionsfile version 1\n")
  file.write("%d\n"%len(factions))
  for i, faction in enumerate(factions):
    fac_color = 0xAAAAAA
    if len(faction) == 7:
      fac_color = faction[6]
    file.write("fac_%s %s %d %d \n"%(convert_to_identifier(faction[0]), replace_spaces(faction[1]), faction[2], fac_color))
    for reln in relations[i]:
      file.write(" %f "%reln)
    file.write("\n")
    ranks = []
    if (len(faction) > (faction_ranks_pos)):
      ranks = faction[faction_ranks_pos]
    file.write("%d "%(len(ranks)))
    for rank in ranks:
      file.write(" %s "%(replace_spaces(rank)))
  file.close()

def two_to_pow(x):
  result = 1
  for i in xrange(x):
    result = result * 2
  return result

def save_python_header():
  file = open("./ID_factions.py","w")
  for i, faction in enumerate(factions):
    file.write("fac_%s = %d\n"%(faction[0], i))
  file.write("\n\n")
  file.close()

print "Exporting factions..."
save_python_header()
relations = compile_relations()
save_factions(relations)
