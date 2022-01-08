from tkinter import *
import random

#Random Number
def six():
    return random.randrange(1,7)

def two():
    return random.randrange(0,2)

#Creating window for the game:
window = Tk()
window.title("Handcricket")
window.geometry("600x400")

#Starting Heading
Header = "MENU"
HeaderWidget = Label(window, text = "Handcricket")
HeaderWidget.pack()

#Heading Change
def Heading(Header):
    HeaderWidget.config(text=Header)

#The Game
def Game():
    Play.destroy()
    Exit.destroy()
    result = TossMenu()
    
    #Player won toss or not
    
    if result == 1:
        Match(BatBowl())
    else:
        Match(two())

#Batting
def Bat():
    score = 0
    rand = 0
    choice = IntVar()
    Heading("Batting")
    ScoreWidget = Label(window, text = "Your Score: "+str(score))
    PlayerWidget = Label(window, text = "Your Choice: "+str(choice.get()))
    OpponentWidget = Label(window, text = "Opponent's Choice: "+str(rand))
    ScoreWidget.pack()
    PlayerWidget.pack()
    OpponentWidget.pack()
    c1 = Button(window, text='1',command=lambda: choice.set(1))
    c2 = Button(window, text='2',command=lambda: choice.set(2))
    c3 = Button(window, text='3',command=lambda: choice.set(3))
    c4 = Button(window, text='4',command=lambda: choice.set(4))
    c5 = Button(window, text='5',command=lambda: choice.set(5))
    c6 = Button(window, text='6',command=lambda: choice.set(6))
    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()
    c6.pack()
    while True:
        ScoreWidget.config(text = "Your Score: "+str(score))
        window.wait_variable(choice)
        rand = six()
        if choice.get() == rand:
            break
        else:
            score += choice.get()
        PlayerWidget.config(text = "Your Choice: "+str(choice.get()))
        OpponentWidget.config(text = "Opponent's Choice: "+str(rand))
        
    print("You are out!")
    c1.destroy()
    c2.destroy()
    c3.destroy()
    c4.destroy()
    c5.destroy()
    c6.destroy()
    PlayerWidget.destroy()
    OpponentWidget.destroy()
    return score



#Bowling
def Bowl():
    score = 0
    choice = IntVar()
    Heading("Bowling")
    ScoreWidget = Label(window, text = "Computer's Score: "+str(score))
    ScoreWidget.pack()
    c1 = Button(window, text='1',command=lambda: choice.set(1))
    c2 = Button(window, text='2',command=lambda: choice.set(2))
    c3 = Button(window, text='3',command=lambda: choice.set(3))
    c4 = Button(window, text='4',command=lambda: choice.set(4))
    c5 = Button(window, text='5',command=lambda: choice.set(5))
    c6 = Button(window, text='6',command=lambda: choice.set(6))
    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()
    c6.pack()
    while True:
        ScoreWidget.config(text = "Computer's Score: "+str(score))
        window.wait_variable(choice)
        val = six()
        if choice.get() == val:
            break
        else:
            score += val
    print("Computer is out!")
    c1.destroy()
    c2.destroy()
    c3.destroy()
    c4.destroy()
    c5.destroy()
    c6.destroy()
    return score




def Match(myplay):
    playerscore = 0
    opponentscore = 0
    if myplay == 0:
        print ("You are Batting first")
        playerscore = Bat()
        opponentscore = Bowl()
    else:
        print ("You are Bowling first")
        opponentscore = Bowl()
        playerscore = Bat()

    if (playerscore>opponentscore):
        print("You Win")
    else:
        print ("You Lose")

        

#Toss Menu
def TossMenu():
    choice = IntVar()
    Heading("Heads or Tails?")
    Heads = Button(window, text='Heads',command=lambda: choice.set(0))
    Tails = Button(window, text='Tails',command=lambda: choice.set(1))
    Heads.pack()
    Tails.pack()
    window.wait_variable(choice)
    Heads.destroy()
    Tails.destroy()
    if choice.get() == two():
        #Player wins the toss
        return 1
    else:
        #Player loses the toss
        return 0

#Player chooses whether to start with bowling or batting
def BatBowl():
    choice = IntVar()
    Heading("Do you choose to bat or bowl?")
    Bat = Button(window, text='Bat',command=lambda: choice.set(0))
    Bowl = Button(window, text='Bowl',command=lambda: choice.set(1))
    Bat.pack()
    Bowl.pack()
    window.wait_variable(choice)
    Bat.destroy()
    Bowl.destroy()
    return choice.get()


#Main Menu
Play = Button(window, text='Play',command=lambda: Game())
Play.pack()
Exit = Button(window, text='Exit',command=exit)
Exit.pack()
window.mainloop()
