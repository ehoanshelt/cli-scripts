#!/usr/bin/env python
import sys
from subprocess import call

"""
installs.py

This script will log into a pod and list the /nas/wp/www/sites/ folder.

Used to see if a pod really is free!
"""

sshname = "mcalabresi_" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) != 2:
        print "Usage: installs [pod]"
        sys.exit(2)
    execstr = "ssh " + sshname + "@pod-" + args[1] + ".wpengine.com \"cd /nas/wp/www/sites; ls\""
    call(execstr, shell=True)

    
