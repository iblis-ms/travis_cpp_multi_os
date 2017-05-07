#!/usr/bin/python

import os, sys, shutil
import platform

def runCommand(command):
  retcode = os.system(command)
  if retcode != 0:
    raise Exception("Error while executing:\n\t %s" % command)

if __name__ == "__main__":
  if os.path.isdir("output"):
    shutil.rmtree("output")
  os.mkdir("output")
  command = "cd output && cmake ../app && make" 
  runCommand(command)
