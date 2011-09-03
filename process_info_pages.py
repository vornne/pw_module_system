import string

from module_info import *
from module_info_pages import *

from process_common import *

def save_info_pages():
  ofile = open(export_dir + "info_pages.txt","w")
  ofile.write("infopagesfile version 1\n")
  ofile.write("%d\n"%(len(info_pages)))
  for i, info_page in enumerate(info_pages):
    ofile.write("ip_%s %s %s"%(info_page[0], string.replace(info_page[1]," ","_"), string.replace(info_page[2]," ","_")))
    ofile.write("\n")
  ofile.close()

def save_python_header():
  ofile = open("./ID_info_pages.py","w")
  for i, info_page in enumerate(info_pages):
    ofile.write("ip_%s = %d\n"%(info_page[0], i))
  ofile.write("\n\n")
  ofile.close()

print "Exporting info pages..."
save_info_pages()
save_python_header()
  
