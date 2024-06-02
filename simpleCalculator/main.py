from tkinter import *

expression = ""




def press(num):

    global expression


    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("error")
        expression = ""

if __name__ == "__main__":

    root = Tk()
    root.title("A simple Calculator")
    root.geometry("500x500")
    root.configure(background="gainsboro")

    equation = StringVar()

    topFrame = Frame(root, background='gainsboro', height=50)
    topFrame.pack(side=TOP, fill=X)

    btmFrame = Frame(root, background='gainsboro', height=00)
    btmFrame.pack(side=BOTTOM, fill=X)

    exp_field = Entry(topFrame, textvariable=equation, width=70, bd=30, insertwidth=4, justify='right')
    exp_field.grid(padx=10, pady=10, columnspan=4)

    #--- ------ button

    btn7 = Button(btmFrame, text='7', fg='black', bg='gainsboro', command=lambda: press(7), height=3, width=13)
    btn7.grid(row=2, column=0, pady=10, padx=10)
    btn8 = Button(btmFrame, text='8', fg='black', bg='gainsboro', command=lambda: press(8), height=3, width=13)
    btn8.grid(row=2, column=1, pady=10, padx=10)
    btn9 = Button(btmFrame, text='9', fg='black', bg='gainsboro', command=lambda: press(9), height=3, width=13)
    btn9.grid(row=2, column=2, pady=10, padx=10)
    btnPlus = Button(btmFrame, text='+', fg='black', bg='gainsboro', command=lambda: press("+"), height=3, width=13)
    btnPlus.grid(row=2, column=3, pady=10, padx=10)

    btn4 = Button(btmFrame, text='4', fg='black', bg='gainsboro', command=lambda: press(4), height=3, width=13)
    btn4.grid(row=3, column=0, pady=10, padx=10)
    btn5 = Button(btmFrame, text='5', fg='black', bg='gainsboro', command=lambda: press(5), height=3, width=13)
    btn5.grid(row=3, column=1, pady=10, padx=10)
    btn6 = Button(btmFrame, text='6', fg='black', bg='gainsboro', command=lambda: press(6), height=3, width=13)
    btn6.grid(row=3, column=2, pady=10, padx=10)
    btnMoins = Button(btmFrame, text='-', fg='black', bg='gainsboro', command=lambda: press("-"), height=3, width=13)
    btnMoins.grid(row=3, column=3, pady=10, padx=10)

    btn1 = Button(btmFrame, text='1', fg='black', bg='gainsboro', command=lambda: press(1), height=3, width=13)
    btn1.grid(row=4, column=0, pady=10, padx=10)
    btn2 = Button(btmFrame, text='2', fg='black', bg='gainsboro', command=lambda: press(2), height=3, width=13)
    btn2.grid(row=4, column=1, pady=10, padx=10)
    btn3 = Button(btmFrame, text='3', fg='black', bg='gainsboro', command=lambda: press(3), height=3, width=13)
    btn3.grid(row=4, column=2, pady=10, padx=10)
    btnMult = Button(btmFrame, text='*', fg='black', bg='gainsboro', command=lambda: press("*"), height=3, width=13)
    btnMult.grid(row=4, column=3, pady=10, padx=10)

    btn0 = Button(btmFrame, text='0', fg='black', bg='gainsboro', command=lambda: press(0), height=3, width=13)
    btn0.grid(row=5, column=0, pady=10, padx=10)
    btnC = Button(btmFrame, text='C', fg='black', bg='gainsboro', command=clear, height=3, width=13)
    btnC.grid(row=5, column=1, pady=10, padx=10)
    btnEqual = Button(btmFrame, text='=', fg='black', bg='gainsboro', command=equalpress, height=3, width=13)
    btnEqual.grid(row=5, column=2, pady=10, padx=10)
    btnDivide = Button(btmFrame, text='/', fg='black', bg='gainsboro', command=lambda: press("/"), height=3, width=13)
    btnDivide.grid(row=5, column=3, pady=10, padx=10)





    root.mainloop()
