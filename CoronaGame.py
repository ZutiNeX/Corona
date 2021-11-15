print('''
Welcome To CoronaVirus Simulator Created By ZutiNeX

In This Program We Are Going To Ask Some Questions

And You Have To Select Correct Answers For It...

Or You Can Call It Text-Based-Adventure Game

Lets Go!!!
''')

print(".\n.\n.")

#Login 
inp = input("Enter your name: ")
print(f"Welcome to the game, {inp}")

#Game 
def fir_ques():
 while(True):
    ans = "Mask"
    guess = ""
    opt = ['1.Mask', '2.Clothes on face', '3.Handkercheif']
    while guess != ans:
        for a in opt:
            print(a)
        guess = input(f"What's recommended to wear while going outside home during pandemic time, {inp}: ")
        if(guess==ans):
            print("Yes you are right, we should wear mask during pandemic!")
            return True
        else:
            print("Check the spelling or you have entered the invalid answer!")
            # return False

fir_ques()

print(".\n.\n.")

def sec_ques():
    while(True):
        ans1 = "COVID-19"
        guess1 = ""
        opt1 = ['1.COVID-19', '2.Coved', 'Codiv']
        while guess1 != ans1:
            for b in opt1:
                print(b)
            guess1 = input(f"What is CoronaVirus-19 short form, {inp}: ")
            if(guess1==ans1):
                print("Yes you are right, COVID-19 is the short form for CoronaVirus-19")
                return True
            elif(guess1=='Coved'):
                print("You are not right Coved isnt the right answer")
            elif(guess1=='Codiv'):
                print("You are not right Codiv isnt the right answer")
            else:
                print("Check the spelling or you have entered the invalid answer!")


sec_ques()

print(".\n.\n.")

def thir_ques():
    while(True):
        ans2 = "Sanitizer"
        guess2 = ""
        opt2 = ["1.Sanitizer", "2.Normal Water", "3.HandWash"]
        while guess2!= ans2:
            for c in opt2:
                print(c)
            guess2 = input(f"What is preffered in pandemic {inp}: ")
            if(guess2==ans2):
                print("Yes you are right, Sanitizer is preffered more than handwash and Normal Water")
                return True
            elif(guess2=='Normal Water'):
                print("You are not right, Normal Water isnt preffered much :(")
            elif(guess2=="Handwash"):
                print("Pretty close, but sorry you are wrong")
            else:
                print("Check the spelling or you have entered the invalid answer!")

thir_ques()

print(".\n.\n.")

def ask_():
    n  = input(f"Are you enjoying the game so far, {inp} ") 
    # ret = print("Sorry")
    if(n=='Yes'):
        print("Thanks!")
    if(n=='No'):
        print(f"Sorry {inp}")
        quit()

ask_()

print(".\n.\n.")#Add this before every function 

def last_ques():
 while(True):
    anslast = "True"
    guesslast = ""
    optlast = ['1.True', '2.False']
    while guesslast != anslast:
        for l in optlast:
            print(l)
        guesslast = input(f"Should we avoid crowd or not {inp} ")
        if(guesslast==anslast):
            print("Yes we should avoid crowd")
            return True
        elif(guesslast=="False"):
            print("We should avoid crowd")
            return False
        else:
            print("Wrong!")

last_ques()

print(".\n.\n.")#Add this before every function 

def end():
    print(f"I hope you enjoyed the game {inp}")

end() 
#Game Ends
