import string

from module_info import *
from module_scripts import *
from module_generated_scripts import *

from process_common import *
from process_operations import *

def save_scripts(variable_list,variable_uses,scripts,tag_uses,quick_strings):
  file = open(export_dir + "scripts.txt","w")
  file.write("scriptsfile version 1\n")
  file.write("%d\n" % len(scripts))
  for script in scripts:
    file.write("%s -1\n" % (convert_to_identifier(script[0])))
    save_statement_block(file,convert_to_identifier(script[0]), 0, script[1], variable_list,variable_uses,tag_uses,quick_strings)
    file.write("\n")
  file.close()

def save_python_header():
  file = open("./ID_scripts.py","w")
  for i, script in enumerate(scripts):
    file.write("script_%s = %d\n"%(convert_to_identifier(script[0]), i))
  file.write("\n\n")
  file.close()


print "Exporting scripts..."
save_python_header()
variable_uses = []
variables = load_variables(export_dir, variable_uses)
tag_uses = []
quick_strings = load_quick_strings(export_dir)
save_scripts(variables,variable_uses,scripts,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_quick_strings(export_dir,quick_strings)
