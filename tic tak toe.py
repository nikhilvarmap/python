from tkinter import *
player = 'X'
def callb(x,y):
    global player
    if player =='X'and tat[x][y] == 0:
        b[x][y].configure(text = 'X')
        tat[x][y] = 'X'
        player = 'O'
    elif player =='O' and tat[x][y] == 0:
        b[x][y].configure(text = 'O')
        player = 'X'
        tat[x][y] = 'O'
    else:
        pass
root = Tk()
b = [[0,0,0],[0,0,0],[0,0,0]]
tat = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font = ('verdana',56),width =3,bg = 'brown',command = lambda x=i,y=j: callb(x,y))
        b[i][j].grid(row = i,column = j)
mainloop()
    
