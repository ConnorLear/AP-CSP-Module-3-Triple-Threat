"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""


import random

#Values for game
bp: int = 10
casino_prof: int = 0
cost_to_play: int = 1
casino_cash: int = 0
total_player_cash: int = 10
person = "person"

#Game
while not person == "casino" and not person == "player":
    #Chooses what person is playing
    person: str = input("Who do you want to play as(Player/Casino): ").lower()

    #Casino
    if person == "casino":
        #Checks if player wants to play
        conformation = input(f"Did the player play(Y/N): ").lower()
        #Plays if player said yes
        if conformation == "y":
            while conformation == "y":

                print()

                #Gives money to casino
                casino_cash += cost_to_play
                print(f"Casino collects: ${cost_to_play}")

                #Rolls die & returns the rolls
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                d3 = random.randint(1,6)
                print(f"Player rolled: {d1}-{d2}-{d3}")

                #Checks if player won
                if d1 == d2 == d3:
                    if d1 == 1:
                        print(f"Casino pays: ${d1*bp}")
                        casino_prof -= 9
                        print(f"Casino cash: ${casino_prof}")
                    elif d1 == 2:
                        print(f"Casino pays: ${d1*bp}")
                        casino_prof -= 19
                        print(f"Casino cash: ${casino_prof}")
                    elif d1 == 3:
                        print(f"Casino pays: ${d1*bp}")
                        casino_prof -= 29
                        print(f"Casino cash: ${casino_prof}")
                    elif d1 == 4:
                        print(f"Casino pays: ${d1*bp}")
                        casino_prof -= 39
                        print(f"Casino cash: ${casino_prof}")
                    elif d1 == 5:
                        print(f"Casino pays: ${d1*bp}")
                        casino_prof -= 49
                        print(f"Casino cash: ${casino_prof}")
                    else:
                        print(f"Casino pays: ${d1*bp}")
                        casino_prof -= 99
                        print(f"Casino cash: ${casino_prof}")

                #If the test above fails the player losses and this program plays
                else:
                    print("Casino pays: $0")
                    casino_prof += cost_to_play
                    print(f"Casino cash: ${casino_prof}")

                print()

                #Checks again if player wants to play
                conformation = input("Does the player still want to play(Y/N): ").lower()

            #Runs if player done playing
            print("Ok!")
            print(f"Casino gained: ${casino_prof}")
        #Runs if player didn't want to play
        else:
            print("Ok!")

    #Player
    elif person == "player":
        conformation = input(f"Do you want to play for ${cost_to_play}(Y/N): ").lower()
        if conformation == "y":
            while conformation == "y":
                total_player_cash -= cost_to_play
                print()
                print(f"You paid: ${total_player_cash}")
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                d3 = random.randint(1,6)
                print(f"You rolled: {d1}-{d2}-{d3}")
                if d1 == d2 == d3:
                    if d1 == 1:
                        print(f"You earned: ${d1*bp}")
                        total_player_cash += d1*bp
                        print(f"You now have: ${total_player_cash}")
                    elif d1 == 2:
                        print(f"You earned: ${d1*bp}")
                        total_player_cash += d1*bp
                        print(f"You now have: ${total_player_cash}")
                    elif d1 == 3:
                        print(f"You earned: ${d1*bp}")
                        total_player_cash += d1*bp
                        print(f"You now have: ${total_player_cash}")
                    elif d1 == 4:
                        print(f"You earned: ${d1*bp}")
                        total_player_cash += d1*bp
                        print(f"You now have: ${total_player_cash}")
                    elif d1 == 5:
                        print(f"You earned: ${d1*bp}")
                        total_player_cash += d1*bp
                        print(f"You now have: ${total_player_cash}")
                    else:
                        print(f"You earned: ${d1*bp}")
                        total_player_cash += d1*bp
                        print(f"You now have: ${total_player_cash}")
                else:
                    print("You earned: $0")
                    print(f"You now have: ${total_player_cash}")
                print()
                conformation == input("Do you still want to play(Y/N): ").lower()
            print("Ok!")
            print(f"You left with: ${total_player_cash}")
        else:
            print("Ok!")
    else:
        print("Thats not a person you can choose.")