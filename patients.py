#!/usr/bin/python
#
# This program keeps a list of names for a doctor's
# office. It uses a menu to control the list.

names = [] # an empty list of names

cmd = ""

while cmd !='4':
    print("1. Listnames")
    print("2. Addname")
    print("3. Call.next.patient")
    print("\n4. Quit")
    cmd = input("\rCommand :") # In Python 3 raw_input() was replaced with input()
    if cmd == '1':
        for name in names:
            print(name)
        print("\n")
    elif cmd == '2':
        newName = input("Name :")
        names.append(newName)
    elif cmd == '3':
        if len(names) == 0:
            print("There are no more patients!")
        else:
            nextPatient = names[0]
            names.remove(nextPatient)
            print (f"Calling {nextPatient}")
    elif cmd != '4':
        print("Invalid command!")