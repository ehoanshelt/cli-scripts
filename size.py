#!/usr/bin/env python
import sys
from subprocess import call

"""
TODO: add capability to check parent-child output
"""


sshname = "yoursshname" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) < 3:
        print "Usage: size [cluster] [install1] [install2] ..."
        sys.exit(2)
    execstr = "ssh -t %s@pod-%s.wpengine.com \"cd /nas/wp/www/sites; sudo du -shc" % (sshname, args[1])
    for arg in args[2:]:
        execstr += " " + arg
    execstr += "\""

    
    stgstr = "ssh -t %s@pod-%s.wpengine.com \"cd /nas/wp/www/staging; sudo du -shc" % (sshname, args[1])
    for arg in args[2:]:
        stgstr += " " + arg
    stgstr += "\""
    
    gitstr = "ssh -t %s@pod-%s.wpengine.com \"cd /nas/wp/www/sites; sudo du -shc" % (sshname, args[1])
    for arg in args[2:]:
        gitstr += " %s/.git" % (arg)
    gitstr += "\""
    
    wpepstr = "ssh -t %s@pod-%s.wpengine.com \"cd /nas/wp/www/sites; sudo du -shc" % (sshname, args[1])
    for arg in args[2:]:
        wpepstr += " %s/_wpeprivate" % (arg)
    wpepstr += "\""
    
    
    print "production sites:\n"
    call(execstr, shell=True)
    print "staging sites:\n"
    call(stgstr, shell=True)
    print "git size:\n"
    call(gitstr, shell=True)
    print "_wpeprivate size:\n"
    call(wpepstr, shell=True)

"""

This is a one-liner to run from bash:

ourvar=$(sudo /nas/wp/ec2/cluster parent-child acctname); echo -e "du -shc "${ourvar}| bash
"""
