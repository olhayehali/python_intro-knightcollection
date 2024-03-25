from menu import Menu

if __name__ == "__main__":
    try:
        menu = Menu()
        menu.start()
    except Exception as e:
        print(e)
