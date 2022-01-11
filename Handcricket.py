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
window.geometry("640x360")

bgframe = Frame(window)
bgframe.pack(side="top", expand=1)
bgframe.place(x= 0, y= 0)
bgimage = PhotoImage(file = 'wallpaper.png')
bgwidget = Label(bgframe, image = bgimage)
bgwidget.pack()

buttonimage = PhotoImage(file = 'button.png')


#Starting Heading
Header = "MENU"
HeaderWidget = Label(window, text = "Handcricket",height = 2, width = 30)
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
    ScoreWidget = Label(window, text = "Your Score: "+str(score), height = 2, width = 20)
    PlayerWidget = Label(window, text = "Your Choice: "+str(choice.get()), height = 2, width = 20)
    OpponentWidget = Label(window, text = "Opponent's Choice: "+str(rand), height = 2, width = 20)
    ScoreWidget.pack()
    PlayerWidget.pack()
    OpponentWidget.pack()
    c1 = Button(window, text='1',command=lambda: choice.set(1), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c2 = Button(window, text='2',command=lambda: choice.set(2), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c3 = Button(window, text='3',command=lambda: choice.set(3), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c4 = Button(window, text='4',command=lambda: choice.set(4), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c5 = Button(window, text='5',command=lambda: choice.set(5), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c6 = Button(window, text='6',command=lambda: choice.set(6), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()
    c6.pack()
    while True:
        ScoreWidget.config(text = "Your Score: "+str(score), height = 2, width = 20)
        window.wait_variable(choice)
        rand = six()
        if choice.get() == rand:
            break
        else:
            score += choice.get()
        PlayerWidget.config(text = "Your Choice: "+str(choice.get()), height = 2, width = 20)
        OpponentWidget.config(text = "Opponent's Choice: "+str(rand), height = 2, width = 20)

    ResultWidget = Label(window, text = "You are out", height = 2, width = 20)
    ResultWidget.pack()
    ContinueButton = Button(window, text='Continue',command=lambda: choice.set(0), height = 20, width = 200, image = buttonimage, compound=CENTER)
    ContinueButton.pack()
    window.wait_variable(choice)
    c1.destroy()
    c2.destroy()
    c3.destroy()
    c4.destroy()
    c5.destroy()
    c6.destroy()
    PlayerWidget.destroy()
    OpponentWidget.destroy()
    ResultWidget.destroy()
    ContinueButton.destroy()
    return score



#Bowling
def Bowl():
    score = 0
    rand = 0
    choice = IntVar()
    Heading("Bowling")
    ScoreWidget = Label(window, text = "Computer's Score: "+str(score), height = 2, width = 20)
    PlayerWidget = Label(window, text = "Your Choice: "+str(choice.get()), height = 2, width = 20)
    OpponentWidget = Label(window, text = "Opponent's Choice: "+str(rand), height = 2, width = 20)
    ScoreWidget.pack()
    PlayerWidget.pack()
    OpponentWidget.pack()
    c1 = Button(window, text='1',command=lambda: choice.set(1), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c2 = Button(window, text='2',command=lambda: choice.set(2), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c3 = Button(window, text='3',command=lambda: choice.set(3), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c4 = Button(window, text='4',command=lambda: choice.set(4), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c5 = Button(window, text='5',command=lambda: choice.set(5), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c6 = Button(window, text='6',command=lambda: choice.set(6), height = 20, width = 200, image = buttonimage, compound=CENTER)
    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()
    c6.pack()
    while True:
        ScoreWidget.config(text = "Computer's Score: "+str(score), height = 2, width = 20)
        window.wait_variable(choice)
        rand = six()
        if choice.get() == rand:
            break
        else:
            score += rand
        PlayerWidget.config(text = "Your Choice: "+str(choice.get()), height = 2, width = 20)
        OpponentWidget.config(text = "Opponent's Choice: "+str(rand), height = 2, width = 20)
    ResultWidget = Label(window, text = "Computer is out", height = 2, width = 20)
    ResultWidget.pack()
    ContinueButton = Button(window, text='Continue',command=lambda: choice.set(0), height = 20, width = 200, image = buttonimage, compound=CENTER)
    ContinueButton.pack()
    window.wait_variable(choice)
    c1.destroy()
    c2.destroy()
    c3.destroy()
    c4.destroy()
    c5.destroy()
    c6.destroy()
    PlayerWidget.destroy()
    OpponentWidget.destroy()
    ResultWidget.destroy()
    ContinueButton.destroy()
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
    
    Heading("Game Over")
    
    if playerscore == opponentscore:
        ResultWidget = Label(window, text = "Draw!", height = 2, width = 20)
        ResultWidget.pack()
    elif playerscore>opponentscore:
        ResultWidget = Label(window, text = "You Win!", height = 2, width = 20)
        ResultWidget.pack()
    else:
        ResultWidget = Label(window, text = "Computer Wins!", height = 2, width = 20)
        ResultWidget.pack()

        

#Toss Menu
def TossMenu():
    choice = IntVar()
    Heading("Heads or Tails?")
    Heads = Button(window, text='Heads',command=lambda: choice.set(0), height = 20, width = 200, image = buttonimage, compound=CENTER)
    Tails = Button(window, text='Tails',command=lambda: choice.set(1), height = 20, width = 200, image = buttonimage, compound=CENTER)
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
    Bat = Button(window, text='Bat',command=lambda: choice.set(0), height = 20, width = 200, image = buttonimage, compound=CENTER)
    Bowl = Button(window, text='Bowl',command=lambda: choice.set(1), height = 20, width = 200, image = buttonimage, compound=CENTER)
    Bat.pack()
    Bowl.pack()
    window.wait_variable(choice)
    Bat.destroy()
    Bowl.destroy()
    return choice.get()


#Main Menu
Play = Button(window, text='Play',command=lambda: Game(), height = 20, width = 200, image = buttonimage, compound=CENTER)
Play.pack()
Exit = Button(window, text='Exit',command=exit, height = 20, width = 200, image = buttonimage, compound=CENTER)
Exit.pack()
window.mainloop()
