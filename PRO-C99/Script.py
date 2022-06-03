#Setup
import datetime
import os

t = datetime.datetime
now = t.now()
files = os.listdir("FolderToCheck/")

#Display
for i in range(1, 2):
    print("\n")
print("(Tip: try 1 sec for testing purposes)\n")
unit = input("Enter unit ('hr'/'min'/'sec'): ")
inter = int(input(f"Enter expiry (in {unit}s): "))
for file in files:
    path = "FolderToCheck/"+str(file)

    a = t.fromtimestamp(os.path.getctime(path))
    oldDate = str(a)
    currentDate = str(now)

    d1 = t.strptime(oldDate, "%Y-%m-%d %H:%M:%S.%f")
    d2 = t.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f")

    diff = d2 - d1
    if unit=="sec" :
        if diff.seconds>=inter:
            suffix = "second" if round(diff.seconds)==1 else "seconds"
            print(f"Age of file is {diff.seconds} {suffix}")
            choice = input("Do you want to delete it?(y/n): ")
            if choice=="y":
                os.remove("FolderToCheck/"+str(file))
                continue
            elif choice=="n":
                continue
        else:
            continue
    elif unit=="min" :
        if (diff.seconds/60)>=inter:
            suffix = "minute" if round(diff.seconds/60)==1 else "minutes"
            print(f"Age of file is {round(diff.seconds/60)} {suffix}")
            choice = input("Do you want to delete it?(y/n): ")
            if choice=="y":
                os.remove("FolderToCheck/"+str(file))
                continue
            elif choice=="n":
                continue
        else:
            continue
    elif unit=="hr" :
        if (diff.seconds/3600)>=inter:
            suffix = "hour" if round(diff.seconds/3600)==1 else "hours"
            print(f"Age of file is {round(diff.seconds/3600)} {suffix}")
            choice = input("Do you want to delete it?(y/n): ")
            if choice=="y":
                os.remove("FolderToCheck/"+str(file))
                continue
            elif choice=="n":
                continue
        else:
            continue    

    

for i in range(1, 2):
    print("\n")