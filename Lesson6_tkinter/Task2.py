import tkinter as tk
import random

def gen_num():
    global label
    label["text"] = str(random.randint(1, 6))

window = tk.Tk()
button1 = tk.Button(
    text = "Бросить",
    width=20,
    height=7,
    command = gen_num,
)

label = tk.Label(
    text = " ",
    width=20,
    height=7,
)

button1.grid(row=0, column=0)
label.grid(row=1, column=0)

window.mainloop()
