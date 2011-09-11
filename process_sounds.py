import process_operations as po
import module_sounds

def process_sounds(processor, txt_file):
  unique_sound_files = {}
  sound_files_list = []
  sounds_list = []
  last_sound_no = 0
  for sound in module_sounds.sounds:
    sound_flags = sound[1]
    sound_files = sound[2]
    sounds_list.append("snd_%s %d %d " % (sound[0], sound[1], len(sound_files)))
    for sound_file in sound_files:
      if isinstance(sound_file, str):
        flags = 0
      else:
        flags = sound_file[1]
        sound_file = sound_file[0]
      sound_no = unique_sound_files.setdefault(sound_file, last_sound_no)
      if sound_no == last_sound_no:
        last_sound_no += 1
        sound_files_list.append(" %s %d\r\n" % (sound_file, sound_flags))
      sounds_list.append("%d %d " % (sound_no, flags))
    sounds_list.append("\r\n")
  txt_file.write("soundsfile version 3\r\n%d\r\n" % len(sound_files_list))
  txt_file.write("".join(sound_files_list))
  txt_file.write("%d\r\n" % len(module_sounds.sounds))
  txt_file.write("".join(sounds_list))

export = po.make_export(data=module_sounds.sounds, data_name="sounds", tag="snd", process_list=process_sounds)
