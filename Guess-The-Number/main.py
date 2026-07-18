import random

# for continue the game
while True:
    print("guess the number\n  ")
    _rounds = int(input("\nHow many rounds you need? "))
    _guess = 0
    number = random.randint(0, 1000)
    
# finite loop
    while(_guess < _rounds) :
    	_guess = _guess +1
    	print(f"\nyour guess {_guess}" )
	
	#use this to filter invalid input
    	try:
                n = int(input())
            # if input numbet is greater
                if n > number :
                    if n - number > 100:
                        print("too high")
                    elif n - number >10:
                        print("high")
                    elif n - number > 0:
                        print("high but too close")
            # if input number is smaller
                elif n < number :
                    if number - n > 100:
                        print("too low")
                    elif number - n > 10:
                        print("low")
                    elif number - n > 0:
                        print("low but too close")
            # if input number is equal
                else:
                    print("You guessed it right!")
                    break
    # use this to don't break the loop
    	except ValueError:
                print("Invalid choice")
                continue

    if _guess == _rounds and n != number:
        print(f"Sorry, you failed.\nThe number was {number}")
    choice = input("Do you want to continue: y/n   ").lower()
    if choice == "y" :
        continue
    else:
        print("Thanks for playing")
        break