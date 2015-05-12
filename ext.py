import os, sys

for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
  base_file, ext = os.path.splitext(filename)
  if ext == ".DATA":
    os.rename(filename, base_file + ".DATA.prc")