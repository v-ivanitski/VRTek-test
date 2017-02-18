#!/usr/bin/env python3

import os

import installVB
from installVB import opSys
from installVB import debDistr
from installVB import rpmDistr

def isVirtualBoxExist ():
    if opSys.lower() in debDistr:
        return os.system("dpkg --get-selections | grep virtualbox")
    if opSys.lower() in rpmDistr:
        return os.system("yum list all | grep virtualbox")

if isVirtualBoxExist():
    installVB.install

os.makedirs("./test")

config = open ("./config", "r")
for line in config.readlines():
    os.system(line)
config.close()
for i in range (2,4):
    cloneCmd = ("vboxmanage clonevm ubuntu1604_1 --name ubuntu1604_" + i +
                " --register") 
    os.system(cloneCmd)


