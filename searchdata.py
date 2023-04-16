import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import face_recognition

root=Tk()
root.geometry("1600x556")
root.title("SEARCH DATA")
root.config(bg='black')
sh=tk.Label(root,bg='black')
def selectpic():
    global img
    global filename
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("png images","*.png"),("jpg images","*.jpg")))
    print(filename)
    img = Image.open(filename)
    img = img.resize((300,450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    sh['image'] = img

def clear():
    
    a1.destroy()
    b1.destroy()
    c1.destroy()
    d1.destroy()
    e1.destroy()
    
def searchpic():
    global a1,b1,c1,d1,e1
    df=pd.read_csv(r"C:\Users\OM MURUGA\Desktop\python\records.csv")
    df1=pd.DataFrame(df)
    un1=df1['Image_Location']
    un2=df1['Name']
    un3=df1['Gender']
    un4=df1['DOB']
    un5=df1['Phone_No']
    un6=df1['Address']

    original=face_recognition.load_image_file(filename)
    originalen=face_recognition.face_encodings(original)[0]
    for i in range(0,len(un1),1):
        unknown=face_recognition.load_image_file(un1[i])
        unknownen=face_recognition.face_encodings(unknown)[0]
        result=face_recognition.compare_faces([originalen],unknownen)
        print(result)
        if result[0] == True:
            a1=Label(root,text=un2[i],fg='red',bg='black')
            a1.configure(font=('Helvetica',14,'bold'))
            a1.place(x=655,y=170)
            b1=Label(root,text=un3[i],fg='red',bg='black')
            b1.configure(font=('Helvetica',14,'bold'))
            b1.place(x=655,y=190)
            c1=Label(root,text=un4[i],fg='red',bg='black')
            c1.configure(font=('Helvetica',14,'bold'))
            c1.place(x=655,y=210)
            d1=Label(root,text=un5[i],fg='red',bg='black')
            d1.configure(font=('Helvetica',14,'bold'))
            d1.place(x=655,y=230)
            e1=Label(root,text=un6[i],fg='red',bg='black')
            e1.configure(font=('Helvetica',14,'bold'))
            e1.place(x=655,y=250)
            b3=Button(root,text="CLEAR RESULT",fg='red',bg='black',activebackground='red',activeforeground='black',pady=5,command=clear)
            b3.place(x=700,y=400)
            b3.configure(font=( "Helvetica",14, "bold"))

            break

b1=Button(root,text="SELECT IMAGE",fg='red',bg='black',activebackground='red',activeforeground='black',pady=5,command=selectpic)
b1.place(x=120,y=60)
b1.configure(font=( "Helvetica",14, "bold"))
b2=Button(root,text="SEARCH",fg='red',bg='black',activebackground='red',activeforeground='black',pady=5,command=searchpic)
b2.place(x=640,y=60)
b2.configure(font=( "Helvetica",14, "bold"))
a=Label(root,text="SELECTED IMAGE :",fg='red',bg='black')
a.configure(font=( "Helvetica",14, "bold"))
a.place(x=115,y=130)
b=Label(root,text="RESULTS :",fg='red',bg='black')
b.configure(font=('Helvetica',14,'bold'))
b.place(x=645,y=130)
sh.place(x=75,y=200)
root.mainloop()
