

print("\n\n                 Welcome To PenShell! ")
print("------------------------------------------------------\n\n")

imp = {'commands': [], 'packName': "PenShell", 'username': ""}
imp['commands'] = ["echo", "launch", "view", "setpass", "penos"]

imp['username'] = input("Type Your Username for this session: ")
print("Hello, " + imp['username'])


while True:
    command = input("=======>")
    if command == "echo":
        toecho = input("what to echo: ")
        print(toecho)
    elif command == "launch":
        apptofind = input("which app to launch: ")
        filename = 'Apps/' + apptofind + '/' + apptofind +'.py'
        exec(open(filename).read())
        exitcode = 2
        print("     Program Ended With Exit Code: " + str(exitcode))
        print("      You Are Now Back In PenShell.") 
        print("---------------------------------------------------")
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
    elif command == "setpass":
        print("Sorry, but the setpass feature is not aviliable is this version, it may come in later versions.")
    elif command == "penos":
        print("Entering PenOS...")
        gotAccess = input("PenOS is only aviliable To Developers Right Now. Please Type PenDev Pass To Continue: ")
        if gotAccess == "Spc123@pen123":
            print("Welcome...")
            print("Launching PenOS DevCreate...")
            exec(open("Core/PenOS/src/__init__.py").read())
            print("    PenOS DevCreate Ended, You Are Back In PenShell.")
            print("---------------------------------------------------------\n")
        else:
            print("Wrong Credentials!")
            
    else:
        print("unknown command!")


    