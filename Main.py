import requests
import os
import sys
import time

print("\n\n                 Welcome To PenShell! ")
print("------------------------------------------------------\n\n")

imp = {'commands': [], 'packName': "PenShell", 'username': ""}
imp['commands'] = ["echo", "launch", "view", "setpass", "penos", "nav", "update", "fetch", "cmd"]

imp['username'] = input("Type Your Username for this session: ")
print("Hello, " + imp['username'])
where = 'PENSHELLSYSTEMHISTORY'

while True:
    command = input((where + '>'))
    if command == "echo":
        toecho = input("what to echo: ")
        print(toecho)
        where += '/' + command
    elif command == "launch":
        apptofind = input("which app to launch: ")
        filename = 'Apps/' + apptofind + '/' + apptofind +'.py'
        exec(open(filename).read())
        exitcode = 2
        print("     Program Ended With Exit Code: " + str(exitcode))
        print("      You Are Now Back In PenShell.") 
        print("---------------------------------------------------")
        where += '/' + command
    elif command == "quit":
        print("quitting...")
        break
    elif command == "view":
        toview = input("What To View: ")
        if toview == "packagename":
            print(imp['packName'])
        elif toview == "commands":
            print(str(imp['commands']))
        else:
            print("Error: Cant Show Data ( 404: Data Not Found )")
        where += '/' + command
    elif command == "setpass":
        print("Sorry, but the setpass feature is not aviliable is this version, it may come in later versions.")
        where += '/' + command
    elif command == "penos":
        print("Entering PenOS...")
        print("Welcome...")
        exec(open("Core/PenOS/src/__init__.py").read())
        print("    PenOS Ended, You Are Back In PenShell.")
        print("---------------------------------------------------------\n")
        where += '/' + command
    elif command == "nav":
        print("Fetching Module 'nav'...")
        print("Starting PenNavigator!")
        exec(open('Core/PenNavigator/nav.py').read())
        print("------------------- PenNavigator Ended, You Are Back In PenShell--------------------------------")
        where += '/' + command
    elif command == "update":
        print("Updating PenShell...")
        insreq = requests.get('https://penshellpenos.firebaseio.com/.json')
        print("Update Request Code: " + str(insreq.status_code))
        print("Update Done...")
        print("Update Details: \n" + insreq.text)
        print("Thanks For Updating, Hope You Like PenShell!")
        where += '/' + command
    elif command == "fetch":
        dataid = input("What To Fetch: ")
        if dataid == "pendata":
            print(str(imp))
        else:
            print("INVALID DATAID")
        where += '/' + command
    elif command == "cmd":
        os.system("start cmd")
        where += '/' + command
    elif command == "clrhis":
        where = 'PENSHELLSYSTEMHISTORY'
    elif command == "watchandomithistory":
        x = 'pendevonlycommand'
        print(x, end="\r")
        time.sleep(1)
        where += '/' + command
    else:
        print("unknown command!")
        where += '/UNKNOWNERROR'
        
print("Bye!!! :)")


    