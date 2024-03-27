import tkinter as tk

def kukni_zatvorky(vyraz: str)->bool:
    bracket_counter=0
    for i in vyraz:
        if i=="(":
            bracket_counter+=1
        elif i==")":
            bracket_counter-=1
            if bracket_counter<0:
                return False
    return True if bracket_counter==0 else False

def create_vyraz(vyraz: str):
    global colors
    lave_zatvorky=[]
    pis_sirka=20
    y=pis_sirka//2
    color_num=0
    for i in range(len(vyraz)):
        x=i*pis_sirka
        letter=vyraz[i]
        temp=canvas.create_text(x + 10, y, text=letter, font=f"Helvetica {pis_sirka}", anchor="nw")
        if letter=='(':
            lave_zatvorky.append(temp)
            canvas.itemconfig(temp, fill=colors[color_num])
            color_num+=1
        elif letter==')':
            color=canvas.itemcget(lave_zatvorky[-1], "fill")
            canvas.itemconfig(temp, fill=color)
            lave_zatvorky.pop()

root=tk.Tk()

canvas=tk.Canvas(root, width=600, height=100, bg="white")
canvas.pack()

colors=["red","orange","cyan","green","blue","purple","pink"]
vyraz="(2x+y)-x+5(x(x+8))+y"

check=kukni_zatvorky(vyraz)
if check:
    create_vyraz(vyraz)

root.mainloop()
