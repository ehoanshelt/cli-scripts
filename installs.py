#!/usr/bin/env python
import sys
from subprocess import call

"""
installs.py

This script will log into a pod and list the /nas/wp/www/sites/ folder.

Used to see if a pod really is free!
"""

sshname = "yourusername" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) != 2:
        print "Usage: installs [pod]"
        sys.exit(2)
    execstr = "ssh %s@pod-%s.wpengine.com \"cd /nas/wp/www/sites; ls\"" % (sshname, args[1])
    call(execstr, shell=True)

    
