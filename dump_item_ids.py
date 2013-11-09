#!/usr/bin/python -tt

from module_items import *
import argparse

parser = argparse.ArgumentParser(description="Dump item ids with names, for use with the administrator items tool.")
parser.add_argument("output_file", nargs='?', default="admin_item_ids", help="file name without extension")
args = parser.parse_args()

with open(args.output_file + ".txt", "w") as f:
  for i, item in enumerate(items):
    if (item[1].startswith("INVALID") or "Banner" in item[1]):
      continue
    elif (item[0] == "all_items_end"):
      break
    f.write("{0:3} = {1} ({2})\n".format(i, item[1], item[0]))
