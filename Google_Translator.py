from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import messagebox
master= tk.Tk()
master.title("Universal Translator")


def translate():
    language_1=t1.get("1.0","end-1c")
    cl=choose_language.get()

    if language_1=='':
        messagebox.showerror('Language Translator','Please fill the box')
    else:
        t2.delete(1.0,'end')
        translator=Translator()
        output = translator.translate(language_1,dest=cl)
        t2.insert('end',output.text)


def clear():
    t1.delete(1.0,'end')
    t2.delete(1.0,'end')

master.geometry('530x330')
master.maxsize(530,330)
master.minsize(530,330)
img= ImageTk.PhotoImage(Image.open('img1.png'))
label = Label(image=img)
label.place(x=230,y=3)
label1=Label(master,text="Software Designed By Suneet Verma",font=("roboto",8,"italic"))
label1.place(x=170,y=310)
a= tk.StringVar()
auto_detect = ttk.Combobox(master,width=20,textvariable=a,state='readonly',font=('verdana',10,'bold'))
auto_detect['values']=('Auto Detect','English','Hindi','English','Hindi','Bengali','Afrikaans','Irish','Albanian','Italian','Arabic','Japanese','Azerbaijani','Kannada','Basque','Korean','Bengali','Latin','Belarusian','Latvian','Bulgarian','Lithuanian','Catalan','Macedonian','Chinese','Simplified','Malay','Chinese','Traditional','Maltese','Croatian','Norwegian','Czech','Persian','Danish','Polish','Dutch','Portuguese','Romanian','Esperanto','Russian','Estonian','Serbian','Filipino','Slovak','Finnish','Slovenian','French','Spanish','Galician','Swahili','Georgian','Swedish','German','Tamil','Greek','Telugu','Gujarati','Thai','Haitian','Turkish','Hebrew','Ukrainian','Urdu','Hungarian','Vietnamese','Icelandic','Welsh','Indonesian','Yiddish')
auto_detect.place(x=30,y=70)
auto_detect.current(0)
l=tk.StringVar()
choose_language= ttk.Combobox(master,width=20,textvariable=l,state='readonly',font=('verdana',10,'bold'))
choose_language['values']=('English','Hindi','Bengali','Afrikaans','Irish','Albanian','Italian','Arabic','Japanese','Azerbaijani','Kannada','Basque','Korean','Bengali','Latin','Belarusian','Latvian','Bulgarian','Lithuanian','Catalan','Macedonian','Chinese','Simplified','Malay','Chinese','Traditional','Maltese','Croatian','Norwegian','Czech','Persian','Danish','Polish','Dutch','Portuguese','Romanian','Esperanto','Russian','Estonian','Serbian','Filipino','Slovak','Finnish','Slovenian','French','Spanish','Galician','Swahili','Georgian','Swedish','German','Tamil','Greek','Telugu','Gujarati','Thai','Haitian','Turkish','Hebrew','Ukrainian','Urdu','Hungarian','Vietnamese','Icelandic','Welsh','Indonesian','Yiddish')
choose_language.place(x=290,y=70)
choose_language.current(0)
t1 = Text(master,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)
t2 = Text(master,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)
button = Button(master,text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=translate)
button.place(x=150,y=280)
button = Button(master,text="Clear",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=clear)
button.place(x=280,y=280)
master.mainloop()