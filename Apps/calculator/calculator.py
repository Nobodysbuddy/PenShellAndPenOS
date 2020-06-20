print("\n\n    Welcome To The Calculator!")
print("-----------------------------------------------")
print("This Is An Special App Created For PenShell. ")
print("( \xa9 Penshell Calculator, all rights reserved. )\n")

print("Please Get Ready For A Tour Of Our Calculator:")
print("the \"->\" is where you will type your operation which you want to perform.")
print("any opertation asks for two (or three) numbers")
print("the result is shown afetr the \"result:\" statement")
print("type quit to end the program.")
print("Lets Start:\n")


while True:
    opr = input("->")
    num1 = input("Type First Number: ")
    num2 = input("Type Second Number: ")
    global result
    if opr == "add":
        result = float(num1) + float(num2)
        print("result: " + str(result))
    elif opr == "quit":
        print("quiting...")
        break
    else:
        print('Error: Cant Display Result ( 404: Command Not Found )')
       
    

