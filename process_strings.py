import process_common as pc
import process_operations as po
import module_strings
import module_generated_strings

def generate_strings(processor, unused):
  for name, generator in module_generated_strings.__dict__.iteritems():
    if name.startswith("generate_"):
      try:
        string_id = processor.process_id(name.replace("generate_", "str_"), "str")
        entry = module_strings.strings[string_id]
        module_strings.strings[string_id] = (entry[0], generator(entry[1], processor))
      except pc.ModuleSystemError as e:
        if not e.entry:
          e.entry = "generated strings"
        raise

def process_entry(processor, txt_file, entry, index):
  txt_file.write("str_%s %s\r\n" % (entry[0], pc.replace_spaces(entry[1])))

export = po.make_export(data=module_strings.strings, data_name="strings", tag="str",
    header_format="stringsfile version 1\r\n%d\r\n", process_entry=process_entry, process_list=generate_strings)
