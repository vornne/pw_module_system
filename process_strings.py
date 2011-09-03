import string
from header_common import *
from module_info import *
from module_strings import *

from process_common import *

def save_strings(strings):
  ofile = open(export_dir + "strings.txt","w")
  ofile.write("stringsfile version 1\n")
  ofile.write("%d\n"%len(strings))
  for string in strings:
    ofile.write("str_%s %s\n"%(convert_to_identifier(string[0]),replace_spaces(string[1])))
  ofile.close()

def save_python_header():
  ofile = open("./ID_strings.py","w")
  for i, string in enumerate(strings):
    ofile.write("str_%s = %d\n"%(convert_to_identifier(string[0]), i))
  ofile.write("\n\n")
  ofile.close()

print "Exporting strings..."
save_python_header()
save_strings(strings)
