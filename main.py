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
reps = 0
clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clock():
    global reps, clock
    window.after_cancel(clock)
    timer.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
    ticks.delete("1.0", END)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        timer.config(text='LONG BREAK', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        timer.config(text='SHORT BREAK', fg=PINK)
    else:
        countdown(WORK_MIN*60)
        timer.config(text='WORK YOUR ASS OFF', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global clock
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0:
    #     count_sec = "00"
    # if count_min == 0:
    #     count_min = "00"
    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        clock = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_ses = math.floor(reps / 2)
        marks = ""
        for i in range(work_ses):
            marks += "✓"
        ticks.delete("1.0", END)
        ticks.insert(END, marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(bg=YELLOW, padx=100, pady=50)

im = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=im)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(row=1, column=1)

# labels
timer = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

# buttons
start = Button(text='Start', width=10, fg=GREEN, bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW,
               command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', width=10, fg=GREEN, highlightthickness=0, highlightbackground=YELLOW,command=reset_clock)
reset.grid(row=2, column=2)


# text
def add_tick():
    ticks.insert(END, tb)


tb = "✓"
ticks = Text(width=10, height=10, highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
ticks.grid(row=3, column=1)

window.mainloop()
