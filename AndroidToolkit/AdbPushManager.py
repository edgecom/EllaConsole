import os
from subprocess import Popen, PIPE, STDOUT

from Projects.EllaConsole.PrintFunctions import *

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


script_path = os.path.dirname(os.path.realpath(__file__))
script_path = script_path.split("\\")

ella_path = ""

for i in script_path:
        if i == "Scripts":
            break
        ella_path += i + "\\"

print_debug("Found Ella in: " + ella_path)
#/data/user/0/com.EllaActivity1/files/
#toWhere = "/storage/emulated/0/data/user/0/Ella/"
toWhere = "/data/user/0/com.EllaActivity1/files/"

product_path = os.path.dirname(os.path.realpath(__file__)) + "\MinimalProducts" + "\BureauVeritas.xml"

product = ET.parse(product_path)
product_root: ET.Element = product.getroot()

exportPahts: [str] = []

command = "adb push"
#command = "adb -d shell \"run-as com.example.test cat /data/data/com.EllaActivity/test > data.db \""
adbPath = os.path.dirname(os.path.realpath(__file__)) + "\Adb\\" + command

#adb_root = "adb root"
#adb_disable_verity = "adb disable-verity"

def CopyFile(paths):
    concatedCommand = adbPath + " " +  paths
    print_debug("Executing: " + concatedCommand)
    concatedCommand = concatedCommand.replace("\\", "/")
    p = Popen(concatedCommand, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    for line in p.stdout:
        line = str(line.rstrip())
        if (line.find('adb: error') != -1):
            print_err(line)
        else:
            print(str(line))
    pass

for i in product_root.iter():
    if (i != product_root):
        for j in i.iter():
            if (j != i):
                if (str(j.tag) == "TakeAll"):
                    from_path = ella_path + str(i.tag) + "\\"
                    to_path = toWhere + str(product_root.tag) + "/" + str(i.tag) + "/"
                    exportPahts.append(from_path + " " + to_path)
                    print_warn("Adding " + to_path)
                else:
                    for k in j.iter():
                        if (k != j):
                            from_path = ella_path + str(i.tag) + "\\" + str(j.tag) + "\\" + str(k.text)
                            to_path = toWhere + str(product_root.tag) + "/" + str(i.tag) + "/" + str(j.tag) + "/" + str(k.text)
                            exportPahts.append(from_path + " " + to_path)
                            print_warn("Adding " + to_path)



for i in exportPahts:
    print("Copying: " + i)
    CopyFile(i)
