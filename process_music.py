import process_operations as po
import module_music

def process_entry(processor, txt_file, entry, index):
  txt_file.write("%s %d %d\r\n" % (entry[1], entry[2], entry[2]|entry[3]))

export = po.make_export(data=module_music.tracks, data_name="music", tag="track",
    header_format="%d\r\n", process_entry=process_entry)
