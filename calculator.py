from tkinter import *

# # displayed entry
# global entry
entry = StringVar()

# these functions will be called by button commands and should prevent the user from writing an incalculable string in the entry variable
def write_num(num):
    entryTemp = entry.get()
    entryTemp += num
    entry.set(entryTemp)
    print(entry)

def write_op(sym):
    if entry[-1] in ('1','2','3','4','5','6','7','8','9','0'):
        entry += sym

def clear_label():
    entry = ''

def backspace():
    entry = entry[:-1]


root = Tk(className='Calculator')

# settings: size of window
HEIGHT = 233
WIDTH = 144

# settings: button color
numcolor = 'lightgray'
othercolor = 'lightblue'
clickcolor = 'orange'

# button padding 
bpad = 1

# canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='darkblue')
# canvas.pack()

upper_frame = Frame(root, bg='gray', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor="n")

button_frame = Frame(root, bg="gray", bd=5)
button_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor="n")

# widgets: buttons and a label
label = Label(upper_frame, bg='lightgray', font=('Narkism',14), text=entry)
button1 = Button(button_frame, text='0', bg=numcolor, activebackground=clickcolor, command=write_num('0'))
button2 = Button(button_frame, text='.', bg=numcolor, activebackground=clickcolor, command=write_op('.'))
button3 = Button(button_frame, text='+', bg=othercolor, activebackground=clickcolor, command=write_op('+'))
button4 = Button(button_frame, text='=', bg=othercolor, activebackground=clickcolor, command=write_op('='))
button5 = Button(button_frame, text='1', bg=numcolor, activebackground=clickcolor, command=write_num('1'))
button6 = Button(button_frame, text='2', bg=numcolor, activebackground=clickcolor, command=write_num('2'))
button7 = Button(button_frame, text='3', bg=numcolor, activebackground=clickcolor, command=write_num('3'))
button8 = Button(button_frame, text='-', bg=othercolor, activebackground=clickcolor, command=write_op('-'))
button9 = Button(button_frame, text='4', bg=numcolor, activebackground=clickcolor, command=write_num('4'))
button10 = Button(button_frame, text='5', bg=numcolor, activebackground=clickcolor, command=write_num('5'))
button11 = Button(button_frame, text='6', bg=numcolor, activebackground=clickcolor, command=write_num('6'))
button12 = Button(button_frame, text='*', bg=othercolor, activebackground=clickcolor, command=write_op('*'))
button13 = Button(button_frame, text='1/x', bg=othercolor, activebackground=clickcolor)
button14 = Button(button_frame, text='7', bg=numcolor, activebackground=clickcolor, command=write_num('7'))
button15 = Button(button_frame, text='8', bg=numcolor, activebackground=clickcolor, command=write_num('8'))
button16 = Button(button_frame, text='9', bg=numcolor, activebackground=clickcolor, command=write_num('9'))
button17 = Button(button_frame, text='/', bg=othercolor, activebackground=clickcolor, command=write_op('/'))
button18 = Button(button_frame, text='%', bg=othercolor, activebackground=clickcolor)
button19 = Button(button_frame, text=chr(27), bg=othercolor, activebackground=clickcolor, command=backspace)
button20 = Button(button_frame, text='clear', bg=othercolor, activebackground=clickcolor, command=clear_label)
button21 = Button(button_frame, text='+-', bg=othercolor, activebackground=clickcolor)
button22 = Button(button_frame, text='sqrt', bg=othercolor, activebackground=clickcolor)

# place widgets
label.place(relwidth=0.9, relheight=0.9, relx=0.5, rely=0.5, anchor='center')
button1.grid(row=4, column=0, sticky=NSEW, padx=bpad, pady=bpad, columns=2)
button2.grid(row=4, column=2, sticky=NSEW, padx=bpad, pady=bpad)
button3.grid(row=4, column=3, sticky=NSEW, padx=bpad, pady=bpad)
button4.grid(row=3, column=4, sticky=NSEW, padx=bpad, pady=bpad, rows=2)
button5.grid(row=3, column=0, sticky=NSEW, padx=bpad, pady=bpad)
button6.grid(row=3, column=1, sticky=NSEW, padx=bpad, pady=bpad)
button7.grid(row=3, column=2, sticky=NSEW, padx=bpad, pady=bpad)
button8.grid(row=3, column=3, sticky=NSEW, padx=bpad, pady=bpad)
button9.grid(row=2, column=0, sticky=NSEW, padx=bpad, pady=bpad)
button10.grid(row=2, column=1, sticky=NSEW, padx=bpad, pady=bpad)
button11.grid(row=2, column=2, sticky=NSEW, padx=bpad, pady=bpad)
button12.grid(row=2, column=3, sticky=NSEW, padx=bpad, pady=bpad)
button13.grid(row=2, column=4, sticky=NSEW, padx=bpad, pady=bpad)
button14.grid(row=1, column=0, sticky=NSEW, padx=bpad, pady=bpad)
button15.grid(row=1, column=1, sticky=NSEW, padx=bpad, pady=bpad)
button16.grid(row=1, column=2, sticky=NSEW, padx=bpad, pady=bpad)
button17.grid(row=1, column=3, sticky=NSEW, padx=bpad, pady=bpad)
button18.grid(row=1, column=4, sticky=NSEW, padx=bpad, pady=bpad)
button19.grid(row=0, column=0, sticky=NSEW, padx=bpad, pady=bpad)
button20.grid(row=0, column=1, sticky=NSEW, padx=bpad, pady=bpad, columns=2)
button21.grid(row=0, column=3, sticky=NSEW, padx=bpad, pady=bpad)
button22.grid(row=0, column=4, sticky=NSEW, padx=bpad, pady=bpad)

# below code and "sticky" settings above will make buttons sized relative to button_frame
for i in range(21):
    exec('button_frame.grid_columnconfigure('+str(i)+',weight=1)')
    exec('button_frame.grid_rowconfigure('+str(i)+',weight=1)')



root.mainloop()

