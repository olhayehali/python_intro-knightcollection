from knightcollection.menu import Menu

#run the program
#condition below check if this file is the main file that is being run
#this is important because if this file is being imported into another file
#this code will not run
if __name__ == "__main__":
    try:
        #create a menu object and start the program
        menu = Menu()
        #start the menu:start run method is menu class that is a thread
        menu.start()
    except Exception as e:
        print(e)
