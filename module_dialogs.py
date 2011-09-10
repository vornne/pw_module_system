from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from module_constants import *

####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
# Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop id.
#    Use the constant 'anyone' if you'd like the line to match anybody.
# 2) Flags:
#    Appending '|party_tpl' to this field means that the dialog partner is a party template id
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other' means that the dialog partner field must be a tuple, and this line is spoken
#      by the second troop which you must make sure is present on the scene.
# 3) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 4) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
# 5) Dialog text (string).
# 6) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 7) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 8) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over.
####################################################################################################################

dialogs = [
]
