from header_common import *
from header_parties import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Icon and flags.
#   3.1) Map icon.
#   3.2) Party flags. See header_parties.py for a list of available flags.
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id.
#   11.2) Number of troops in this stack.
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0

parties = [
  ("main_party","Main Party",(0,pf_limit_members),no_menu,"pt_none",0,0,ai_bhvr_hold,0,(17, 52.5),[("trp_player",1,0)]), # hard coded, must not be removed
]
