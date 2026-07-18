#  snake gun water

# we will use  random so we cannot know computer choice
import random
list = [ 's', 'w', 'g']

chance = int(input(" Number of round: "))
no_chance = 0
computer_point = 0
human_point = 0

print(" use 's' for snake 'g' for gun 'w' for water ")

#loop body
while no_chance < chance:
    no_chance = no_chance + 1
    print(f"\nround {no_chance}")
    _input  = input()
    _random = random.choice(list)
    
    # for tie
    if _input == _random:
        print("tie")
        print(f"you choose {_input} and computer choose {_random}")
    # for human choose Snake
    elif _random == "w"  and _input == "s"  :
        print("human wins")
        print(f"you choose {_input} and computer choose {_random}")
        human_point = human_point +1
        
    elif _random == "g"  and _input == "s"  :
        print("computer wins")
        print(f"you choose {_input} and computer choose {_random}")
        computer_point = computer_point +1
    # for human choose Water
    elif _random == "g"  and _input == "w" :
        print("human wins")
        print(f"you choose {_input} and computer choose {_random}")
        human_point = human_point +1
        
    elif _random == "s" and _input == "w" :
        print("computer wins")
        print(f"you choose {_input} and computer choose {_random}")
        computer_point = computer_point +1 
    # for human choose Gun
    elif _random == "s"  and _input == "g" :
        print("human wins")
        print(f"you choose {_input} and computer choose {_random}")
        human_point = human_point +1
        
    elif _random == "w" and _input == "g" :
        print("computer wins")
        print(f"you choose {_input} and computer choose {_random}")
        computer_point = computer_point +1
        
    #incase unauthorised choice is taken
    else:
        print(" Invalid choice ")

#score print and winner anouncement
if int(human_point) > int(computer_point):
    print("\n\nvictor: human" )
    
elif int(human_point) < int(computer_point):
    print("\n\nvictor: computer" )

elif int(human_point) == int(computer_point):
    print("\n\nDraw")

print(f"\nyour score {human_point}\ncomputer score {computer_point}")