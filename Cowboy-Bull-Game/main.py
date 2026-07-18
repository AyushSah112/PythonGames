#Cow Bull Game 🐮
import random
print("🤠 Howdy, Partner!\nA sneaky outlaw has hidden a secret number.\nTrack it down using Cows 🐮 and Bulls 🐂.\nDraw your guess!")
def difficulty() :
    dif = int(input("Select your difficulty:\n1 for easy\n2 for medium\n3 for hard\n"))
    if dif == 1:
        digit = 3
    elif dif == 2:
        digit = 4
    elif dif == 3:
        digit = 5
    else:
        print("invalid input")
    return digit

def secret_generator(digit) :
    secret = str(random.randint(10**(digit - 1), (10**digit - 1)))
    return secret
    
def play() :
    digit = difficulty()
    secret = secret_generator(digit)
    
    n = 0
    while True:
        cow = 0
        bull = 0
        
        n +=1
        guess = input(f"Round {n} : ")
       
        if len(guess) != digit or not guess.isdigit() :
            print("Please enter a Valid input")
            continue 
            
        for i in range(digit):
            if guess[i] == secret[i] :
                cow += 1
            elif guess[i] in secret:
                bull +=1 

        print(f" {cow} cow, {bull} bull")
        
        if cow == digit:
            if n == 1:
                print("🏆 LEGENDARY!\nYou cracked the code on your first try!")
            else:
                print(f"Congratulations, partner! You guessed it right\nNumber of attempts you take {n}" )
            break
            
while True:
    play()
    choice = input("Do you want to play again? y/n  ")
    
    if choice != "y":
        print("🤠 Thanks for riding with us, partner!\nUntil our trails cross again... Happy Guessing!")
        break
        