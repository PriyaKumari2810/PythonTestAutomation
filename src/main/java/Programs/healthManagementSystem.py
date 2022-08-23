# Health Management System
# 3 clients - Person1, Person2 and Person3

def getdate():
    import datetime
    return datetime.datetime.now()

# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Person1-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Person1-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Person2-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Person2-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Person3-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Person3-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Person1),2(Person2),3(Person3)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Person1-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Person1-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Person2-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Person2-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Person3-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Person3-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Person1,Person2,Person3)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Person1 2 for Person2 3 for Person3 "))
    take(b)
else:
    b = int(input("Press 1 for Person1 2 for Person2 3 for Person3 "))
    retrieve(b)
