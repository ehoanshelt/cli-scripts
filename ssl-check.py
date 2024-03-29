#!/usr/bin/env python
import sys
from subprocess import call

"""
ssl.py

This script will log into a pod and check all of the .conf files in /nas/wp/conf/lb/sites/ folder to see if anyone has a dedicated IP configured.

"""

sshname = "yourusername" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) != 2:
        print "Usage: ssl [pod]"
        sys.exit(2)
    execstr = "ssh %s@pod-%s.wpengine.com \"cd /nas/local/ssl; ls\"" % (sshname, args[1])
    print "\nList of installs with SSL certificates on the server:\n"
    call(execstr, shell=True)
    execstr = "ssh %s@pod-%s.wpengine.com \"cd /nas/wp/conf/lb/sites; grep :443 *.conf\"" % (sshname, args[1])
    print "\nList of sites that have a dedicated IP - check this against your migration list:\n"
    call(execstr, shell=True)
    redirectstr = "ssh %s@pod-%s.wpengine.com \"cd /nas/wp/conf/lb/sites; grep -A 5 \'Redirect insecure\' *.conf\"" % (sshname, args[1])
    print "\nList of sites that have forced paths to HTTPS - check this against your migration list:\n"
    call(redirectstr, shell=True)

