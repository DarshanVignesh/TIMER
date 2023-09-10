from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
reps=0
time=None
def countdown(n):
    min=math.floor(n/60)
    sec=n%60
    if sec<10:
        sec=f"0{sec}"
    if n>=0:
     canvas.itemconfig(timer,text=f"{min}:{sec}")
     global time
     time=window.after(1000,countdown,n-1)
    else:
        start()

def start():
    global reps
    reps=reps+1
    work_sec=WORK_MIN*60
    break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        countdown(long_break_sec)
        timer_label.config(text="Long break",fg=GREEN)
    elif reps%2==0:
        countdown(break_sec)
        timer_label.config(text="Short break",fg=GREEN)
    else:
        countdown(work_sec)
        check_mark.config(text="✔")
        timer_label.config(text="Work now",fg=RED)

def reset():
    window.after_cancel(time)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer,text="00:00")
    global reps
    reps=0

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.config(padx=100,pady=50)

#creating canvas

canvas=Canvas(height=224,width=200,bg=YELLOW ,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


timer_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),highlightthickness=0,bg=YELLOW)
timer_label.config(fg=GREEN)
timer_label.grid(row=0,column=1)

start_button=Button(text="Start",font=(FONT_NAME,10,"bold"),fg=RED,command=start)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",font=(FONT_NAME,10,"bold"),fg=RED,command=reset)
reset_button.grid(column=2,row=2)

check_mark=Label(font=(FONT_NAME,10,"bold"),fg="green")
check_mark.grid(column=1,row=3)










window.mainloop()