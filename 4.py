from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('600x600+700+100')


def input(symbol):
    entry.insert(END,symbol )


def clear():
    entry.delete(0,END)    

def result():
    text = entry.get()
    result=0
    if '+' in text:
        split_text = text.split('+')
        first = float(split_text[0])
        second  = float(split_text[1])
        result = first +second
    if '-' in text:
        split_text = text.split('+')
        first = float(split_text[0])
        second  = float(split_text[1])
        result = first -second

    if '*' in text:
        split_text = text.split('+')
        first = float(split_text[0])
        second  = float(split_text[1])
        result = first *second

    if '/' in text:
        split_text = text.split('+')
        first = float(split_text[0])
        second  = float(split_text[1])
        result = first/second

    clear()
    entry.insert(0, result)    
    




entry = Entry(window,width =15,font =('',20))
entry.place(x =100,y=50)

button1 = Button(window, bg='black', fg = 'white',text = '1', command=lambda:input('1'))
button1.place(x = 100,y=100, width=50,height=50)


button2 = Button(window, bg='black', fg = 'white',text = '2',command=lambda:input('2'))
button2.place(x = 150,y=100, width=50,height=50)

button3 = Button(window, bg='black', fg = 'white',text = '3',command=lambda:input('3'))
button3.place(x = 200,y=100, width=50,height=50)

button4 = Button(window, bg='black', fg = 'white',text = '4',command=lambda:input('4'))
button4.place(x = 100,y=150, width=50,height=50)

button5= Button(window, bg='black', fg = 'white',text = '5',command=lambda:input('5'))
button5.place(x = 150,y=150, width=50,height=50)

button6 = Button(window, bg='black', fg = 'white',text = '6',command=lambda:input('6'))
button6.place(x = 200,y=150, width=50,height=50)

button7 = Button(window, bg='black', fg = 'white',text = '7',command=lambda:input('7'))
button7.place(x = 100,y=200, width=50,height=50)

button8 = Button(window, bg='black', fg = 'white',text = '8',command=lambda:input('8'))
button8.place(x = 150,y=200, width=50,height=50)

button9 = Button(window, bg='black', fg = 'white',text = '9', command=lambda:input('9'))
button9.place(x = 200,y=200, width=50,height=50)

buttonPlus = Button(window,bg = 'black',fg='white',text='+' ,command=lambda:input('+'))
buttonPlus.place(x=250,y=100,width=50,height=50)

buttonMIn = Button(window,bg = 'black',fg='white',text='-',command=lambda:input('-'))
buttonMIn.place(x=250,y=150,width=50,height=50)

buttonDil = Button(window,bg = 'black',fg='white',text='/',command=lambda:input('/'))
buttonDil.place(x=250,y=200,width=50,height=50)

buttonMn = Button(window,bg = 'black',fg='white',text='*',command=lambda:input('*'))
buttonMn.place(x=250,y=250,width=50,height=50)

buttonR = Button(window,bg = 'black',fg='white',text='=',command=result)
buttonR.place(x=200,y=250,width=50,height=50)

buttonClear = Button(window,bg = 'black',fg='white',text='CE',command=clear)
buttonClear.place(x=150,y=250,width=50,height=50)

buttonK= Button(window,bg = 'black',fg='white',text='.',command=lambda:input('.'))
buttonK.place(x=100,y=250,width=50,height=50)


window.mainloop()