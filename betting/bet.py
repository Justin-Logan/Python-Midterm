from utils.utilities import clear_screen

class Bet:
    def __init__(self, bet_type, user):

        from race.race import Race
        race = Race(4)
        race.shuffle()
        cheat = race.horses
    
        bet_costs = {
            "exacta": 15,
            "exactabox": 10,
            "trifecta": 20,
            "trifectabox": 18
        }

        bet_payouts = {
            "exacta": 150,
            "exactabox": 100,
            "trifecta": 250,
            "trifectabox": 180
        }

        if bet_type not in bet_costs:
            print("Invalid bet type!")
            return
        
        if user.money < bet_costs[bet_type]:
            print("You do not have enough money to place this bet!")
            input("Press enter to continue...")
            clear_screen()
            return

        print(f"CHEAT: {cheat}")

        while True:
            choice = input("Enter your horse selections (1-4, space-separated): ")
            user.picks = choice.split()

            if len(user.picks) < 1 or len(user.picks) > 4:
                print("You must enter at least one horse and no more than four, with each separated by a space.")
                print("Press enter to continue", end="")
                input()
                clear_screen()
                continue

            try:
                if all(1 <= int(num) <= 4 for num in user.picks) and len(set(user.picks)) == len(user.picks):
                    user.picks = [f"Horse {num}" for num in user.picks]
                    print(f"You selected horses: {user.picks}")
                    break
                else:
                    print("Please enter choices between numbers 1 and 4 only, and each number must be unique.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
            
            print("Press enter to continue", end="")
            input()
            clear_screen()

        user.money -= bet_costs[bet_type]

        print(f"The race result was: {race.horses}")

        winnings = 0

        match bet_type:
            case "exacta":
                if user.picks[:2] == race.horses[:2]:
                    winnings = bet_payouts["exacta"]
            case "exactabox":
                if set(user.picks[:2]) == set(race.horses[:2]):
                    winnings = bet_payouts["exactabox"]
            case "trifecta":
                if user.picks[:3] == race.horses[:3]:
                    winnings = bet_payouts["trifecta"]
            case "trifectabox":
                if set(user.picks[:3]) == set(race.horses[:3]):
                    winnings = bet_payouts["trifectabox"]


        user.money += winnings

        if winnings > 0:
            print(f"You won ${winnings} dollars!")
        else:
            print("You did not win this time.")

        print("Press enter to continue ", end="")
        input()
        clear_screen()
