#!/usr/bin/env python
import sys
from subprocess import call

"""
TODO: add capability to check parent-child output
"""


sshname = "yoursshnamehere" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) < 3:
        print "Usage: size [cluster] [install1] [install2] ..."
        sys.exit(2)
    execstr = "ssh -t " + sshname + "@pod-" + args[1] + ".wpengine.com \"cd /nas/wp/www/sites; sudo du -shc"
    for arg in args[2:]:
        execstr += " " + arg
    execstr += "\""

    
    stgstr = "ssh -t " + sshname + "@pod-" + args[1] + ".wpengine.com \"cd /nas/wp/www/staging; sudo du -shc"
    for arg in args[2:]:
        stgstr += " " + arg
    stgstr += "\""
    call(execstr, shell=True)
    print "staging sites:\n"
    call(stgstr, shell=True)

    
