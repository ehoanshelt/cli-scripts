#!/usr/bin/env python
import sys
import pickle
import os
from subprocess import Popen, PIPE, call

sshname = "yoursshusername" # replace with your login
localname = "yourlocalfilename" # replace with your login

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

    localdir = '/Users/%s/Documents/LRA/%s' % (localname, args[2])
    successmessage = 'Looks as clean as a whistle!'

#################### Check for Select * in Themes and PLugins #############################
    
    commandstrthemes = " \"grep -r 'Select \*' /nas/wp/www/sites/%s/wp-content/themes\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstrthemes)
    print "Checking for Bad Queries in Themes:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! Bad Queries found in themes!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/bad_query_themes.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/bad_query_themes.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"
    
    commandstrplugins = " \"grep -r 'Select \*' /nas/wp/www/sites/%s/wp-content/plugins\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstrplugins)
    print "Checking for Bad Queries in Plugins:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! Bad Queries found in plugins!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/bad_query_plugins.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/bad_query_plugins.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"
    
#################### Check for SESSION Variables in Themes and PLugins #############################
    
    commandstrsest = " \"grep -r '_SESSION' /nas/wp/www/sites/%s/wp-content/themes\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstrsest)
    print "Checking for SESSION Variables in Themes:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! SESSION Variables found in themes!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/SESSION_themes.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/SESSION_themes.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"
    
    commandstrsesp = " \"grep -r '_SESSION' /nas/wp/www/sites/%s/wp-content/plugins\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstrsesp)
    print "Checking for SESSION Variables in Plugins:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! SESSION Variables found in plugins!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/SESSION_plugins.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/SESSION_plugins.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"
        
        
#################### Check for Upload Manipulation in Themes and PLugins #############################
    
    commandstruploadt = " \"ack-grep -r 'add_action(\'upload_dir' /nas/wp/www/sites/%s/wp-content/themes\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstruploadt)
    print "Checking for Upload Manipulation in Themes:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! Upload Manipulation found in themes!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/Upload_Mani_themes.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/Upload_Mani_themes.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"
    
    commandstruploadp = " \"ack-grep -r 'add_action(\'upload_dir' /nas/wp/www/sites/%s/wp-content/plugins\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstruploadp)
    print "Checking for Upload Manipulation in Plugins:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! Upload Manipulation found in plugins!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/Upload_Mani_plugins.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/Upload_Mani_plugins.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"

#################### Check for Slow SQL Queries #############################
    sqlslow = "ssh -t %s@pod-%s.wpengine.com \"sudo cat /var/log/mysql/mysql-slow.log | grep %s\"" % (sshname, args[1], args[2])
    print "My-SQL Slow Log:\n"
    call(sqlslow, shell=True)
    print "++++++++++++++++++++++++++++++++++"

#################### Check for Long Query Error #############################
    longquery = "ssh -t %s@pod-%s.wpengine.com \"sudo cat /var/log/apache2/%s.error.log | grep LONG\"" % (sshname, args[1], args[2])
    print "Long Query Log:\n"
    call(longquery, shell=True)
    print "++++++++++++++++++++++++++++++++++"
	
#################### Check for Upload Manipulation in Themes and PLugins #############################
    sqlslow = "ssh -t %s@pod-%s.wpengine.com \"cat /var/log/mysql/mysql-slow.log | grep ehoanshelt" % (sshname, args[1])
    print "My-SQL Slow Log:\n"
    call(sqlslow, shell=True)

#################### Check for php handler in .htaccess #############################
    
    commandstrphphandle = " \"grep 'AddType application/x-httpd-php' /nas/wp/www/sites/%s/.htaccess\"" % (args[2])
    execstr = '%s%s' % (connstr,commandstrphphandle)
    print "Checking for PHP handler in .htaccess:\n"
    p = Popen(execstr, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    if len(output) > 10:
        text = "ALERT! PHP handler found in .htaccess!"
        print text
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        file = open(localdir + '/php_handler.txt', 'w+')
        pickle.dump(output, file)
        file.close()
        print "Writing to File Completed to %s/php_handler.txt" % (localdir)
        print "++++++++++++++++++++++++++++++++++"
    else:
        print successmessage
        print "++++++++++++++++++++++++++++++++++"
