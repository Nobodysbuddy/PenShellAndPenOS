print("\n\nPenOS!\n")
print("Welcome To PenOS,")
print("a open-source Command Line Interface For Launching And Developing Applications")
print("------------------------------------------------------------------------------")

modules = []


if modules == []:
    print('You Dont Have Any Modules Installed. Please Use The Install Command To Install One.')

else:
    print('You Have Modules! You Are Good To Go!')
    
print('\n If You Dont Have Any Modules Install One To Do Things With PenOS.')
print("Starting PenOS...")
print("------------------------------------------------------------------------\n\n")
    
while True:
    command = input("====>")
    if command == "install":
        pname = input("Package's Name: ")
        try:
            filename = 'Modules/' + pname + '/' + pname + '.py'
            exec(open(filename).read())
        except:
            print("Cant Find Filename Or Module Doesn't Exist")
        
        
    elif command == "quit":
        break
