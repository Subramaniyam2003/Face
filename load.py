#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
from playsound import playsound
w=Tk()

#Using piece of code from old splash screen
width_of_window = 530
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    import home




Frame(w, width=530, height=250, bg='black').place(x=0,y=0)
label1=Label(w, text='FACE IDENTIFICATION', fg='red', bg='black') #decorate it 
label1.configure(font=( "Helvetica",24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='red', bg='black') #decorate it 
label2.configure(font=("Helvetica", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))




for i in range(1): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    w.update_idletasks()
    time.sleep(0.1)
    playsound('2.wav')

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    w.update_idletasks()
    time.sleep(0.3)
    playsound('2.wav')

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=260, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=280, y=145)
    w.update_idletasks()
    time.sleep(0.3)
    playsound('2.wav')

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=260, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=280, y=145)
    w.update_idletasks()
    time.sleep(0.3)
    playsound('2.wav')


w.destroy()
new_win()
w.mainloop()




















