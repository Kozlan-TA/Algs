import tkinter as tk

def decrease():
    global clicks, label
    if clicks > 0:
        clicks -= 1
    label["text"] = str(clicks)

def increase():
    global clicks, label
    clicks += 1
    label["text"] = str(clicks)

clicks = 0
window = tk.Tk()
button1 = tk.Button(
    text = "-",
    width=15,
    height=7,
    command = decrease,
)

button2 = tk.Button(
    text = "+",
    width=15,
    height=7,
    command = increase,
)

label = tk.Label(
    text = str(clicks),
    width=15,
    height=7,
)

button1.grid(row=0, column=0)
label.grid(row=0, column=1)
button2.grid(row=0, column=2)

window.mainloop()
