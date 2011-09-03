from header_common import *
from module_info import *
from module_sounds import *

def write_python_header(sounds):
  file = open("./ID_sounds.py","w")
  for i, sound in enumerate(sounds):
    file.write("snd_%s = %d\n"%(sound[0], i))
  file.write("\n\n")
  file.close()

def write_sounds(sound_samples, sounds):
  ofile = open(export_dir + "sounds.txt","w")
  ofile.write("soundsfile version 3\n")
  ofile.write("%d\n"%len(sound_samples))
  for sound_sample in sound_samples:
    ofile.write(" %s %d\n"%sound_sample)
  ofile.write("%d\n"%len(sounds))
  for sound in sounds:
    ofile.write("snd_%s %d %d "%(sound[0], sound[1],len(sound[2])))
    sample_list = sound[2]
    for s in sample_list:
      ofile.write("%d %d "%(s[0], s[1]))
    ofile.write("\n")
  ofile.close()

def compile_sounds(sounds):
  unique_sound_files = []
  for sound in sounds:
    sound_flags = sound[1]
    sound_files = sound[2]
    for i, sound_file in enumerate(sound_files):
      if isinstance(sound_file, list):
        sound_file_flags = sound_file[1]
        sound_file = sound_file[0]
      else:
        sound_file_flags = 0
      for j, unique_sound_file in enumerate(unique_sound_files):
        if unique_sound_file[0] == sound_file:
          sound_no = j
          break
      else:
        sound_no = len(unique_sound_files)
        unique_sound_files.append((sound_file, sound_flags))
      sound_files[i] = [sound_no, sound_file_flags]
  return unique_sound_files

print "Exporting sounds..."
sound_samples = compile_sounds(sounds)
write_sounds(sound_samples, sounds)
write_python_header(sounds)
