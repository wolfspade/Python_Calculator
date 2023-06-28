# Making a Calculator with GUI and Python
 
# Importing Tkinter
from tkinter import *

# The Expression wrote
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    
    # Update the expression by set method
    equation.set(expression)

# Function to clear the text entry box
def clear():
    global expression
    expression = ""
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    # Try and expect for zero division error
    
    try:
        global expression
        
        total = str(eval(expression))
        # Update the expression by using set method
        equation.set(total)
        
        # Intialize the expression variable by empty string
        expression = ""
        
    except:
        equation.set("error")
        expression = ""
                

# Main Driver Code
if __name__ == "__main__":
    # Create the Gui Window
    gui = Tk()
    # Give a title
    gui.title("Calculator")
    # setting the background Colour of gui Window
    gui.configure(background="light green")
    # GUI Dimension using geometry method
    gui.geometry("270x150")
    # Create an instance of the StringVar() class
    equation = StringVar()
    # Create a text Entry
    expression_field = Entry(gui, textvariable=equation )
    # Grid method used for placing the widgets at respective position
    expression_field.grid(columnspan=5,ipadx=60)
    #Button1
    button1 = Button(gui, text= "1",fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    button1.grid(row=1, column=0)
    #Button2
    button2 = Button(gui, text= "2",fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    button2.grid(row=1, column=1)
    #Button3
    button3 = Button(gui, text= "3",fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    button3.grid(row=1, column=2)
    #Button4
    button4 = Button(gui, text= "4",fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    button4.grid(row=2, column=0)
    #Button5
    button5 = Button(gui, text= "5",fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=2, column=1)
    #Button6
    button6 = Button(gui, text= "6",fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    button6.grid(row=2, column=2)
    #Button7
    button7 = Button(gui, text= "7",fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    button7.grid(row=3, column=0)
    #Button8
    button8 = Button(gui, text= "8",fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    button8.grid(row=3, column=1)
    #Button9
    button9 = Button(gui, text= "9",fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    button9.grid(row=3, column=2)
    #Zero Button
    buttonZero = Button(gui, text= "0",fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    buttonZero.grid(row=4, column=0)
    #EqualsButton
    equalsButton = Button(gui, text= "=",fg='black', bg='red', command=lambda: equalpress(), height=1, width=7)
    equalsButton.grid(row=4, column=1)
    #ClearButton
    clearButton = Button(gui, text= "Clear",fg='black', bg='red', command=lambda: clear(), height=1, width=7)
    clearButton.grid(row=4, column=2)
    #plus Button
    buttonPlus = Button(gui, text= "+",fg='black', bg='red', command=lambda: press('+'), height=1, width=7)
    buttonPlus.grid(row=1, column=4)
    #minus Button
    buttonMinus = Button(gui, text= "-",fg='black', bg='red', command=lambda: press('-'), height=1, width=7)
    buttonMinus.grid(row=2, column=4)
    #multiply Button
    buttonMultiply = Button(gui, text= "*",fg='black', bg='red', command=lambda: press('*'), height=1, width=7)
    buttonMultiply.grid(row=3, column=4)
    #divide Button
    buttonDivide = Button(gui, text= "/",fg='black', bg='red', command=lambda: press('/'), height=1, width=7)
    buttonDivide.grid(row=4, column=4)
    
    # GUI mainloop methods    
    gui.mainloop()


    
    




