from menu import main_menu
from menu import user_text
from menu import cleanup



def main():
    # Mainmenu loads 
    cleanup()
    print("")
    print("----API AI Caller----\n")
    print("Please choose:\n")
    print("(1) - New text\n")
    print("(2) - Show current text\n")
    print("(3) - Delete current text\n")
    print("(4) - Call AI: Claude\n")
    print("(5) - Call AI: ChatGPT\n")
    print("(0) - Quit\n")
    
    
    
    
while True:
    main()
    # giving user input to menu component
    key = input("Please choose (1-4): ")
    main_menu(key)
    
    if key == "0": 
        cleanup()
        break


