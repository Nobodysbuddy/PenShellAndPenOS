from pathlib import Path
print("\n\n                Welcome To PenNavigator!                        ")
print("Pen Navigator Tells You Everything About Your Files and Folders!")
print("----------------------------------------------------------------\n")

while True:
    providedPath = input("NavPath>>>")

    print("Going To " + providedPath)
    print("Showing All Folders in " + providedPath + ":\n")
    
    if providedPath == "exit":
        break
    else:
        path = Path(providedPath)
        x = [x for x in path.iterdir() if x.is_dir()]
        index = 1
        for i in x:
            print(str(index) + ") " + str(i))
            index += 1