import tkinter as tk
import random
matches=[]

def create_match():
    x=10+10*len(matches)+10*(len(matches)+1)
    stick=canvas.create_line(x,50,x,150,width=5,fill='yellow')
    head=canvas.create_oval(x-5, 45, x+5, 55, fill='brown', outline='brown')
    return [stick,head]

def remove_match(num):
    for i in range(num):
        canvas.delete(matches.pop())
    player[0], player[1]=player[1], player[0]
    canvas.itemconfig(stats, text=f'Taha hrac {player[0]}\nPocet zapaliek: {len(matches)}')
    if len(matches)==0:
        canvas.delete('all')
        canvas.create_text(650//2, 100, text=f"Hrac cislo {player[1]} vyhrava!", font=('Helvetica', 30))

root=tk.Tk()
canvas=tk.Canvas(root, width=650, height=200)
canvas.pack()
player=[1, 2]
matches=[create_match() for _ in range(15)]

stats=canvas.create_text(650//2, 15, text=f'Ide hrac cislo {player[0]}\nPocet zapaliek: {len(matches)}', anchor='center', font=('Helvetica', 15))

root.bind('1', lambda x: remove_match(1))
root.bind('2', lambda x: remove_match(2))
root.bind('3', lambda x: remove_match(3))

root.mainloop()
