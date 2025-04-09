#import all from Tkinter
#import math libray
from tkinter import *;
import math;

#functions
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def buttonPressed(num):
    global equation_Text; #global variable for display label
    equation_Text = equation_Text + str(num);# take display values as a string and store it.
    equation_label.set(equation_Text); #setting the global variable value to the display label
#-----------------------------------------------------------------------------------------------------------------------
def btnClear():
    global equation_Text;
    equation_label.set("");#make clear the current display value
    equation_Text = "";#make clear the current display label variable
#-----------------------------------------------------------------------------------------------------------------------
def equals():
    global equation_Text;
    try:#exception handling for unnecessary errors
        total = str(eval(equation_Text));
        equation_label.set(total);
        equation_Text = total;

    except SyntaxError:#unnecessary user inputs handling
        equation_label.set("SyntaxError!");
    except ZeroDivisionError:#invalid arithmatic error handling
        equation_label.set("Arithmatic Error!")
#-----------------------------------------------------------------------------------------------------------------------
def sqr():

    try:
        global equation_Text;
        curr_val = float(equation_label.get());#take display value as float
        result = str(math.sqrt(curr_val));#calculate square root and casting to string
        equation_label.set(result);
        equation_Text = result;
    except ValueError:
        equation_label.set("Cannot Perform that Operation!");#handling user's invalid inputs


#-----------------------------------------------------------------------------------------------------------------------
def pow2():
    try:
        global equation_Text;
        curr_val = float(equation_label.get());
        result = str(math.pow(curr_val, 2));#make given number to the power of 2 and casting to String
        equation_label.set(result);
        equation_Text = result;
    except ValueError:
        equation_label.set("Cannot Perform that Operation!");

    except OverflowError: #overflow error handling
        equation_label.set("OverFlow! \n cannot Perform that much!");





#-----------------------------------------------------------------------------------------------------------------------
def expo():
    try:
        global equation_Text;
        curr_val = float(equation_label.get());
        result = str(math.exp(curr_val));#make exponential value and casting to string
        equation_label.set(result);
        equation_Text = result;
    except ValueError:
        equation_label.set("Cannot Perform that Operation!");
    except OverflowError:
        equation_label.set("OverFlow! \n cannot Perform that much!");

#-----------------------------------------------------------------------------------------------------------------------
#memory store function
def memPlus():

    try:
        global mem_text;
        mem_text = mem_text + float(equation_label.get());
        result = str(mem_text);
        mem_label.set(result);
    except ValueError:
        equation_label.set("ValueError!\n Clear the console and type again");

#-----------------------------------------------------------------------------------------------------------------------

#memory deduction function
def memMinus():

    try:
        global mem_text;
        mem_text = mem_text - float(equation_label.get());
        result = str(mem_text);
        mem_label.set(result);
    except ValueError:
        equation_label.set("ValueError!\n Clear the console and type again");
#-----------------------------------------------------------------------------------------------------------------------
#memory clear function
def memClear():
    global mem_text;
    mem_text =0;
    result = str(mem_text);
    mem_label.set(result);
#-----------------------------------------------------------------------------------------------------------------------
#memroy recall function
def memRecall():
    global mem_text;
    global equation_Text;
    equation_Text = equation_Text + str(mem_text);
    equation_label.set(equation_Text);

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

mainWindow = Tk(); #creating an instance/object from Tk
mainWindow.title("Calculator 1.0");#title name window
mainWindow.geometry("450x550")#basic width and height
mainWindow.resizable(False,False);                #szsing off from both x and y axis
titleIcon = PhotoImage(file='images/images.png');#importing necessary image to the title
mainWindow.iconphoto(True,titleIcon);#make title image set and true
mainWindow.config(bg='#AEDEFC');#main window background color

equation_Text = ""; #global variable that store display values
equation_label = StringVar(); #make label as Stringvar type

#display label making a label with configuration font, color etc.
#after creating we need to pack the label to the window with extra padding x and y
display_label = Label(mainWindow, textvariable=equation_label, font=('consolas', 15), fg='BLACK', bg="#C5BAFF", width=50, height=3);
display_label.pack(padx=10, pady=10);
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#memory buttons
#memeory Frame creation
memBtnFrame = Frame(mainWindow, bg='#AEDEFC', width=370, height=35);
memBtnFrame.pack(padx=10, pady=10);


#memory buttons creation
#button name, sizes and command to perform when clicked
buttonMemPlus = Button(memBtnFrame, text='M+', font=10, bg='red', height=1,width=4, command=memPlus);
buttonMemPlus.grid(row=0, column=1, padx=15, pady=0);#adjusting the layout position

buttonMemMinus = Button(memBtnFrame, text='M-', bg='red', height=1,width=4, font=10, command=memMinus);
buttonMemMinus.grid(row=0, column=4, padx=15, pady=0);

buttonMemClear = Button(memBtnFrame, text='MCE', bg='red', height=1,width=4, font=10, command=memClear);
buttonMemClear.grid(row=0, column=2, padx=15, pady=0);

buttonMemRecall = Button(memBtnFrame, text='MR', bg='red', height=1,width=4, font=10, command=memRecall);
buttonMemRecall.grid(row=0, column=3, padx=15, pady=0);






#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#buttons
#buttons frame
buttonFrame = Frame(mainWindow, bg="#79D7BE", width=370, height=350);
buttonFrame.pack();

#buttons
buttonNum7 = Button(buttonFrame, bg='#4F75FF', text=7, height=3, width=7, font=35, command=lambda: buttonPressed('7'));
buttonNum7.grid(row=0, column=1, padx=5, pady=5);

buttonNum8 = Button(buttonFrame, bg='#4F75FF', text=8, height=3, width=7, font=35, command=lambda: buttonPressed('8'));
buttonNum8.grid(row=0, column=2, padx=5, pady=5);

buttonNum9 = Button(buttonFrame, bg='#4F75FF', text=9, height=3, width=7, font=35, command=lambda: buttonPressed('9'));
buttonNum9.grid(row=0, column=3,padx=5, pady=5);

buttonNum4 = Button(buttonFrame, bg='#4F75FF', text=4, height=3, width=7, font=35, command=lambda: buttonPressed('4'));
buttonNum4.grid(row=1, column=1,padx=5, pady=5);

buttonNum5 = Button(buttonFrame, bg='#4F75FF', text=5, height=3, width=7, font=35, command=lambda: buttonPressed('5'));
buttonNum5.grid(row=1, column=2,padx=5, pady=5);

buttonNum6 = Button(buttonFrame, bg='#4F75FF', text=6, height=3, width=7, font=35, command=lambda: buttonPressed('6'));
buttonNum6.grid(row=1, column=3,padx=5, pady=5);

buttonNum1 = Button(buttonFrame, bg='#4F75FF', text=1, height=3, width=7, font=35, command=lambda: buttonPressed('1'));
buttonNum1.grid(row=2, column=1,padx=5, pady=5);

buttonNum2 = Button(buttonFrame, bg='#4F75FF', text=2, height=3, width=7, font=35, command=lambda: buttonPressed('2'));
buttonNum2.grid(row=2, column=2,padx=5, pady=5);

buttonNum3 = Button(buttonFrame, bg='#4F75FF', text=3, height=3, width=7, font=35, command=lambda: buttonPressed('3'));
buttonNum3.grid(row=2, column=3,padx=5, pady=5);

buttonNum0 = Button(buttonFrame, bg='#4F75FF', text=0, height=3, width=7, font=35, command=lambda: buttonPressed('0'));
buttonNum0.grid(row=3, column=2,padx=5, pady=5);

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#operators
#lambda uses to make readable and handling several event handling tasks simpler and easier.

buttonClr = Button(buttonFrame, bg='#EB5A3C', text='CE', height=3, width=7, font=35, command= lambda :btnClear());
buttonClr.grid(row=0, column=4,padx=5, pady=5);

buttonMul = Button(buttonFrame, bg='#EB5A3C', text='*', height=3, width=7, font=35, command=lambda: buttonPressed('*'));
buttonMul.grid(row=1, column=4,padx=5, pady=5);

buttonDiv = Button(buttonFrame, bg='#EB5A3C', text='/', height=3, width=7, font=35, command=lambda: buttonPressed('/'));
buttonDiv.grid(row=2, column=4,padx=5, pady=5);

buttonSub = Button(buttonFrame, bg='#EB5A3C', text='-', height=3, width=7, font=35, command=lambda: buttonPressed('-'));
buttonSub.grid(row=3, column=4,padx=5, pady=5);

buttonDeci = Button(buttonFrame, bg='#1230AE', text='.', height=3, width=7, font=60, command=lambda: buttonPressed('.'));
buttonDeci.grid(row=3, column=1,padx=5, pady=5);

buttonSum = Button(buttonFrame, bg='#1230AE', text='=', height=3, width=7, font=35, command=lambda: equals());
buttonSum.grid(row=3, column=3,padx=5, pady=5);

buttonAdd = Button(buttonFrame, bg='#EB5A3C', text='+', height=3, width=7, font=35, command=lambda: buttonPressed('+'));
buttonAdd.grid(row=2, column=5,padx=5, pady=5);

buttonPow = Button(buttonFrame, bg='#EB5A3C', text='Pow(2)', height=3, width=7, font=35, command=pow2);
buttonPow.grid(row=3, column=5,padx=5, pady=5);

buttonEx = Button(buttonFrame, bg='#EB5A3C', text='e', height=3, width=7, font=35, command= expo);
buttonEx.grid(row=1, column=5,padx=5, pady=5);

buttonSqr = Button(buttonFrame, bg='#EB5A3C', text='SQR', height=3, width=7, font=35, command=sqr);
buttonSqr.grid(row=0, column=5,padx=5, pady=5);

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#memory label-------------------
mem_text=0.0;#initilazing mem_text value
mem_label = StringVar();

memDisplay_label = Label(mainWindow, textvariable=mem_label, font=('consolas', 20), fg='red', bg="#4B164C", width=27, height=2 );
memDisplay_label.pack(padx=10, pady=10);


mainWindow.mainloop();#the event loop which creates the window, starts the whole program and execute functions and GUI and at the end terminate the program