import tkinter as tk
import json

def clr():
    global form1, form2, form3, form4, form5, form6, form7, form8
    form1.delete(0, tk.END)
    form2.delete(0, tk.END)
    form3.delete(0, tk.END)
    form4.delete(0, tk.END)
    form5.delete(0, tk.END)
    form6.delete(0, tk.END)
    form7.delete(0, tk.END)
    form8.delete(0, tk.END)
    
def send():
    global form1, form2, form3, form4, form5, form6, form7, form8
    result = {}
    result["Имя"] = form1.get()
    result["Фамилия"] = form2.get()
    result["Адрес 1"] = form3.get()
    result["Адрес 2"] = form4.get()
    result["Город"] = form5.get()
    result["Регион"] = form6.get()
    result["Почтовый индекс"] = form7.get()
    result["Страна"] = form8.get()
    clr()
    with open("./Lesson6_Tkinter/form.json", "w") as file:
        json.dump(result, file)

window = tk.Tk()
window.geometry("340x220")

text_width, entry_width = 20, 30

text1 = tk.Label(
    text = "Имя:",
    justify = "right",
    width=text_width,
)
text2 = tk.Label(
    text = "Фамилия:",
    justify = "right",
    width=text_width,
)
text3 = tk.Label(
    text = "Адрес 1:",
    justify = "right",
    width=text_width,
)
text4 = tk.Label(
    text = "Адрес 2:",
    justify = "right",
    width=text_width,
)
text5 = tk.Label(
    text = "Город:",
    justify = "right",
    width=text_width,
)
text6 = tk.Label(
    text = "Регион:",
    justify = "right",
    width=text_width,
)
text7 = tk.Label(
    text = "Почтовый индекс:",
    justify = "right",
    width=text_width,
)
text8 = tk.Label(
    text = "Страна:",
    justify = "right",
    width=text_width,
)

form1 = tk.Entry(
    width=entry_width,
)
form2 = tk.Entry(
    width=entry_width,
)
form3 = tk.Entry(
    width=entry_width,
)
form4 = tk.Entry(
    width=entry_width,
)
form5 = tk.Entry(
    width=entry_width,
)
form6 = tk.Entry(
    width=entry_width,
)
form7 = tk.Entry(
    width=entry_width,
)
form8 = tk.Entry(
    width=entry_width,
)

bt1 = tk.Button(
    text="Очистить",
    width=10,
    height=1,
    command=clr
)

bt2 = tk.Button(
    text="Отправить",
    width=10,
    height=1,
    command=send
)

text1.grid(row=0, column=0)
text2.grid(row=1, column=0)
text3.grid(row=2, column=0)
text4.grid(row=3, column=0)
text5.grid(row=4, column=0)
text6.grid(row=5, column=0)
text7.grid(row=6, column=0)
text8.grid(row=7, column=0)

form1.grid(row=0, column=1, pady=2)
form2.grid(row=1, column=1, pady=2)
form3.grid(row=2, column=1, pady=2)
form4.grid(row=3, column=1, pady=2)
form5.grid(row=4, column=1, pady=2)
form6.grid(row=5, column=1, pady=2)
form7.grid(row=6, column=1, pady=2)
form8.grid(row=7, column=1, pady=2)

bt1.place(x=150, y=190)
bt2.place(x=250, y=190)

window.mainloop()
