#!/usr/bin/python -tt

import os
import argparse
import subprocess
import shutil

parser = argparse.ArgumentParser(description="Compile the Mount&Blade Warband shaders.")
parser.add_argument("-b", "--compile-b", action="store_true", help="compile the ps_2_b profile as well")
args = parser.parse_args()

if not os.access(os.path.join("shaders", "fxc.exe"), os.R_OK|os.X_OK):
  print "You must copy fxc.exe from the TaleWorlds Warband shader package to the shaders subdirectory."
  exit(1)

import module_info

def compile_profile(profile, name):
  command_list = ["./fxc.exe", "/nologo", "/T", "fx_2_0", "/D", "PS_2_X=%s" % profile, "/Fo", "mb.fxo", "mb.fx"]
  exit_code = subprocess.call(command_list, cwd="shaders")
  output_fxo = os.path.join("shaders", "mb.fxo")
  if exit_code == 0:
    module_fxo = module_info.export_path(name)
    try:
      os.remove(module_fxo)
    except Exception:
      pass
    shutil.move(output_fxo, module_fxo)
  else:
    try:
      os.remove(output_fxo)
    except Exception:
      pass
    exit(exit_code)

compile_profile("ps_2_a", "mb.fx")

if args.compile_b:
  compile_profile("ps_2_b", "mb_2b.fx")
