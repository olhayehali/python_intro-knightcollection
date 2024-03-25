from  threading import Thread
from knight import Knight
import os
import pickle

class Menu(Thread):

    """
    
    """

    def __init__(self):
        super().__init__()
        #pickle file name
        self.pickle_file = "data.pickle"
        #setting the scene
        self.knights_number = 0
        self.knights_list = []
        #check if the file exists if not create it
        if not os.path.exists(self.pickle_file):
            with open(self.pickle_file, "wb") as file:
                pickle.dump(self.knights_list, file)
        #read the file
        self.writeOrRead("rw")

    #method for reading and writing to the pickle file
    def writeOrRead(self,mode):
        try:
            if mode == "rw":
                with open(self.pickle_file,mode) as file:
                    self.knights_list = pickle.load(file)
                    self.knights_number = len(self.knights_list)                    
                    print(self.knights_list, self.knights_number) 
                    raise Exception("error")
            elif mode == "wb":
                with open(self.pickle_file,mode) as file:
                    pickle.dump(self.knights_list, file)
                    self.knights_list = pickle.load(file)
                    self.knights_number = len(self.knights_list)
        except Exception as e:
            print("error reading file")

    #create a knight
    def create_knights(self,knight_number):
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
                self.knights_list.append(tempKnight)
                self.writeOrRead("wb")

    #update the data of a knight
    def change_data(self,index):
        self.writeOrRead("rb")
        print(index)
        try:
            print("what would you like to change?")
            print("1: name")
            print("2: strength")
            print("3: agility")
            print("4: special armor")
            print("0: exit")
            while True:
                selection = int(input("select a number: "))
                if selection == 0 or selection == 1 or selection == 2 or selection == 3 or selection == 4:
                    break
                else:
                    print("please select a valid number")
            if selection == 1:
                print("current name: ",self.knights_list[index-1].name)
                self.knights_list[index-1].name = str(input("what is the name of the knight name: "))
            elif selection == 2:
                print("current strength: ",self.knights_list[index-1].strength)
                self.knights_list[index-1].strength = int(input("what is the strength of the knight: "))
            elif selection == 3:
                print("current agility: ",self.knights_list[index-1].agility)
                self.knights_list[index-1].agility = int(input("what is the agility of the knight: "))
            elif selection == 4:
                print("current special armor: ",self.knights_list[index-1].specialArmor)
                self.knights_list[index-1].specialArmor = str(input("what is the special armor of the knight: "))
            elif selection == 0:
                return True
            else:
                print("please select a valid number")
            self.writeOrRead("wb")
            print("knight updated")
            #ask if want to change more
            if str(input("would you like to change more? y/n: ")) == "y":
                self.change_data(index)
            return True
        except Exception as e:
            print(e)

    #delete the data of a knight
    def delete_data(self,index):
        try:
            self.knights_list.pop(index-1)
            self.writeOrRead("wb")
            return True
        except Exception as e:
            print(e)
            return False

    #select the current knights and select one
    def select_knights(self,action):
        self.writeOrRead("rb")
        for k,knight in enumerate(self.knights_list,1):
            print(f"{k}: {knight.name}")

        if action == "update":
            print("what knight would you like to update?\n")
            while True:
                index = int(input("select a number: "))
                if index > 0 and index <= len(self.knights_list):
                    break
                else:
                    print("please select a valid number")
            if self.change_data(index) : 
                print("knight updated")
            else: self.select_knights("update")
        else:
            print("what knight would you like to delete?\n")
            while True:
                index = int(input("select a number: "))
                if index > 0 and index <= len(self.knights_list):
                    break
                else:
                    print("please select a valid number")

            if self.delete_data(index) : 
                print("knight deleted")
            else: self.select_knights("delete")

    #show all knights
    def show_all_knights(self):
        self.writeOrRead("rb")
        os.system('clear')
        print("--- all your knights---")
        print(f"\n your have :{len(self.knights_list)} knights\n")
        #show all knights in list with good format
        if int(len(self.knights_list)) > 0:
            for k,knight in enumerate(self.knights_list,1):
                knight.render(k)
        if input("press any key to continue"):
            pass
        else:
            print("you have no knights")
        self.menu()

    #menu for the program
    #this is the main menu for the program
    #this is where the user will select what they want to do
    #this will also call the other methods in the program
    def menu(self):
        #clear the screen
        os.system('clear')
        #print display menu
        print("what do you want to do?")
        print("1: create a new  knight")
        print("2: update a  knight")
        print("3: delete  a  knight")
        print("4: show all your  knight")    
        print("0:Exit")
        try:
            with open(self.pickle_file, "rb") as file:
                self.knights_list = pickle.load(file)
                knights_number = len(self.knights_list)
        except Exception as e:
            print("error")

        #allow a selection to be tested 
        try:
            selection = int(input("select select a number:"))
            print() # create a blank line

            if selection == 1:
                
                self.knights_number += 1

                self.create_knights(self.knights_number)
                self.menu() 
            elif selection == 2:
                if int(len(self.knights_list)) == 0:
                    print("you need to create a knight first \n")
                else:
                    self.select_knights("update")
                self.menu()
            elif selection == 3:
                if int(len(self.knights_list)) == 0:
                    print("you need to create a knight first \n")
                else:
                    self.select_knights("delete")
                self.menu()
            elif selection == 4:
                self.show_all_knights()
            elif selection == 0:
                print("goodbye")
                return

            #required for catching an integer
            else:
                print("---try again---")
                self.menu()
        #we are loruning integer select
        except ValueError:
            print("---try again---")
            print("please select a number")
            self.menu()

    #run the program
    #condition below check if this file is the main file that is being run
    #this is important because if this file is being imported into another file
    #this code will not run
    def run(self):
        pass