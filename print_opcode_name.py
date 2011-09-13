#!/usr/bin/python

import argparse
import header_operations

parser = argparse.ArgumentParser(description="Convert an opcode from an error message in Mount&Blade Warband to the matching operation name.")
parser.add_argument("opcode", type=int, help="the opcode from the error message")
args = parser.parse_args()

print header_operations.get_opcode_name(args.opcode)
