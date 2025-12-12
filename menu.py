user_text = ""

def main_menu(key):
    global user_text
    if key == "1":
        print("\n" * 50)
        user_text = input("Please enter your text:")
        print("\n" * 50)
        return
    if key == "2":
        print("\n" * 50)
        print(user_text) 
        wait = input("Press any key")
        print("\n" * 50)
        return
    if key == "3":
        print("\n" * 50)
        wait = input("Press any key to delete text")
        user_text = ""
        wait = input("Text deleted. Press any key")
        print("\n" * 50)
        return