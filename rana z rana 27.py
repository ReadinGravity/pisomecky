import tkinter as tk

def kukni_zatvorky (vyraz:str)->bool:
     zatvorkovac = 0
    for i in vyraz:
        if i == '(':
            zatvorkovac+=1
        elif i == ')':
            zatvorkovac-=1
            if zatvorkovac < 0:
                return False
    return True if bracket_counter == 0 else False

def create_vyraz (vyraz: str)
    global colors
    lave_zatvorky= []
    sirka_pismena = 20
    y = sirka_pismena//2
    color_num = 0

for i in range(len(vyraz)):
    x=i*sirka_pismena
    pismeno=vyraz[i]
    temp=canvas.create_text(x+10,y,text=pismeno,font=f"Arial {sirka_pismena}", anchor="nw")
        if letter == '(':
            left_brackets.append(temp)
            canvas.itemconfig(temp, fill=colors[color_num])
        elif letter == ')':
            color = canvas.itemcget(left_brackets[-1], 'fill')
            canvas.itemconfig(temp, fill=color)
            left_brackets.pop()

root=tk.Tk()
canvas=tk.Canvas(root, width=600, height=100, bg="white")
canvas.pack()

