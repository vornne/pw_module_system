from module_info import *
from process_common import *
from process_operations import *

print "Checking global variable usages..."
variable_uses = []
variables = load_variables(export_dir,variable_uses)
for i, variable_use in enumerate(variable_uses):
  if (variable_use == 0):
    print "WARNING: Global variable never used: " + variables[i]
