#!/usr/bin/env python
"""
teamwork.py

CLI hooks into TeamWork API
"""

import json
import sys
import urllib
import urllib2

# TeamWork user-specific data -- change this to match your own
username="matthew@wpengine.com"
key="jump497ankle"
companyID = "27567"

toplevelURL = "https://wpengine.teamwork.com/"

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, toplevelURL, key, "xxx") # TeamWork uses API key as username and dummy password
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)

projectsURL = toplevelURL + "projects.json"
urllib2.install_opener(opener)
#response = urllib2.urlopen(urllib2.Request(projectsURL))

#print response.read()

args = sys.argv
if (len(args) < 2) or (args[1] == 'help'):
    print 'Usage: teamwork <command> [options]\n'
    print 'Options:\n'
    print ' create <project_name> <ZenDesk ticket number> [account_name]	--	Creates a new TeamWork project with the name specified'
    print '    --account_name will use project_name unless directly specified'
    sys.exit(2)

command = sys.argv[1]
if command == 'create':
    # Create a new project
    if len(args) < 4:
        print 'Usage: teamwork create <project_name> <ZenDesk ticket> [account_name]'
        sys.exit(2)
    projectname = sys.argv[2]
    ticketID = sys.argv[3]
    try:
        acctname = sys.argv[4]
    except IndexError:
        acctname = projectname
    print('Creating project %s...' % projectname)
    dict = {
        "project": {
            "name": projectname,
            "description": "",
            "startDate": "",
            "endDate": "",
            "companyId": companyID,
            "newCompany": "",
            "category-id": "3102" # make this a configurable option based on category
        }
    }
    data = json.dumps(dict)
    req = urllib2.Request(projectsURL, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError, err:
        if err.code == 422:
            print('Project name %s taken, please try another one!' % projectname)
            sys.exit(3)
        else:
            raise
    response = f.read()
    f.close()
    response_dict = json.loads(response)
    if response_dict['STATUS'] == 'OK':
        print('Project %s successfully created\n' % projectname)
        print 'Creating default task lists...\n'
        projectID = response_dict['id']
        tl_dict = {
            "todo-list": {
                "name": "Provision Pod",
                "description": "",
                "milestone-id": "",
                "todo-list-template-id": "171807"
            }
        }
        tl_data = json.dumps(tl_dict)
        tasklistURL = toplevelURL + "projects/" + projectID + "/todo_lists.json"
        tl_req = urllib2.Request(tasklistURL, tl_data, {'Content-Type': 'application/json'})
        try:
            tl_f = urllib2.urlopen(tl_req)
        except urllib2.HTTPError, err:
            raise
        tl_response = tl_f.read()
        tl_f.close()
        tl_response_dict = json.loads(tl_response)
        if tl_response_dict['STATUS'] == 'OK':
            print('Task list \"Provision Pod\" for project %s successfully created\n' % projectname)
        else:
            print('Something went wrong: %s' % tl_response_dict['STATUS'])
            sys.exit(3)
        tl2_dict = {
            "todo-list": {
                "name": "Pre-migration Checks",
                "description": "",
                "milestone-id": "",
                "todo-list-template-id": "170443"
            }
        }
        tl2_data = json.dumps(tl2_dict)
        tasklistURL = toplevelURL + "projects/" + projectID + "/todo_lists.json"
        tl2_req = urllib2.Request(tasklistURL, tl2_data, {'Content-Type': 'application/json'})
        try:
            tl2_f = urllib2.urlopen(tl2_req)
        except urllib2.HTTPError, err:
            raise
        tl2_response = tl2_f.read()
        tl2_f.close()
        tl2_response_dict = json.loads(tl2_response)
        if tl2_response_dict['STATUS'] == 'OK':
            print('Task list \"Pre-migration Checks\" for project %s successfully created\n' % projectname)
        else:
            print('Something went wrong: %s' % tl2_response_dict['STATUS'])
            sys.exit(3)
        tl3_dict = {
            "todo-list": {
                "name": "Migration of Data",
                "description": "",
                "milestone-id": "",
                "todo-list-template-id": "170448"
            }
        }
        tl3_data = json.dumps(tl3_dict)
        tasklistURL = toplevelURL + "projects/" + projectID + "/todo_lists.json"
        tl3_req = urllib2.Request(tasklistURL, tl3_data, {'Content-Type': 'application/json'})
        try:
            tl3_f = urllib2.urlopen(tl3_req)
        except urllib2.HTTPError, err:
            raise
        tl3_response = tl3_f.read()
        tl3_f.close()
        tl3_response_dict = json.loads(tl3_response)
        if tl3_response_dict['STATUS'] == 'OK':
            print('Task list \"Migration of Data\" for project %s successfully created\n' % projectname)
        else:
            print('Something went wrong: %s' % tl3_response_dict['STATUS'])
            sys.exit(3)
        print('Creating default links in project...')
        linkURL = toplevelURL + "projects/" + projectID + "/links.json"
        link1_dict = {
            "link": {
                "name": "ZenDesk",
                "description": "",
                "private": "0",
                "code": "https://help.wpengine.com/tickets/" + ticketID,
                "open-in-new-window": "1"
            }
        }
        link1_data = json.dumps(link1_dict)
        link1_req = urllib2.Request(linkURL, link1_data, {'Content-Type': 'application/json'})
        try:
            link1_f = urllib2.urlopen(link1_req)
        except urllib2.HTTPError, err:
            raise
            print('Something went wrong: %s' % link1_response_dict['STATUS'])
            sys.exit(3)
        link1_response = link1_f.read()
        link1_f.close()
        link1_response_dict = json.loads(link1_response)
        print('Link \"ZenDesk\" for project %s successfully created\n' % projectname)
        link2_dict = {
            "link": {
                "name": "OverDrive",
                "description": "",
                "private": "0",
                "code": "https://overdrive.wpengine.com/account/config/" + acctname,
                "open-in-new-window": "1"
            }
        }
        link2_data = json.dumps(link2_dict)
        link2_req = urllib2.Request(linkURL, link2_data, {'Content-Type': 'application/json'})
        try:
            link2_f = urllib2.urlopen(link2_req)
        except urllib2.HTTPError, err:
            raise
            print('Something went wrong: %s' % link2_response_dict['STATUS'])
            sys.exit(3)
        link2_response = link2_f.read()
        link2_f.close()
        link2_response_dict = json.loads(link2_response)
        print('Link \"OverDrive\" for project %s successfully created\n' % projectname)
    else:
        print('Something went wrong: %s' % response_dict['STATUS'])
        sys.exit(3)
