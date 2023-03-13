print("Welcome to Game Zone Application designed by Malika and Mishty \n\n")
print("Enter 1 to play tic tac toe game")
print("Enter 2 to play Quiz game")
inp = int(input())
if(inp==1):
    print("--------###################-------")
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    player = 1  

    ########win Flags##########    
    Win = 1    
    Draw = -1    
    Running = 0    
    Stop = 1    
    ###########################    
    Game = Running    
    Mark = 'X'    

    #This Function Draws Game Board    
    def DrawBoard():    
        print(" 1 %c | 2 %c | 3 %c " % (board[1],board[2],board[3]))    
        print("_____|_____|_____")    
        print(" 4 %c | 5 %c | 6 %c " % (board[4],board[5],board[6]))    
        print("_____|_____|_____") 
        print(" 7 %c | 8 %c | 9 %c " % (board[7],board[8],board[9]))    
        print("     |     |     ")    

    #This Function Checks position is empty or not    
    def CheckPosition(x):    
        if(board[x] == ' '):    
            return True    
        else:    
            return False    

    #This Function Checks player has won or not    
    def CheckWin():    
        global Game    
        #Horizontal winning condition    
        if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
            Game = Win    
        elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
            Game = Win    
        elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
            Game = Win    
        #Vertical Winning Condition    
        elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
            Game = Win    
        elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
            Game = Win    
        elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
            Game=Win    
        #Diagonal Winning Condition    
        elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
            Game = Win    
        elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
            Game=Win    
        #Match Tie or Draw Condition    
        elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
            Game=Draw    
        else:            
            Game=Running    

    print("Welcome to Tic-Tac-Toe Game Designed By Malika And Mishty")
    print("Enter name of Player 1 : ")
    player1 = input()
    print("Enter name of Player 2 : ")
    player2 = input()
    print("Player 1 [X] --- Player 2 [O]\n")    
    print()    
    print()    
    print("Please Wait...")      
    while(Game == Running):    
        DrawBoard()    
        if(player % 2 != 0):    
            print("\n"+player1+"'s chance")    
            Mark = 'X'    
        else:    
            print("\n"+player2+"'s chance")    
            Mark = 'O'    
        choice = int(input("Enter the position between [1-9] where you want to mark : "))    
        if(CheckPosition(choice)):    
            board[choice] = Mark    
            player+=1    
            CheckWin()    
        else:
            print("\n !!!!!!!!!   You entered wrong input !!!!!!")
    DrawBoard()    
    if(Game==Draw):    
        print("Game Draw")    
    elif(Game==Win):    
        player-=1    
    if(player%2!=0):    
        print("\n\n"+player1+" Won")    
    else:    
        print("\n\n"+player2+" Won")    
else:
    print("Welcome to Quiz game designed by Malika and Mishty")
    from tkinter import *
    from tkinter import ttk
    y=0
    a=ttk.Notebook()
    frame1=ttk.Frame(a)
    frame2=ttk.Frame(a)
    frame3=ttk.Frame(a)
    frame4=ttk.Frame(a)
    frame5=ttk.Frame(a)

    root=ttk.Frame(a)

    def quiz(y):
        a.add(frame1, text="Q1")
        a.add(frame2, text="Q2")
        a.add(frame3, text="Q3")
        a.add(frame4, text="Q4")
        a.add(frame5, text="Q5")

        Label(frame1, text="Total keywords in Python ?",font=("Arial",50,"bold")).grid(row=2,column=2)
        Button(frame1, text="33",font=("Arial",30,"bold"),bg="light blue",command=a1_right).grid(row=3,column=1)
        Button(frame1, text="31",font=("Arial",30,"bold"),bg="light green",command=a1_wrong).grid(row=3,column=2)
        Button(frame1, text="30",font=("Arial",30,"bold"),bg="light pink",command=a1_wrong).grid(row=3,column=3)

        Label(frame2, text="Output of 2**3 ?",font=("Arial",50,"bold")).grid(row=2,column=2)
        Button(frame2, text="6",font=("Arial",30,"bold"),bg="light blue",command=a2_wrong).grid(row=3,column=1)
        Button(frame2, text="8",font=("Arial",30,"bold"),bg="light green",command=a2_right).grid(row=3,column=2)
        Button(frame2, text="9",font=("Arial",30,"bold"),bg="light pink",command=a2_wrong).grid(row=3,column=3)

        Label(frame3, text="Output of np.arange(1,5)",font=("Arial",50,"bold")).grid(row=2,column=2)
        Button(frame3, text="[1,2,3,4]",font=("Arial",30,"bold"),bg="light blue",command=a3_right).grid(row=3,column=1)
        Button(frame3, text="[0,1,2,3,4]",font=("Arial",30,"bold"),bg="light green",command=a3_wrong).grid(row=3,column=2)
        Button(frame3, text="[1,2,3,4,5]",font=("Arial",30,"bold"),bg="light pink",command=a3_wrong).grid(row=3,column=3)

        Label(frame4, text="Keyword use to declare a function ?",font=("Arial",50,"bold")).grid(row=2,column=2)
        Button(frame4, text="define",font=("Arial",30,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=1)
        Button(frame4, text="def",font=("Arial",30,"bold"),bg="light green",command=a4_right).grid(row=3,column=2)
        Button(frame4, text="none",font=("Arial",30,"bold"),bg="light pink",command=a4_wrong).grid(row=3,column=3)

        Label(frame5, text="Output of 2*12 ?",font=("Arial",50,"bold")).grid(row=2,column=2)
        Button(frame5, text="24",font=("Arial",30,"bold"),bg="light blue",command=a5_right).grid(row=3,column=1)
        Button(frame5, text="28",font=("Arial",30,"bold"),bg="light green",command=a5_wrong).grid(row=3,column=2)
        Button(frame5, text="32",font=("Arial",30,"bold"),bg="light pink",command=a5_wrong).grid(row=3,column=3)

    def a1_right():
        Label(frame1,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
        Label(frame1,text="Marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a1_wrong():
        Label(frame1,text="Incorrect",font=("Arial",40,"bold"),background="red",fg="yellow").grid(row=1,column=2)
        Label(frame1,text="Marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a2_right():
        Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
        Label(frame2,text="Marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a2_wrong():
        Label(frame2,text="Incorrect",font=("Arial",40,"bold"),background="red",fg="yellow").grid(row=1,column=2)
        Label(frame2,text="Marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a3_right():
        Label(frame3,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
        Label(frame3,text="Marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a3_wrong():
        Label(frame3,text="Incorrect",font=("Arial",40,"bold"),background="red",fg="yellow").grid(row=1,column=2)
        Label(frame3,text="Marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a4_right():
        Label(frame4,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
        Label(frame4,text="Marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a4_wrong():
        Label(frame4,text="Incorrect",font=("Arial",40,"bold"),background="red",fg="yellow").grid(row=1,column=2)
        Label(frame4,text="Marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a5_right():
        Label(frame5,text="Correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
        Label(frame5,text="Marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

    def a5_wrong():
        Label(frame5,text="Incorrect",font=("Arial",40,"bold"),background="red",fg="yellow").grid(row=1,column=2)
        Label(frame5,text="Marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)


    quiz(y)
    a.pack()
    a.mainloop()


    
    root.mainloop()
