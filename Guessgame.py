guess_word="Life"
guess_count=1
guess_limit=4
while(guess_count<=guess_limit):
    guess=input("Enter your guess word :")
    
    if(guess.casefold()==guess_word.casefold()):
        print("You Won !")
        break
    else:
        print("Try Again !")
        guess_count+=1
        guesses_left=guess_limit-guess_count
        if(guesses_left>0):
            print("You now have "+str(guesses_left)+" attempts left")
        else:
            print("You Lost !. Try your luck better next time !")
            break
        