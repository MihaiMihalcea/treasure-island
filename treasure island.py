print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.") 


crossroad = input("You find yourself at a crossroad, which road do you take? Left or Right? ")
if crossroad.lower() == 'right':
    print("Oh no! You've reached a dead end. Game Over!")
if crossroad.lower() == 'left':
    print("Your instincts turned out to be great as you manage to go past a forrest.")
    river = input("You've stumbled upon a riverbed. Do you swim across or you wait for a boat to arrive? Swim or Wait? ")
    if river.lower() == 'swim':
        print("You've made a terrible choice as the river was full of crocodiles. Game Over!")
    elif river.lower() == 'wait':
        print("Your patience is rewarded as a fisherman finally arrives and he willingly takes you across the river.")
        house = input("You finally reached the X on the map and it's a house, but it has 3 doors, which do you open? Red, Blue or Yellow? ")
        if house.lower() == 'red':
            print("The red door opens and slams shut behind you while you suddenly catch fire. Game over!")
        elif house.lower() == 'blue':
            print("The blue door opens and slams shut behind you while glowy eyes stare at you from the darkness. Game Over!")
        elif house.lower() == 'yellow':
            print("The yellow door opens and you're immediately covered in yellowy light emmanating from the chests filled with coins. You win!")
