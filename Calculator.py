from tkinter import *
root = Tk()

# window configuration
root.title("Calculator")
root.iconbitmap('calc.ico')
root.config(bg="gray79")

# Entry widget to display the value
e = Entry(root, width=60, borderwidth=10)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

operation = ""
f_num = ""

# This will take what we have clicked and show it to the entry accordingly
def button_click(first_number):
    # To get the value which is pressed on the entry widget
    already_in = e.get()
    # To clear the entry field
    e.delete(0, END)
    # To store value together with currently pressed value
    e.insert(0, str(already_in) + str(first_number))

# This will perform our add operation
def button_add():
    global f_num, operation
    # The first number is what is currently on the field
    f_num = e.get()
    # we update the operation global variable for it to be used on the equal function
    operation = "addition"
    e.delete(0, END)

# To perform Subtraction
def button_subtract():
    global f_num, operation
    f_num = e.get()
    operation = "subtraction"
    e.delete(0, END)

# To perform multiply
def button_multiply():
    global f_num, operation
    f_num = e.get()
    operation = "multiply"
    e.delete(0, END)

# To perform division
def button_divide():
    global f_num, operation
    f_num = e.get()
    operation = "divide"
    e.delete(0, END)

# To display the answer in the widget after clicking equal button.
def button_equal():
    if operation == "addition":
        answer = int(f_num) + int(e.get())
    elif operation == "subtraction":
        answer = int(f_num) - int(e.get())
    elif operation == "multiply":
        answer = int(f_num) * int(e.get())
    else:
        answer = int(f_num) / int(e.get())
    # Deleting the what ever is in entry before showing answer
    e.delete(0, END)
    e.insert(0, answer)


def button_clear():
    e.delete(0, END)


frame = LabelFrame(root, bg="gray5")
frame.grid()
button_1 = Button(frame, font=("Cambria"), bg="gray75", text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(frame, font=("Cambria"), bg="gray75", text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(frame, font=("Cambria"), bg="gray75", text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(frame, font=("Cambria"), bg="gray75", text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(frame, font=("Cambria"), bg="gray75", text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(frame, font=("Cambria"), bg="gray75", text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(frame, font=("Cambria"), bg="gray75", text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(frame, font=("Cambria"), bg="gray75", text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(frame, font=("Cambria"), bg="gray75", text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(frame, font=("Cambria"), bg="gray75", text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(frame, text="+", bg="gray70", font=("Cambria"), padx=40, pady=20, command=button_add)
button_subtract = Button(frame, text="-", bg="gray70", font=("Cambria"), padx=42, pady=20, command=button_subtract)
button_multiply = Button(frame, text="*", bg="gray70", font=("Cambria"), padx=42, pady=20, command=button_multiply)
button_divide = Button(frame, text="/", bg="gray70", font=("Cambria"), padx=41, pady=20, command=button_divide)
button_equal = Button(frame, text="=", bg="gray70", font=("Cambria"), padx=41, pady=20, command=button_equal)
button_clear = Button(frame, text="C", font=("Cambria"), bg="gray46", fg="black", padx=41, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=4)

button_clear.grid(row=1, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=2, column=4)
button_add.grid(row=4, column=2)
button_subtract.grid(row=4, column=0)

root.mainloop()
