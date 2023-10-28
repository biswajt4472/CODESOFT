import tkinter as tk

def button_click(num):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(num))

def button_clear():
    display.delete(0, tk.END)

def button_equals():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

window = tk.Tk()
window.title("Calculator")
window.configure(background='black')


display = tk.Entry(window, width=100)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


button_1 = tk.Button(window, text="1", padx=40, pady=20,background='#007BFF', command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, background='#007BFF',command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20,background='#007BFF', command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, background='#007BFF',command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20,background='#007BFF', command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20,background='#007BFF', command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20,background='#007BFF', command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20,background='#007BFF', command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20,background='#007BFF', command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20,background='#007BFF', command=lambda: button_click(0))
button_ = tk.Button(window, text=".", padx=41, pady=20, background='#999e99',command=lambda: button_click('.'))


button_1.grid(row=5, column=1)
button_2.grid(row=5, column=2)
button_3.grid(row=5, column=3)
button_4.grid(row=4, column=1)
button_5.grid(row=4, column=2)
button_6.grid(row=4, column=3)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)
button_0.grid(row=6, column=2)
button_.grid(row=7, column=1)


button_add = tk.Button(window, text="+", padx=40, pady=20, background='#808080', command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=40, pady=20,  background='#808080',command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=40, pady=20,  background='#808080',command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=40, pady=20,  background='#808080',command=lambda: button_click("/"))
button__ = tk.Button(window, text="%", padx=40, pady=20, background='#808080',command=lambda: button_click('%'))


button_add.grid(row=1, column=0)
button_subtract.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=1, column=3)
button__.grid(row=1, column=4)

button_clear = tk.Button(window, text="Clear", padx=30, pady=20,background='red',command=button_clear)
button_equals = tk.Button(window, text="=",padx=40, pady=20, background='#61ed81',command=button_equals)

button_clear.grid(row=7, column=3)
button_equals.grid(row=7, column=2)

window.mainloop()