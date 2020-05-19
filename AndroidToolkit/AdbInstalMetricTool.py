import os
from subprocess import Popen, PIPE, STDOUT

from Projects.EllaConsole.PrintFunctions import *


script_path = os.path.dirname(os.path.realpath(__file__))
monitor_path = script_path + "\Adb\OVRMetricsTool_v1.4.apk"




command = "adb install"
install_what = monitor_path
adbPath = script_path + "\Adb\\"

def Start():
    final = adbPath + command + " " + monitor_path
    print_err("Executing: " + final)
    p = Popen(final, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    for line in p.stdout:
        line = str(line.rstrip())
        print(line)


Start()