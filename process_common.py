import string

full_table = string.maketrans(" '`()-\t", "_______")
def convert_to_identifier_with_no_lowercase(s):
  return string.translate(s, full_table, ",|")

def convert_to_identifier(s):
  return string.lower(convert_to_identifier_with_no_lowercase(s))

part_table = string.maketrans(" \t", "__")
def replace_spaces(s):
  return string.translate(s, part_table)
