import process_common as pc
import process_operations as po
import module_party_templates

def process_entry(processor, txt_file, entry, index):
    icon_flags = 0 if not entry[2] else ((entry[2][1] if po.block_len(entry[2]) > 1 else 0) | processor.process_id(entry[2][0], "icon"))
    txt_file.write("pt_%s %s %d %d %d %d " % (entry[0], pc.replace_spaces(entry[1]), icon_flags, entry[3],
        processor.process_id(entry[4], "fac"), entry[5]))
    member_count = po.block_len(entry[6])
    if member_count > 6:
      raise pc.ERROR("party templates can only have a maximum of 6 members")
    members_list = ["%d %d %d %d " % (processor.process_id(troop[0], "trp"), troop[1], troop[2], troop[3] if len(troop) > 3 else 0) for troop in entry[6]]
    members_list.extend("-1 " for i in xrange(6 - member_count))
    members_list.append("\r\n")
    txt_file.write("".join(members_list))

export = po.make_export(data=module_party_templates.party_templates, data_name="party_templates", tag="pt",
    header_format="partytemplatesfile version 1\r\n%d\r\n", process_entry=process_entry)
