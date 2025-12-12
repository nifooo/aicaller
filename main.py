from menu import main_menu
from menu import user_text



def main():
    print("\n" * 50)
    print("")
    print("----API AI Caller----\n")
    print("Please choose:\n")
    print("(1) - New text\n")
    print("(2) - Show current text\n")
    print("(3) - Delete current text\n")
    print("(4) - Call AI\n")
    print("(0) - Quit")
    
    
    
    
while True:
    main()
    key = input("Please choose (1-4)")
    main_menu(key)
    main()
    if key == "0":
        break


