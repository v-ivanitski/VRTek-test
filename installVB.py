#!usr/bin/env python3

import os
import platform
import re
import subprocess

#Repository and pub key list
VB_DEB_REPO = "http://download.virtualbox.org/virtualbox/debian"
VB_RHEL_REPO = "http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo"
VB_FEDORA_REPO = "http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo"
VB_PUB_KEY = "https://www.virtualbox.org/download/oracle_vbox.asc"
VB_PUB_KEY_NEW = "https://www.virtualbox.org/download/oracle_vbox_2016.asc"

opSys = platform.linux_distribution()[0]
distrVersin = platform.linux_distribution()[2]
oldVersionDebDistr = ['wily','utopic','trusty','saucy','raring','quantal',
                      'precise','oneiric','natty','maverick','lucid','wheezy',
                      'squeeze','lenny']
debDistr = ['ubuntu','debian']
rpmDistr = ['centos', 'redhat', 'redhat', 'fedora']

def isDebRepoExist():
    sourcesList = open("/etc/apt/sources.list", "r")
    for line in sourcesList.readlines():
        reResult = re.search(VB_DEB_REPO, line)
        if (reResult != None):
            sourcesList.close()
            return True
    sourcesList.close()
    return False
        
def isRpmRepoExist():
    
    #find virtualboxb.repo if it`s OK
    return True
    #else:
    #return False

def addDebRepo():
    sourceList = open("/etc/apt/sources.list", "a")
    sourceList.write("deb" + " " + VB_DEB_REPO + " " + distrName + " contrib \n")
    sourceList.close()
    
def addRpmRepo():
    PIPE = subprocess.PIPE
    if (opSys.lower() == "fedora"):
        wgetCmd = "wget " + VB_FEDORA_REPO
    else:
        wgetCmd = "wget " + VB_RHEL_REPO
    wget = subprocess.Popen(wgetCmd, shell=True, stdin=PIPE, stdout=PIPE,
                            stderr=subprocess.STDOUT, close_fds=True,
                            cwd="/etc/yum.repos.d/")

def install():
    if opSys.lower() in debDistr:
        if not isDebRepoExist():
            addDebRepo()
        if distrVersion in oldVersionDebDistr:
            os.system("wget " + VB_PUB_KEY + " -O- | sudo apt-key add -")
        else:
            os.system("wget " + VB_PUB_KEY_NEW + " -O- | sudo apt-key add -")
        os.system("apt-get update")
        os.system("apt-get install virtualbox-5.1 dkms -y")

    if opSys.lower() in rpmDistr:
        if not isRpmRepoExist():
            addRpmRepo()
        os.system("yum update")
        os.system("yum install binutils qt gcc make patch libgomp glibc-headers " +
                  "glibc-devel kernel-headers kernel-devel dkms")
        os.system("yum install VirtualBox-5.1")
