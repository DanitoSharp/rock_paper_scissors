import random

# Created the game in a function
def rock_paper_Scissors():
    # Use a loop to hold my games logic
    while(True):
        # user gets prompted to start or quit the game
        print("Start new game... Start (y) or Quit (n)")
        res = input()
        relis = ["y", "n"]
        if(res.lower() == "n"):
            break
        elif(res.lower() not in relis):
            print("Error, Invaild input!")
            print()
            input("press \"enter\" to try again!")
            continue
        
        # used a second loop to keep asking player for the correct input
        # and retry automatically if player and cpu ties
        while(True):
            print("let's play!")
            print("Pick an option between \"R\"(Rock), \"P\"(Paper) or \"S\"(Scissors)")
            hand = input()
            signs = ["r", "p", "s"]
            
            if(hand.lower() not in signs):
                print("Error, Invaild sign!")
                print()
                input("press \"enter\" to try again!")
                continue
            
            # used a random choice generator for the CPU
            cpu = random.choice(signs)

            if(hand.lower() == cpu):
                print("it's a tie!")
                print()
                input("press \"enter\" to try again!")
                continue
            else:
                if(hand == "r" and cpu == "s"):
                    print("You(Rock) beats CPU(Scissors), you won!")
                    print()
                    input("press \"enter\"")
                    break
                if(hand == "r" and cpu == "p"):
                    print("Oh, CPU(Paper) covers You(Rock), you lost!")
                    print()
                    input("press \"enter\"")
                    break
                if(hand == "s" and cpu == "r"):
                    print("Oh, CPU(Rock) beats You(Scissors), you lost!")
                    print()
                    input("press \"enter\"")
                    break
                if(hand == "s" and cpu == "p"):
                    print("You(Scissors) cuts CPU(Paper), you won!")
                    print()
                    input("press \"enter\"")
                    break
                if(hand == "p" and cpu == "r"):
                    print("You(Paper) covers CPU(Rock), you won!")
                    print()
                    input("press \"enter\"")
                    break
                if(hand == "p" and cpu == "s"):
                    print("Oh, CPU(Scissors) cuts You(Paper), you lost!")
                    print()
                    input("press \"enter\"")
                    break

# Done, function gets called to run the game.
rock_paper_Scissors()