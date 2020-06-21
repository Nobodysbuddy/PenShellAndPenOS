print("\n\nPenOS!\n")
print("Welcome To PenOS,")
print("a open-source Command Line Interface For Launching And Developing Applications")
print("------------------------------------------------------------------------------")
print("Type run To Run A Module.")
    
print('\n If You Want You Can Create Modules. Go To ')
print("                             Starting PenOS...")
print("------------------------------------------------------------------------\n\n")
    
while True:
    command = input("====>")
    if command == "install":
        pname = input("Package's Name: ")
        filename = "Core/PenOS/src/Modules/" + pname + '/' + pname + '.py'
        exec(open(filename).read())
        print("File Execution Over, You are Back...")
        
                
    elif command == "quit":
        break
