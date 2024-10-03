import tkinter
from tkinter import *
from tkinter import messagebox

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("450x500+200+200")
root.resizable(0,0)
root.title("Calculator")
root.bg = "black"

btnrow00 = Frame(root)
btnrow00.pack(expand = True, fill = "both")

btn00 = Button(
    btnrow00,
    text = "calculator",
    font = ("Verdana", 20),
    height = 1,
    bg = "black",
    fg = "white",
    border = 9,
    relief = RAISED,
    activebackground = "black",
    activeforeground = "white",
    )
btn00.pack(side = LEFT, expand = True, fill = "both",)


val = ""
A = 0
operator = ""


#Hover button
def entered(event):
    btnc.config(bg="blue")

def left(event):
    btnc.config(bg="blue")

def entered_(event):
    btnx.config(bg="blue")

def left_(event):
    btnx.config(bg="blue")



# function for numerical button clicked

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_dot_isclicked():
    global val
    val = val + "."
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_exp_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "^"
    val = val + "^"
    data.set(val)


def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def btn_x_pressed():
    global A,operator,val
    v = val[-1]
    val = val[:len(val)-1]
    if v in ['+','-','*','/',]:
        operator=""
    operator = ""
    data.set(val)


# function to find the result
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = float((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    elif operator == "-":
        x = float((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    elif operator == "*":
        x = float((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    elif operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = A / x
            data.set(C)
    elif operator == "^":
        x = float((val2.split("^")[1]))
        C = A ** x
        val = str(C)
        data.set(val)
    else:
        #print(1)
        if '+' in val2 or '-' in val2 or '*' in val2 or '/' in val2 or '^' in val2:
            return
        #print(2)
        x=float(val2)
        C = x * x
        val = str(C)
        data.set(val)

# the label that shows the result
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 26),
    width = 7,
    textvariable = data,
    background = "black",
    fg = "white",
)
lbl.pack(expand = True, fill = "both")

# the frames section

btnrow0 = Frame(root)
btnrow0.pack(expand = True, fill = "both")

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


# The buttons section
# button for frame 0
btnc = Button(
    btnrow0,
    text = "AC",
    font = ("Verdana", 22),
    bg = "blue",
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)
btnc.bind("<Enter>",entered)
btnc.bind("<Leave>", left)


btnx = Button(
    btnrow0,
    text = "del",
    font = ("Verdana", 22),
    bg="blue",
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_x_pressed,
)
btnx.pack(side = LEFT, expand = True, fill = "both",)
btnx.bind("<Enter>",entered_)
btnx.bind("<Leave>", left_)

btnpower = Button(
    btnrow0,
    text = "exp",
    font = ("Verdana", 22),
    bg = "blue",
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_exp_clicked,
)
btnpower.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow0,
    text = "/",
    font = ("Verdana", 22),
    bg="blue",
    relief = RAISED,
    border = 9,
    width = 2,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)


# button for frame 1
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    bg = "black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    bg = "black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow1,
    text = "*",
    font = ("Verdana", 22),
    bg="blue",
    width = 2,
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black", 
    command = btn_mult_clicked,
)
btnmult.pack(side = LEFT, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    bg="blue",
    width = 2,
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_minus_clicked,
)
btnminus.pack(side = LEFT, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow3,
    text = "+",
    font = ("Verdana", 22),
    bg="blue",
    width = 2,
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_plus_clicked,
)
btnplus.pack(side = LEFT, fill = "both",)



# button for frame4
btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    bg="black",
    fg = "white",
    relief = RAISED,
    border = 9,
    activebackground = "black",
    activeforeground = "white",
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btndot = Button(
    btnrow4,
    text = ".",
    font = ("Verdana", 22),
    bg="blue",
    width = 2,
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = btn_dot_isclicked,
)
btndot.pack(side = LEFT, fill = "both",)


btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    bg="blue",
    width = 2,
    relief = RAISED,
    border = 9,
    activebackground = "blue",
    activeforeground = "black",
    command = result,
)
btnequal.pack(side = LEFT, fill = "both",)

root.mainloop()