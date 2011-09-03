import string

from module_info import *
from module_quests import *

from process_common import *

def save_quests():
  ofile = open(export_dir + "quests.txt","w")
  ofile.write("questsfile version 1\n")
  ofile.write("%d\n"%(len(quests)))
  for i_quest in xrange(len(quests)):
    quest = quests[i_quest]
    ofile.write("qst_%s %s %d "%(quest[0],(string.replace(quest[1]," ","_")),quest[2]))
    ofile.write("%s "%(string.replace(quest[3]," ","_")))
    ofile.write("\n")
  ofile.close()

def save_python_header():
  ofile = open("./ID_quests.py","w")
  for i, quest in enumerate(quests):
    ofile.write("qst_%s = %d\n"%(quest[0], i))
  for i, quest in enumerate(quests):
    ofile.write("qsttag_%s = %d\n"%(quest[0], opmask_quest_index|i))
  ofile.write("\n\n")
  ofile.close()

print "Exporting quests..."
save_quests()
save_python_header()
