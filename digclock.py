from tkinter import *
from time import strftime

# Create window
root = Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.configure(bg="black")

# Function to update time
def time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%d / %m / %Y')

    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    clock_label.after(1000, time)

# Clock label
clock_label = Label(
    root,
    font=("Arial", 50, "bold"),
    background="black",
    foreground="cyan"
)

clock_label.pack(pady=20)

# Date label
date_label = Label(
    root,
    font=("Arial", 25),
    background="black",
    foreground="white"
)

date_label.pack()

# Call function
time()

# Run window
root.mainloop()
