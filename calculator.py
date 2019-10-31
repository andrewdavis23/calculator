from tkinter import *

# # displayed entry
# global entry
# entry = ''

def write_num(num):
    label['text'] += num

def write_op(sym):
    if label['text'][-1] not in ('1','2','3','4','5','6','7','8','9','0'):
        label['text'] += sym

root = Tk(className='Calculator')

# size of window
HEIGHT = 377
WIDTH = 233

numcolor = 'lightgray'
othercolor = 'lightblue'
clickcolor = 'orange'

bpad = 1

# canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='darkblue')
# canvas.pack()

upper_frame = Frame(root, bg='gray', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor="n")

frame = Frame(root, bg="gray", bd=5)
frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor="n")

# widgets: buttons and a label
label = Label(upper_frame, bg='lightgray', font=('Narkism',14))
button1 = Button(frame, text='0', bg=numcolor, activebackground=clickcolor, command=write_num('0'))
button2 = Button(frame, text='.', bg=numcolor, activebackground=clickcolor, command=write_op('.'))
button3 = Button(frame, text='+', bg=othercolor, activebackground=clickcolor, command=write_op('+'))
button4 = Button(frame, text='=', bg=othercolor, activebackground=clickcolor, command=write_op('='))
button5 = Button(frame, text='1', bg=numcolor, activebackground=clickcolor, command=write_num('1'))
button6 = Button(frame, text='2', bg=numcolor, activebackground=clickcolor, command=write_num('2'))
button7 = Button(frame, text='3', bg=numcolor, activebackground=clickcolor, command=write_num('3'))
button8 = Button(frame, text='-', bg=othercolor, activebackground=clickcolor, command=write_op('-'))
button9 = Button(frame, text='4', bg=numcolor, activebackground=clickcolor, command=write_num('4'))
button10 = Button(frame, text='5', bg=numcolor, activebackground=clickcolor, command=write_num('5'))
button11 = Button(frame, text='6', bg=numcolor, activebackground=clickcolor, command=write_num('6'))
button12 = Button(frame, text='*', bg=othercolor, activebackground=clickcolor, command=write_op('*'))
button13 = Button(frame, text='1/x', bg=othercolor, activebackground=clickcolor)
button14 = Button(frame, text='7', bg=numcolor, activebackground=clickcolor, command=write_num('7'))
button15 = Button(frame, text='8', bg=numcolor, activebackground=clickcolor, command=write_num('8'))
button16 = Button(frame, text='9', bg=numcolor, activebackground=clickcolor, command=write_num('9'))
button17 = Button(frame, text='/', bg=othercolor, activebackground=clickcolor, command=write_op('/'))
button18 = Button(frame, text='%', bg=othercolor, activebackground=clickcolor)
button19 = Button(frame, text=chr(27), bg=othercolor, activebackground=clickcolor)
button20 = Button(frame, text='clear', bg=othercolor, activebackground=clickcolor)
button21 = Button(frame, text='+-', bg=othercolor, activebackground=clickcolor)
button22 = Button(frame, text='sqrt', bg=othercolor, activebackground=clickcolor)

# place widgets
label.place(relwidth=0.9, relheight=0.9, anchor='n')
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

# below code and stick settings above required to make buttons sized relative to frame
for i in range(1,21):
    exec(frame.grid_columnconfigure(i,weight=1))
    

# frame.grid_columnconfigure(1,weight=1)
# frame.grid_columnconfigure(2,weight=1)
# frame.grid_columnconfigure(3,weight=1)
# frame.grid_columnconfigure(4,weight=1)
# frame.grid_columnconfigure(5,weight=1)
# frame.grid_columnconfigure(6,weight=1)
# frame.grid_columnconfigure(7,weight=1)
# frame.grid_columnconfigure(8,weight=1)
# frame.grid_columnconfigure(9,weight=1)
# frame.grid_columnconfigure(10,weight=1)
# frame.grid_columnconfigure(11,weight=1)
# frame.grid_columnconfigure(12,weight=1)
# frame.grid_columnconfigure(13,weight=1)
# frame.grid_columnconfigure(14,weight=1)
# frame.grid_columnconfigure(15,weight=1)
# frame.grid_columnconfigure(16,weight=1)
# frame.grid_columnconfigure(17,weight=1)
# frame.grid_columnconfigure(18,weight=1)
# frame.grid_columnconfigure(19,weight=1)
# frame.grid_columnconfigure(20,weight=1)
# frame.grid_columnconfigure(21,weight=1)



root.mainloop()

