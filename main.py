from knight import Knight
import pickle
import random, os

pickle_file = "data.pickle"


#setting the scene
knights_number = 0
knights_list = []



#create a knight
def create_knights(knight_number):
    global knights_list 
    #ask the user for the information of the knight
    print("lets create a knights")
    name = str(input("what is the name of the knight name: "))
    strength = int(input("what is the strength of the knight: "))
    agility = int(input("what is the agility of the knight: "))
    specialArmor = str(input("what is the special armor of the knight: "))
    tempKnight = Knight(name, strength, agility, specialArmor)
    #set the information for the knight
    #print out the knight that was made
    print("\n\n\r\r--- your knight---\n")
    tempKnight.render()
    run = True
    while run:
        if str(input("would you like to save this knight? y/n: ")) == "y":
            run = False
            knights_list.append(tempKnight)
            with open(pickle_file, "wb") as file:
                pickle.dump(knights_list, file)
                print("knight saved")

#update the data of a knight
def change_data(index):
    global knights_list
    try:
        if index > 0 and index <= len(knights_list):
            print("what would you like to change?")
            print("1: name")
            print("2: strength")
            print("3: agility")
            print("4: special armor")
            print("0: exit")
            selection = int(input("select a number: "))
            if selection == 1:
                knights_list[index-1].name = str(input("what is the name of the knight name: "))
            elif selection == 2:
                knights_list[index-1].strength = int(input("what is the strength of the knight: "))
            elif selection == 3:
                knights_list[index-1].agility = int(input("what is the agility of the knight: "))
            elif selection == 4:
                knights_list[index-1].specialArmor = str(input("what is the special armor of the knight: "))
            elif selection == 0:
                return
            else:
                print("please select a valid number")
            with open(pickle_file, "wb") as file:
                pickle.dump(knights_list, file)
                print("knight updated")
            return True
        else:
            print("please select a valid number")
            return False
    except Exception as e:
        print(e)

#delete the data of a knight
def delete_data(index):
    global knights_list
    try:
        if index > 0 and index <= len(knights_list):
            knights_list.pop(index-1)
            with open(pickle_file, "wb") as file:
                pickle.dump(knights_list, file)
                print("knight deleted")
            return True
        else:
            print("please select a valid number")
            return  False
        pass
    except Exception as e:
        print(e)

#show all knights
def show_all_knights():
    os.system('clear')
    print("--- all your knights---")
    #show all knights in list with good format
    with open(pickle_file, "rb") as file:
        knights_list = pickle.load(file)
    if int(len(knights_list)) > 0:
        for k,knight in enumerate(knights_list,1):
            knight.render(k)
    if input("press any key to continue"):
        pass
    else:
        print("you have no knights")
    menu()

#select the current knights and select one
def select_knights(knights_ist,action):
    global knights_list
    for k,knight in enumerate(knights_list,1):
        print(f"{k}: {knight.name}")

    if action == "update":
        print("what knight would you like to update?\n")
        index = int(input("select a number: "))
        if change_data(index) : 
            print("knight updated")
        else: select_knights(knights_list,"update")
    else:
        print("what knight would you like to delete?\n")
        index = int(input("select a number: "))
        if delete_data(index) : 
            print("knight deleted")
        else: select_knights(knights_list,"delete")


#call a knight a change their data
def menu():
    os.system('clear')
    global knights_list 
    global knights_number
    #print display menu
    print("what do you want to do?")
    print("1: create a new  knight")
    print("2: update a  knight")
    print("3: delete  a  knight")
    print("4: show all your  knight")    
    print("0:Exit")
    with open(pickle_file, "rb") as file:
        knights_list = pickle.load(file)
        knights_number = len(knights_list)

    #allow a selection to be tested 
    try:
        selection = int(input("select select a number:"))
        print() # create a blank line

        if selection == 1:
            
            knights_number += 1

            create_knights(knights_number)
            menu() 
        elif selection == 2:
            if int(len(knights_list)) == 0:
                print("you need to create a knight first \n")
            else:
                select_knights(knights_list,"update")
            menu()
        elif selection == 3:
            if int(len(knights_list)) == 0:
                print("you need to create a knight first \n")
            else:
                select_knights(knights_list,"delete")
            menu()
        elif selection == 4:
            show_all_knights()
        elif selection == 0:
            print("goodbye")
            return

        #required for catching an integer
        else:
            print("---try again---")
            menu()
    #we are loruning integer select
    except ValueError:
        print("---try again---")
        print("please select a number")
        menu()

#run the program
#condition below check if this file is the main file that is being run
#this is important because if this file is being imported into another file
#this code will not run
if __name__ == "__main__":
    menu()
