import process_operations as po
import module_particle_systems

def process_entry(processor, txt_file, entry, index):
  output_list = ["psys_%s %d %s  %d %f %f %f %f %f \r\n" % (entry[0], entry[1], entry[2],
      entry[3], entry[4], entry[5], entry[6], entry[7], entry[8])]
  output_list.extend("%f %f   %f %f\r\n" % (bt, bm, ft, fm) for (bt, bm), (ft, fm) in zip(entry[9:18:2], entry[10:19:2]))
  output_list.extend("%f %f %f   " % e for e in entry[19:21])
  entry_len = len(entry)
  output_list.append("%f \r\n" % entry[21])
  output_list.append("%f " % entry[22] if entry_len > 22 else "0.0 ")
  output_list.append("%f " % entry[23] if entry_len > 23 else "0.0 ")
  output_list.append("\r\n")
  txt_file.write("".join(output_list))

export = po.make_export(data=module_particle_systems.particle_systems, data_name="particle_systems", tag="psys",
    header_format="particle_systemsfile version 1\r\n%d\r\n", process_entry=process_entry)
