#!/usr/bin/env python
import sys
import pickle
import os
from subprocess import Popen, PIPE, call

sshname = "tturkleton_" # replace with your login

if __name__ == "__main__":
    # Check for parameters: first parameter should be a pod/cluster; subsequent parameters should be a list of installs
    args = sys.argv
    if len(args) < 3:
        print "Usage: size [cluster] [install1]"
        sys.exit(2)
    if len(args[1]) == 3:
    	connstr = "ssh -t %s@sftp%s.wpengine.com" % (sshname,args[1])
    if len(args[1]) > 3:
    	connstr = "ssh -t %s@pod-%s.wpengine.com" % (sshname,args[1])

#################### Check for Select * in Themes and PLugins #############################
    
    commandstrthemes = "%s \"grep -r 'Select \*' /nas/wp/www/sites/%s/wp-content/themes\"" % (connstr, args[2])
    print "Checking for Bad Queries in Themes:\n"
    call(commandstrthemes, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"
    
    commandstrplugins = "%s \"grep -r 'Select \*' /nas/wp/www/sites/%s/wp-content/plugins\"" % (connstr, args[2])
    print "Checking for Bad Queries in Themes:\n"
    call(commandstrplugins, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"
    
    
#################### Check for SESSION Variables in Themes and PLugins #############################
    
    commandstrsest = "%s \"grep -r '_SESSION' /nas/wp/www/sites/%s/wp-content/themes\"" % (connstr, args[2])
    print "Checking for SESSIONS in Themes:\n"
    call(commandstrsest, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"
    
    commandstrsesp = "%s \"grep -r '_SESSION' /nas/wp/www/sites/%s/wp-content/plugins\"" % (connstr, args[2])
    print "Checking for SESSIONS in Plugins:\n"
    call(commandstrsesp, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"
        
        
#################### Check for Upload Manipulation in Themes and PLugins #############################
    
    commandstruploadt = "%s \"grep -r 'add_action(\'upload_dir\'' /nas/wp/www/sites/%s/wp-content/themes\"" % (connstr, args[2])
    print "Looking for Upload Manipulation is Themes:\n"
    call(commandstruploadt, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"
    
    commandstruploadp = "%s \"grep -r 'add_action(\'upload_dir\'' /nas/wp/www/sites/%s/wp-content/plugins\"" % (connstr, args[2])
    print "Looking for Upload Manipulation is Plugins:\n"
    call(commandstruploadp, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"

#################### Check for Slow SQL Queries #############################
    sqlslow = "%s \"sudo cat /var/log/mysql/mysql-slow.log | grep %s\"" % (connstr, args[2])
    print "My-SQL Slow Log:\n"
    call(sqlslow, shell=True)
    print "++++++++++++++++++++++++++++++++++"

#################### Check for Long Query Error #############################
    longquery = "%s \"sudo cat /var/log/apache2/%s.error.log | grep LONG\"" % (connstr, args[2])
    print "Long Query Log:\n"
    call(longquery, shell=True)
    print "++++++++++++++++++++++++++++++++++"

#################### Check WordPress Core Modifications for wp-admin & includes #############################
    wpadmincheck = "%s \"cd /nas/wp/www/sites/%s/_wpeprivate && tar -zxf /nas/wp/install/wordpress-3.9.2.tar.gz -C /nas/wp/www/sites/%s/_wpeprivate && diff -r wordpress/wp-admin ../wp-admin\"" % (connstr, args[2],args[2])
    print "WordPress Core Modidications:\n"
    call(wpadmincheck, shell=True)
    wpincludecheck = "%s \"cd /nas/wp/www/sites/%s/_wpeprivate && tar -zxf /nas/wp/install/wordpress-3.9.2.tar.gz -C /nas/wp/www/sites/%s/_wpeprivate && diff -r wordpress/wp-includes ../wp-includes && rm -r wordpress\"" % (connstr, args[2],args[2])
    call(wpincludecheck, shell=True)
    print "Finished!"
    print "++++++++++++++++++++++++++++++++++"

