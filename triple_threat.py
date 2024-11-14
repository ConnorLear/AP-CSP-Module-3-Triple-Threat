"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Name - Month Year
"""

def pay_out(randomthingy):
    print("Casino pays out: $"+d1*bp)
    casino_prof -= randomthingy
    print("Profit: $"+casino_prof)

import random

bp: int = 10
casino_prof: int = 0
cost_to_play: int = 1
player_paid: int = 0

person: str = input("Who do you want to play as(Player/Casino): ")

if person == "Casino":
    conformation = input(f"Did the person play(Yes/No): ").lower()
    if conformation == "yes":
        while conformation == "yes":
            player_paid += cost_to_play
            print("Casino collects: $"+player_paid)
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            d3 = random.randint(1,6)
            print("Person rolled:",d1+"-"+d2+"-"+d3)
            if d1 == d2 == d3:
                if d1 == 1:
                    pay_out(9)
                elif d1 == 2:
                    pay_out(19)
                elif d1 == 3:
                    pay_out(29)
                elif d1 == 4:
                    pay_out(39)
                elif d1 == 5:
                    pay_out(49)
                else:
                    pay_out(99)
            else:
                print("You get: $0")
                casino_prof += cost_to_play
                print("Casino profit:", casino_prof)

    else:
        print("Ok")
else:
    conformation = input(f"Do you want to play for ${cost_to_play}(Yes/No): ").lower()
    if conformation == "yes":
        while conformation == "yes":
            player_paid += cost_to_play
            print("Casino collects: $"+player_paid)
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            d3 = random.randint(1,6)
            print("Person rolled:",d1+"-"+d2+"-"+d3)
            if d1 == d2 == d3:
                if d1 == 1:
                    pay_out(9)
                elif d1 == 2:
                    pay_out(19)
                elif d1 == 3:
                    pay_out(29)
                elif d1 == 4:
                    pay_out(39)
                elif d1 == 5:
                    pay_out(49)
                else:
                    pay_out(99)
            else:
                print("You get: $0")
                casino_prof += cost_to_play
                print("Casino profit:", casino_prof)