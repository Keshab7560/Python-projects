import tkinter as tk
import time

def start_timer():
    try:
        seconds = int(entry.get())
        if seconds <= 0:
            raise ValueError("Please enter a positive integer.")
        for i in range(seconds, -1, -1):
            timer_label.config(text=f"Time left: {i} seconds")
            root.update()
            time.sleep(1)
        timer_label.config(text="Time's up!")
    except ValueError:
        pass

root = tk.Tk()
root.title("Countdown Timer")

label = tk.Label(root, text="Enter time (in seconds):")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

timer_label = tk.Label(root, text="")
timer_label.pack()

root.mainloop()
