from aiclaude import aicaller
from aigpt import call_chatgpt


user_text = ""

def main_menu(key):
    global user_text
    # 1-3 user text edit
    if key == "1":
        cleanup()
        user_text = input("Please enter your text:\n")
        cleanup()
        return
    
    if key == "2":
        cleanup()
        print(user_text) 
        wait = input("Press any key")
        cleanup()
        return
    
    if key == "3":
        cleanup()
        wait = input("Press any key to delete text")
        user_text = ""
        wait = input("Text deleted. Press any key")
        cleanup()
        return
    
    # calling ai caller with user text
    if key == "4":
        cleanup()
        print("Will send following text:\n")
        print(f"\033[96m{user_text}\033[0m\n")
        wait = input("Press any key\n")
        print("\n")
        aicaller(user_text)
        return

    if key == "5":
        cleanup()
        print("Will send following text:\n")
        print(f"\033[96m{user_text}\033[0m\n")
        wait = input("Press any key\n")
        print("\n")
        call_chatgpt(user_text)
        return

# cleaning the screen
def cleanup():
    print("\n" * 50)
    return
        

