from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry('500x354')
window.title('Calculator')
window.resizable(False, False)


def click(item):
    global expression
    expression += item
    input_text.set(expression)


def clear():
    global expression
    expression = ""
    input_text.set("")


def egalitate():
    try:
        global expression
        rezultat = str(eval(expression))
        input_text.set(rezultat)
        expression = ""
    except Exception:
        expression = ""
        input_text.set("Error! Please click C button")


expression = ''
input_text = StringVar()

input_frame = Frame(window, width=312, height=50, bd=0, highlightcolor='black', bg='#233')
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, background='#eee', bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

frame_button = Frame(window, width=500, height=300, bg='grey')
frame_button.pack()

button_clear = Button(frame_button, text='C', fg='black', width=55, height=3, bd=1, bg='#eee', cursor='hand2',
                      command=lambda: clear())

button_clear.grid(row=0, column=0, columnspan=3)
impartit = Button(frame_button, text='/', fg='black', width=15, height=3, bd=1, bg='#7fffd4', cursor='hand2',
                  command=lambda: click('/'))
impartit.grid(row=0, column=3)

sapte = Button(frame_button, text='7', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
               command=lambda: click('7'))
sapte.grid(row=1, column=0)
opt = Button(frame_button, text='8', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
             command=lambda: click('8'))
opt.grid(row=1, column=1)
noua = Button(frame_button, text='8', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
              command=lambda: click('9'))
noua.grid(row=1, column=2)
inmultire = Button(frame_button, text='*', fg='black', width=15, height=3, bd=1, bg='#7fffd4', cursor='hand2',
                   command=lambda: click('*'))
inmultire.grid(row=1, column=3)

patru = Button(frame_button, text='4', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
               command=lambda: click('4'))
patru.grid(row=2, column=0)
cinci = Button(frame_button, text='5', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
               command=lambda: click('5'))
cinci.grid(row=2, column=1)
sase = Button(frame_button, text='6', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
              command=lambda: click('6'))
sase.grid(row=2, column=2)
minus = Button(frame_button, text='-', fg='black', width=15, height=3, bd=1, bg='#7fffd4', cursor='hand2',
               command=lambda: click('-'))
minus.grid(row=2, column=3)

unu = Button(frame_button, text='1', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
             command=lambda: click('1'))
unu.grid(row=3, column=0)
doi = Button(frame_button, text='2', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
             command=lambda: click('2'))
doi.grid(row=3, column=1)
trei = Button(frame_button, text='3', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
              command=lambda: click('3'))
trei.grid(row=3, column=2)
plus = Button(frame_button, text='+', fg='black', width=15, height=3, bd=1, bg='#7fffd4', cursor='hand2',
              command=lambda: click('+'))
plus.grid(row=3, column=3)

zero = Button(frame_button, text='0', fg='black', width=36, height=3, bd=1, bg='#eee', cursor='hand2',
              command=lambda: click('0'))
zero.grid(row=4, column=0, columnspan=2)
virgula = Button(frame_button, text=',', fg='black', width=17, height=3, bd=1, bg='#eee', cursor='hand2',
                 command=lambda: click(','))
virgula.grid(row=4, column=2)
egal = Button(frame_button, text='=', fg='black', width=15, height=3, bd=1, bg='#7fffd4', cursor='hand2',
              command=lambda: egalitate())
egal.grid(row=4, column=3)
window.mainloop()
