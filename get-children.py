#!/usr/bin/env python
import sys
from subprocess import call

sshname = "yoursshname" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) < 3:
        print "Usage: size [cluster] [parent_installname]"
        sys.exit(2)
    execstr = "ssh -t %s@pod-%s.wpengine.com \"sudo /nas/wp/ec2/cluster parent-child %s\"" % (sshname, args[1], args[2])
    
    print "All Children:\n"
    call(execstr, shell=True)
   