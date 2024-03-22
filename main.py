knights_number = 0
knights = []


#this create a knight
def create_knights(knights):

    #create a new list for knight
    knights_data = []

    print("lets create a knights")

    #set the information for the knight
    knights_data.append(str(input("what is the name of the knight name: ")))

    #add information to the knights 
    knights.append(knights_data)

#select the current knights and select one
def select_knights(knights):
    while knights_number < 1:
        print("their names is "+knights[0])
        knights_number += 1

def data_changed(knights):
    print("--what would you like to update?--")
    print("1:knight name "+knights[0])

    try:
        selection = int(input("selection your option "))
        if selection == 1:
            if knights_number >= 0:
                print("you have a knight")
            name = str(input("what is the new name:"))
            knights[0] = name
            print("your knight new name is "+knights[0])
        else:
            print("---please select a valid option---")
    except ValueError:
        print("---try again---")

def menu(knights_number):
    pass

print("good bye sir "+knights[0])