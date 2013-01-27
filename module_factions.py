from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

# Adding more factions to this list will not work: many scripts are limited to 10 factions by the scene file format.

factions = [
  ("commoners","Commoners", 0, 0, [], [], 0x990099),
  ("outlaws","Outlaws", 0, 0, [], [], 0x775500),
  ("1","Red Faction", 0, 0, [], [], 0xDD0000),
  ("2","White Faction", 0, 0, [], [], 0xFFFFFF),
  ("3","Blue Faction", 0, 0, [], [], 0x3333FF),
  ("4","Green Faction", 0, 0, [], [], 0x00DD00),
  ("5","Yellow Faction", 0, 0, [], [], 0xCCAA44),
  ("6","Purple Faction", 0, 0, [], [], 0x663333),
  ("7","Orange Faction", 0, 0, [], [], 0x884411),
  ("8","Black Faction", 0, 0, [], [], 0x000000),
  ("factions_end","factions_end", 0, 0, [], []),
]
