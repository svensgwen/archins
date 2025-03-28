from InquirerPy import inquirer

def main_menu():
    while True:
        choice = inquirer.select(
            message="Main Menu - Choose an option:",
            choices=["Option 1", "Option 2", "Advanced Options →", "Exit"],
        ).execute()

        if choice == "Advanced Options →":
            advanced_options()
        elif choice == "Exit":
            break
        else:
            print(f"You selected: {choice}")

def advanced_options():
    while True:
        choice = inquirer.select(
            message="Advanced Options - Choose an option:",
            choices=["Sub-option A", "Sub-option B", "More Options →", "← Back"],
        ).execute()

        if choice == "More Options →":
            more_options()
        elif choice == "← Back":
            return
        else:
            print(f"You selected: {choice}")

def more_options():
    while True:
        choice = inquirer.select(
            message="More Options - Choose an option:",
            choices=["Extra 1", "Extra 2", "← Back"],
        ).execute()

        if choice == "← Back":
            return
        else:
            print(f"You selected: {choice}")

if __name__ == "__main__":
    main_menu()
