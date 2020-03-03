from random import randint
Actual = randint(1,101) 
guesses= [] 
Actual
print("hi, \n There is a number from 1 to 100, \n Try to  guess it, \n Good luck. ")
g= input()
Guess=int(g)
while Guess!=Actual:
    guesses.append(Guess)
    if Guess>=1 and Guess<=100:
        if len(guesses)!=1:  
            if abs(Actual-guesses[len(guesses)-1])<abs(Actual-guesses[len(guesses)-2]):
                print(' you are closer to target ')
                g= input()
                Guess=int(g) 
            elif abs(Actual-guesses[len(guesses)-1])>abs(Actual-guesses[len(guesses)-2]):
                print(' you are far from the target ')
                g= input()
                Guess=int(g)
            elif abs(Actual-guesses[len(guesses)-1])==abs(Actual-guesses[len(guesses)-2]):   
                if (guesses[len(guesses)-1])!=(guesses[len(guesses)-2]): 
                    print('you became neither closer to nor far from the right number')
                    g= input()
                    Guess=int(g)   
                else:
                    print("Don't be Idiot, this value is as same as the previous one")
                    g= input()
                    Guess=int(g)
        else:
            print(' Try again ')
            g= input()
            Guess=int(g)    
    else:
        print("OUT OF BOUNDS")
        g= input()
        Guess=int(g)
    
    
              
else:
    guesses.append(Guess)
    print("Wow, you've guessed Correctly this time \n You have guessed it in {} times \n GAME OVER".format(len(guesses)))

    
    
