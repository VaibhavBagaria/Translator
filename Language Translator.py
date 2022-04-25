from tkinter import*
from tkinter import ttk
from googletrans import Translator
from googletrans import LANGUAGES

root=Tk()
root.geometry('1100x500')
root.title('LANGUAGE TRANSLATOR')
root.configure(bg="lightcoral")

languages=list(LANGUAGES.values())

title=Label(root,text="Language Translator",bg="lightcoral", font=("Comic Sans MS boldface",20))
title.place(relx=0.5,rely=0.1,anchor=CENTER)

#Left area
l1=Label(root,text="Enter Text",bg="lightcoral", font=("Courier italic",20))
l1.place(relx=0.08,rely=0.3,anchor=CENTER)

textarea=Text(root,bg="whitesmoke",wrap=WORD,width=41,height=11,bd=0,padx=5,pady=5,font=("Roboto italic",12))
textarea.place(relx=0.18,rely=0.6,anchor=CENTER)

dropdown=ttk.Combobox(root,state="readonly",values=languages,width=20)
dropdown.place(relx=0.23,rely=0.3,anchor=CENTER)
dropdown.set("English")

#Right Area
l2=Label(root,text="Output",bg="lightcoral", font=("Courier italic",20))
l2.place(relx=0.7,rely=0.3,anchor=CENTER)

textarea2=Text(root,bg="whitesmoke",wrap=WORD,width=41,height=11,bd=0,padx=5,pady=5,font=("Roboto italic",12))
textarea2.place(relx=0.8,rely=0.6,anchor=CENTER)

dropdown2=ttk.Combobox(root,state="readonly",values=languages,width=20)
dropdown2.place(relx=0.85,rely=0.3,anchor=CENTER)
dropdown2.set("Portuguese")

def Translation():
    userlanguage=dropdown.get()
    convertedlanguage=dropdown2.get()
    textbox=textarea.get(1.0,END)
    obj_trans=Translator()
    try:
        translated=obj_trans.translate(text=textbox,dest=convertedlanguage,src=userlanguage)
        textarea2.delete(1.0,END)
        textarea2.insert(END,translated.text)
    
    except(TypeError):
        print("Try Again")
        
btn=Button(root,text="Translate",bg="blue",command=Translation)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()