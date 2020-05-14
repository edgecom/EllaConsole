import os
from subprocess import Popen, PIPE, STDOUT

from Projects.EllaConsole.PrintFunctions import *


script_path = os.path.dirname(os.path.realpath(__file__))

path = script_path + "\Adb\\adb"

command = "logcat"

def Start():
    p = Popen(path + " " + command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    for line in p.stdout:
        line = str(line.rstrip())
        if True:
            print(str(line))
        else:
            if line.find("Ella") != -1:
                Print(str(line))

while(True):
    Start()
    pass

