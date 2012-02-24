import process_common as pc
import process_operations as po
import module_scripts
import module_generated_scripts

def generate_scripts(processor, unused):
  for script_name, script_generator in module_generated_scripts.__dict__.iteritems():
    if script_name.startswith("generate_"):
      try:
        script_id = processor.process_id(script_name.replace("generate_", "script_"), "script")
        module_scripts.scripts[script_id][1].extend(script_generator())
      except pc.ModuleSystemError as e:
        if not e.entry:
          e.entry = "generated scripts"
        raise

def process_entry(processor, txt_file, entry, index):
  output_list = ["%s -1\r\n" % entry[0]]
  output_list.extend(processor.process_block(entry[1], entry[0], check_can_fail=True))
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_scripts.scripts, data_name="scripts", tag="script",
    header_format="scriptsfile version 1\r\n%d\r\n", process_entry=process_entry, process_list=generate_scripts)
