user_text = ""

def main_menu(key):
    global user_text
    if key == "1":
        print("\n" * 50)
        user_text = input("Please enter your text:")
        print("\n" * 50)
        return