from datetime import datetime
import random
import time
yourScore = 0
aiScore = 0
round = 1
scissor = 'Scissor'
rock = 'Rock'
paper = 'Paper'
bool = False
while bool == False:
    print("Rock, Paper, Scissors Game")
    print('Round ' + str(round))
    choice = input("Shoot!:")

    if choice.casefold() != paper.casefold() and choice.casefold() != scissor.casefold() \
            and choice.casefold() != rock.casefold():
        print('Invalid choice.')
        continue

    else:
        random.seed(time.time())
        ai = random.randint(1, 600)
        if ai <= 200:
            print('Your opponent chose scissor.')
            if choice.casefold() == paper.casefold():
                aiScore+=1
                print('You lose :(')
            elif choice.casefold() == rock.casefold():
                yourScore+=1
                print('You win!')
            else:
                print('Tie')
        elif 200 < ai <= 400:
            print('Your opponent chose rock')
            if choice.casefold() == paper.casefold():
                yourScore+=1
                print('You win!')
            elif choice.casefold() == scissor.casefold():
                aiScore+=1
                print('You lose :(')
            else:
                print('Tie')
        else:
            print('Your opponent chose paper')
            if choice.casefold() == paper.casefold():
                print('Tie')
            elif choice.casefold() == rock.casefold():
                aiScore+=1
                print('You lose :(')
            else:
                yourScore+=1
                print('You win!')
    print('Current Score: \nYou: ' + str(yourScore) + ' \nAI: ' + str(aiScore))
    con = input('Do you wish to continue?:')
    if 'n' in con:
        bool = True
    else:
        round+=1
