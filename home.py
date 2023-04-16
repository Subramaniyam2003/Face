from tkinter import *
from tkinter import font
def new_win():
    q=Tk()
    q.configure(bg='black')
    q.title('FACE IDENTIFICATION')
    q.geometry(("600x350"))
    def adddatapage():
        q.destroy()
        import adddata
    def searchdatapage():
        q.destroy()
        import searchdata
    def addandsearch():
        b1= Button(q,text='ADD DATA',fg='red',bg='black',activebackground='red',activeforeground='black',pady=10,command=adddatapage)
        b1.configure(font=( "Helvetica",16, "bold"))
        b1.place(x=210,y=100)
        b2= Button(q,text='SEARCH DATA',fg='red',bg='black',activebackground='red',activeforeground='black',pady=10,command=searchdatapage)
        b2.configure(font=( "Helvetica",16, "bold"))
        b2.place(x=190,y=180)
        
    addandsearch()
    

    q.mainloop()
new_win()
