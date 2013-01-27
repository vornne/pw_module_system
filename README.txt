See LICENCE.txt and LICENSE_explanation.txt for usage requirements.

See STYLE.txt for formatting and style recommendations.

This module system requires python installed. Set the path for your module
directory in module_info.py, then double click build_module.bat or run
build_module.py from a terminal to compile it.

module_*.py files contain the module system data that can be edited.
header_*.py files contain definitions that should only be changed with care,
if you know what you are doing.
ID_*.py files just list the numbers associated with each object, and are
optional to generate by passing -i to build_module.py.
process_*.py files do the converting into the numeric format for the M&B
engine, and should definitely not be edited unless you really know what you
are doing.

The dump_crafting_recipes.py script can be run from a terminal to produce .txt
or .xml files with generated crafting data.

If fxc.exe is added to the shaders directory, compile_shaders.py can be run
from a terminal to compile shaders/mb.fx.

The name_server directory contains an optional PHP and MySQL name server, for
associating player names with unique ids (serial numbers) and setting specific
administrator permissions for each player.

The server_stats directory contains a PHP script to fetch and display settings
of Warband servers running PW, as displayed in the server list in game.
