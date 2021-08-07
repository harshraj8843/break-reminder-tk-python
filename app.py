 #!/bin/python3

# to show window icon in ubuntu
import os
import sys

# tkinter import
from tkinter import *

# time import
from time import time

# to play sound
from playsound import playsound

# function to find remaining time in hours minutes seconds
def remaining_time(time):
    if(time <= 60):
        res = str(time) + " Seconds"
        return res
    if(time > 60 and time <= 3600):
        minutes = time // 60
        seconds = time % 60
        res = str(minutes) + " Min " + str(seconds) + " Sec"
        return res
    if(time > 3600):
        hours = time // 3600
        temp_min = time % 3600
        minutes = temp_min // 60
        seconds = temp_min % 60
        res = str(hours) + " Hrs " + str(minutes) + " Min " + str(seconds) + " Sec"
        return res

# create window
window = Tk()

# window title
window.title("Break Reminder")

# window property
window.geometry("500x400")
window.configure(bg="white")

# 'break after' label
label1 = Label(window, text="Break after :", background="white")
label1.place(x=70, y=100)

# hours input (default=0)
entry1 = Entry(window)
entry1.insert(END, "0")
entry1.place(x=170, y=100, width=50)

# 'hrs' text label
label2 = Label(window, text="Hrs", background="white")
label2.place(x=220, y=100)

# minutes input (default=0)
entry2 = Entry(window)
entry2.insert(END, "0")
entry2.place(x=250, y=100, width=50)

# 'minutes' text label
label3 = Label(window, text="Minutes", background="white")
label3.place(x=300, y=100)

# seconds input (default=5)
entry3 = Entry(window)
entry3.insert(END, "5")
entry3.place(x=370, y=100, width=50)

# 'seconds' text label
label4 = Label(window, text="Seconds", background="white")
label4.place(x=420, y=100)

# declaring timer text to "" to hide it at first run
timer_text = ""

# timer label (to show remaining time)
label5 = Label(window, text=timer_text, background="white")
label5.place(x=170, y=250)

# default button text
btn_text = "Start"

# timer is off by default
timer = False

# declaring start time for function
start_time = time()

# start timer function
def start_fn():
    # global variables
    global btn_text
    global timer
    global start_time

    # change button property
    btn_text = "Stop"
    btn.configure( bg="red", text = btn_text)

    # disable inputs
    entry1.config(state='disabled')
    entry2.config(state='disabled')
    entry3.config(state='disabled')

    # start timer
    timer = True
    start_time = time()
    timer_cycle()

def play_sound():
    # play sound after timer stops, to notify user
    playsound('./sound/bell.wav')

# stop timer function
def stop_fn():
    # global variables
    global btn_text
    global timer
    global start_time

    # change button property
    btn_text = "Start"
    btn.configure( bg="lightgreen", text = btn_text)

    # enable inputs
    entry1.config(state='normal')
    entry2.config(state='normal')
    entry3.config(state='normal')

    # stop timer
    timer = False
    start_time = time()

    # play sound to notify user
    play_sound()

# button click function
def clicked():
    global btn_text
    
    # if timer is not running
    if btn_text == "Start":
        start_fn()

    # timer stopped
    else:   
        stop_fn()
        # if stop button is clicked, hide timer text
        label5.configure(text="")

# timer function
def timer_cycle():
    global timer

    # if timer is running
    if timer:
        now = time()
        timeDifference = int(now - start_time)
        total_time = int(entry1.get())*60*60+int(entry2.get())*60+int(entry3.get())
        rem_time = total_time - timeDifference

        # if timer completes
        if rem_time == 0:

            # display message
            label5.configure(text="   Break Time !!!")
            
            # stop timer function call
            stop_fn()

            # deiconify window (if iconified) & move window to top
            # i.e. window will be visible to user (if it is minimized or in background)
            window.withdraw()
            window.deiconify()
        
        # if timer doesn't complete, return the remaining time
        else:
            final_time = remaining_time(rem_time)
            label5.configure(text="Remaining time : "+str(final_time))

    # update timer after 1 second
    window.after(1000, timer_cycle)

# stop/start button
btn = Button(window, text=btn_text, bg="lightgreen", command=clicked)
btn.place(x=200, y=200)

# fixed window size
window.resizable(False, False)

# adding icon to window
program_directory=sys.path[0]
window.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "./icon/bell.png")))

# mainloop
window.mainloop()

# Enjoy it #