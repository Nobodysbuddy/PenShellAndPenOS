import math
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
    global result
    if opr == "add":
        num1 = input("Type First Number: ")
        num2 = input("Type Second Number: ")
        result = float(num1) + float(num2)
        print("result: " + str(result))
    elif opr == "quit":
        print("quiting...")
        break
    elif opr == "sub":
        num1 = input("Type First Number: ")
        num2 = input("Type Second Number: ")
        result = float(num1) - float(num2)
        print('result: ' + str(result))
    elif opr == "mul":
        num1 = input("Type First Number: ")
        num2 = input("Type Second Number: ")
        result = float(num1) * float(num2)
        print('result: ' + str(result))
    elif opr == "div":
        num1 = input("Type First Number: ")
        num2 = input("Type Second Number: ")
        result = float(num1) / float(num2)
        print('result: ' + str(result))
    elif opr == "flrdiv":
        num1 = input("Type First Number: ")
        num2 = input("Type Second Number: ")
        result =  math.floor(float(num1) / float(num2))
        print('result: ' + str(result))
    elif opr == "celdiv":
        num1 = input("Type First Number: ")
        num2 = input("Type Second Number: ")
        result = math.ceil(float(num1) / float(num2))
        print('result: ' + str(result))
    else:
        print('Error: Invalid Operator')
       
    

