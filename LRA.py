#!/usr/bin/env python
import sys
import pickle
import os
from subprocess import Popen, PIPE

sshname = "yourusernamehere" # replace with your login

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

    localdir = '/Users/erichoanshelt/Documents/LRA/%s' % (args[2])

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
        text = "Looks as clean as a whistle!"
        print text
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
        text = "Looks as clean as a whistle!"
        print text
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
        text = "Looks as clean as a whistle!"
        print text
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
        text = "Looks as clean as a whistle!"
        print text
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
        text = "Looks as clean as a whistle!"
        print text
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
        text = "Looks as clean as a whistle!"
        print text
        print "++++++++++++++++++++++++++++++++++"

