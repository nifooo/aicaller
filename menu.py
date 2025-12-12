from aiclaude import aicaller


user_text = ""

def main_menu(key):
    global user_text
    # 1-3 user text edit
    if key == "1":
        print("\n" * 50)
        user_text = input("Please enter your text:\n")
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
    # calling ai caller with user text
    if key == "4":
        print("\n" * 50)
        print("Will send following text:\n")
        print(f"\033[96m{user_text}\033[0m\n")
        wait = input("Press any key\n")
        print("\n")
        aicaller(user_text)
        return
        

