
import random
import tkinter
root = tkinter.Tk()
root.geometry('600x600')
root.title('Welcome to Dice roll simulator')


#label to print result
label = tkinter.Label(root, text='', font=('Arial', 260))
l2 = tkinter.Label(root,text="****************Welcome to Dice Rolling Game*****************", foreground='#7D35D6',font=("Pristina",50, "bold"))



def roll_dice():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result=random.choice(value)
    label.configure(text=result ,justify='center')
    label.pack()
    if(result=='\u2680'):
        label3=tkinter.Label(root,text='You rolled a one! Click roll dice to roll again.',font=("Courier New",20))
        label3.place(x=150,y=450)
    elif(result=='\u2681'):
        label3=tkinter.Label(root,text='You rolled a two! Click roll dice to roll again.',font=("Courier New",20))
        label3.place(x=150,y=450)
    elif(result=='\u2682'):
        label3=tkinter.Label(root,text='You rolled a three! Click roll dice to roll again.',font=("Courier New",20))
        label3.place(x=150,y=450)
    elif(result=='\u2683'):
        label3=tkinter.Label(root,text='You rolled a four! Click roll dice to roll again.',font=("Courier New",20))
        label3.place(x=150,y=450)
    elif(result=='\u2684'):
        label3=tkinter.Label(root,text='You rolled a five! Click roll dice to roll again.',font=("Courier New",20))
        label3.place(x=150,y=450)
    elif(result=='\u2685'):
        label3=tkinter.Label(root,text='You rolled a six! Click roll dice to roll again.',font=("Courier New",20))
        label3.place(x=150,y=450)
button = tkinter.Button(root, text='roll dice', foreground='Green', command=roll_dice,font=("Comic Sans MS", 15, "bold"))
button.pack()
l2.pack()
root.mainloop()
