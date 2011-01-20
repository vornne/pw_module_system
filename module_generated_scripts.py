from module_scripts import *

def generate_script(name, body):
  for script in scripts:
    if script[0] == name:
      script[1].extend(body)
      return
  else:
    raise Exception("Script '" + name + "' not found")

def generate_store_troop_skills_description():
  script_body = [(store_script_param, ":troop_id", 1)]
  for skill in pw_skills:
    script_body.extend([
      (store_skill_level, reg10, "skl_"+skill, ":troop_id"),
      (try_begin),
        (gt, reg10, 0),
        (str_store_string, s0, "@{s0}^"+get_skill_name(skill)+": {reg10}"),
      (try_end),
      ])
  return script_body
generate_script("store_troop_skills_description", generate_store_troop_skills_description())
