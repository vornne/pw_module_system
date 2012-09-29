import process_common as pc
import process_operations as po
import module_dialogs
import module_info
from header_dialogs import *

start_states = []
end_states = []

def compile_dialog_states(processor, dialog_file):
  global start_states
  global end_states
  unique_state_list = ["start", "party_encounter", "prisoner_liberated", "enemy_defeated", "party_relieved",
      "event_triggered", "close_window", "trade", "exchange_members", "trade_prisoners", "buy_mercenaries",
      "view_char", "training", "member_chat", "prisoner_chat"]
  unique_state_usages = [1 for i in unique_state_list]
  unique_states = dict((k, i) for i, k in enumerate(unique_state_list))
  last_index = len(unique_state_list)
  for entry in module_dialogs.dialogs:
    end_state = entry[5]
    index = unique_states.setdefault(end_state, last_index)
    if index == last_index:
      last_index += 1
      unique_state_list.append(end_state)
      unique_state_usages.append(0)
    end_states.append(index)
  for entry in module_dialogs.dialogs:
    start_state = entry[2]
    try:
      index = unique_states[start_state]
      unique_state_usages[index] += 1
      start_states.append(index)
    except KeyError:
      pc.ERROR("starting dialog state '%s' has no matching ending state" % start_state)
  for state, usages in zip(unique_state_list, unique_state_usages):
    if not usages:
      pc.ERROR("ending dialog state '%s' is not used" % state)
  with open(module_info.export_path("dialog_states.txt"), "wb") as state_file:
    state_file.write("".join("%s\r\n" % e for e in unique_state_list))

dialog_names = {}

def get_dialog_name(start_state, end_state, text):
  global dialog_names
  name = "dlga_%s:%s" % (pc.convert_to_identifier(start_state), pc.convert_to_identifier(end_state))
  text_list = dialog_names.setdefault(name, [])
  for i, existing_text in enumerate(text_list):
    if text == existing_text:
      name = "%s.%d" % (name, i + 1)
      break
  else:
    text_list.append(text)
  return name

def process_entry(processor, txt_file, entry, index):
  name = get_dialog_name(entry[start_state_pos], entry[end_state_pos], entry[text_pos])
  trp_pt = entry[speaker_pos]
  flags = entry[flags_pos]
  speaker = 0
  if flags & other:
    speaker = processor.process_id(trp_pt[1], "trp") << other_bits
    flags ^= other
    trp_pt = trp_pt[0]
  if flags & party_tpl:
    speaker |= processor.process_id(trp_pt, "pt")
  else:
    speaker |= processor.process_id(trp_pt, "trp")
  speaker |= flags
  output_list = ["%s %d %d " % (name, speaker, start_states[index])]
  output_list.extend(processor.process_block(entry[conditions_pos], "%s conditions" % name))
  output_list.append("%s " % pc.replace_spaces(entry[text_pos]) if entry[text_pos] else "NO_TEXT ")
  output_list.append(" %d " % end_states[index])
  output_list.extend(processor.process_block(entry[consequences_pos], "%s consequences" % name))
  output_list.append("%s " % entry[voice_pos] if len(entry) > voice_pos else "NO_VOICEOVER ")
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_dialogs.dialogs, data_name="dialogs", file_name="conversation",
    header_format="dialogsfile version 2\r\n%d\r\n", process_entry=process_entry, process_list=compile_dialog_states)
