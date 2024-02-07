import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

boats = []
winner = []
counter = 0

def plachten(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8, fill=random.choice(colors))


colors = ["#cf2d1b", "#ed6111", "#edc811", "#6ced11", "#11ed8e", "#11abed", "#3511ed", "#af11ed", "#ed118e"]
#          red         orange     yellow     green       mint       blue    dark blue   purple     hot pink
def setup():
    for i in range(15):
        plachten(20,i*40+40)
        boats.append(1+2*i)
    canvas.create_line(650,0,650,700,fill='red')

def pohyb():
    global counter
    for i, j in enumerate(boats):
        line_coord = canvas.coords(j)
        move = random.randint(1,10)
        canvas.delete(j)
        canvas.delete(j+1)
        plachten(line_coord[0]+move, line_coord[1])
        boats[i] += 31 if counter==0 else 30
        if len(canvas.find_overlapping(650, 0, 650, 700))>1:
            winner.append((j-30*counter-1)//2+1)
        if len(canvas.find_overlapping(652, 0, 652, 700)):
            canvas.create_text(350, 350, text='vitaz: lodicka cislo ' + str(winner[0]),
                               font=('Courier', '20'), fill='red', anchor=tk.CENTER)
            return
    counter+=1
    canvas.after(100, pohyb)

def start(e):
    pohyb()

setup()
canvas.bind('<Button-1>',start)
root.mainloop()

