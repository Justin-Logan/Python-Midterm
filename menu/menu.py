import betting.bet
from utils import clear_screen

class Menu:
    def __init__(self, user):
        self._user = user
        self.draw_menu(user)
    
    def draw_menu(self, user):
        print("Welcome to Horse Betting!")
        print("\nPlease select from the following options (1-6):\n")
        print("\t1) Place an exacta bet")
        print("\t2) Place an exactabox bet")
        print("\t3) Place a trifecta bet")
        print("\t4) Place a trifectabox bet")
        print("\t5) See your USD balance")
        print("\t6) Exit")

        process_selection(input(), user, self)

def process_selection(value, user, menu):
    clear_screen()
    
    try:
        match int(value):
            case 1:
                betting.Bet("exacta", user)
                return menu.draw_menu(user)
            case 2:
                betting.Bet("exactabox", user)
                return menu.draw_menu(user)
            case 3:
                betting.Bet("trifecta", user)
                return menu.draw_menu(user)
            case 4:
                betting.Bet("trifectabox", user)
                return menu.draw_menu(user)
            case 5:
                print(f"Your USD balance is ${user.money}\n")
                menu_return(menu, user)
            case 6:
                print(f"Your final balance: ${user.money}")
                print("See ya next time!")
                import sys
                sys.exit()
            case _:
                print("Invalid option. Please select a valid menu item.")
                return menu.draw_menu(user)

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.\n")
        menu_return(menu, user)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        menu_return(menu, user)

def menu_return(menu, user):
    print("Press Enter to return to the menu...", end="")
    input()
    clear_screen()
    return menu.draw_menu(user)