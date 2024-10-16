import tkinter as tk

def upd():
    global text, label2, far
    try:
        far = (float(text.get()) - 32) * 5 / 9
    except:
        far = None
    finally:
        label2["text"] = f"{far:.1f}°C" if far != None else " "

window = tk.Tk()

far = None

button = tk.Button(
    text = "->",
    width=4,
    height=2,
    command = upd,
)

text = tk.Entry(

)

label1 = tk.Label(
    text = "°F",
    width=6,
    height=3,
)

label2 = tk.Label(
    text = f"{far:.1f}°C" if far != None else " ",
    width=10,
    height=6,
)

text.grid(row=0, column=0, padx=15)
label1.grid(row=0, column=1)
button.grid(row=0, column=2, padx=10, pady=6)
label2.grid(row=0, column=3)

window.mainloop()
