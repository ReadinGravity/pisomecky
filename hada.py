import tkinter as tk
win=tk.Tk()
canvas=tk.Canvas(win, width=400, height=400)
canvas.pack()

def up(event): #<Up>
    global direction
    direction=[0,-1]

def down(event): #<Down>
    global direction
    direction=[0,1]

def left(event): #<Left>
    global direction
    direction=[-1,0]

def right(event): #<Right>
    global direction
    direction=[1,0]

def inc(event): #speed increase, "a"
    global speed
    if speed>10:
        speed-=10

def dec(event): #speed decrease, "d"
    global speed
    speed+=10

def pohyb():
    global direction, head, snake, speed
    canvas.create_rectangle(head[0], head[1], head[0]+1, head[1]+1, fill='black')
    head[0]+=direction[0]
    head[1]+=direction[1]
    if head in snake:
        canvas.create_text(400//2, 100, text="GAME OVER!", font=('Arial',40), fill="red")
        return
    snake.append([head[0], head[1]])
    canvas.after(speed, pohyb)


speed=50
direction=[0,-1]
head=[500//2, 500//2]
snake=[[500//2, 500//2]]

win.bind("<Up>", up)
win.bind("<Left>", left)
win.bind("<Down>", down)
win.bind("<Right>", right)

win.bind("a", inc)
win.bind("d", dec)
pohyb()

win.mainloop()
