import random

def sng():
    U=0
    C=0
    opt=["ROCK","PAPER","SCISSOR"]

    print('Choose either ROCK or PAPER or SCISSOR')
    print("Type FINISH to end the game")
    while True:
     u=input('enter your choice from the above :- ').upper()
     if(u=="ROCK" or u=="PAPER" or u=="SCISSOR"):
        c=random.choice(opt)
        print(f"computer choose {c}")
        if(u=="ROCK"):  
            if(c=="ROCK"):
                print("round tied")
            elif(c=="PAPER"):
                print("computer won")
                C+=1      
            else:       
                print("you won")
                U+=1 
        elif(u=="PAPER"):  
            if(c=="PAPER"):
                print("round tied")
            elif(c=="SCISSOR"):
                print("computer won")
                C+=1      
            else:       
                print("you won")
                U+=1   
        else:  
            if(c=="SCISSOR"):
                print("round tied")
            elif(c=="ROCK"):
                print("computer won")
                C+=1      
            else:       
                print("you won")
                U+=1   
        print(f"computer score = {C} and your score = {U}\n")
#finish
     elif(u=="FINISH"):
        print(f"your score :- {U}\n computer's score :- {C}\n")
        if(U>C):
            print("you won")
        elif(U==C):
            print("it's a tie")
        else:
            print("computer won")
        break
     else:  
            print("Invalid Input\n")
            continue

sng()