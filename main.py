from tkinter import *
from tkinter import filedialog, messagebox, StringVar
from PIL import Image,ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry('700x480')
win.config(bg='red')
#Button Function
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG file','*.png'),('JPG file','*.jpg'),
                                                      ('All file','*.txt')))
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image=img
def hide():
    global hide_msg
    password = code.get()
    if password == '1416':

       msg = text1.get(1.0,END)
       hide_msg = lsb.hide(str(open_file),msg)
       messagebox.showinfo('Success','Message is Successfully Hidden in the image,Please save your Image')
    elif password == '':
        (messagebox.showerror('Error','Please enter Secret Key'))
    else:
        messagebox.showerror('Error','Wrong Secret Key')
        code.set('')
def save_img():
    hide_msg.save('Secret file.png')
    messagebox.showinfo('Saved','Image has been successfully saved')
def show():
    password = code.get()
    if password == '1416':
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0,END)
        text1.insert(END,show_msg)

    elif password == '':
       messagebox.showerror('Error', 'Please enter Secret Key')
    else:
       messagebox.showerror('Error', 'Wrong Secret Key')
       code.set('')

#Logo
logo = PhotoImage(file='logo.png')
Label(win,image=logo,bd=0).place(x=30,y=0)
#Heading
Label(win,text='Steganography Tool',font='impack 34 bold',bg='red',fg='black').place(x=250,y=50)
#Frame 1
f1 = Frame(win,width=220,height=50,bd=5,bg='black')
f1.place(x=100,y=220)
lf1 = Label(f1,bg='black')
lf1.place(x=0,y=0)
#Frame 2
f2 = Frame(win,width=280,height=90,bd=5,bg='white')
f2.place(x=350,y=200)
text1 = Text(f2,font='ariel 15 bold',wrap=WORD)
text1.place(x=0,width=280,height=90)

# Label for Secret Key
Label (win,text='Enter Secret Key',font='10',bg='white',fg='black').place(x=245,y=330)

#Entry Widget for secret key
code=StringVar()
e = Entry(win,textvariable=code,bd=2,font='impact 10 bold ',show='*')
e.place(x=245,y=370)

#Buttons
open_button = Button(win,text='Open Image',bg='blue',fg='black',font='ariel 12 bold ',cursor='hand2',command=open_img)
open_button.place(x=60,y=417)

save_button = Button(win,text='Save Image',bg='green',fg='black',font='ariel 12 bold ',cursor='hand2',command=save_img)
save_button.place(x=190,y=417)

hide_button = Button(win,text='Hide Data',bg='yellow',fg='black',font='ariel 12 bold ',cursor='hand2',command=hide)
hide_button.place(x=380,y=417)

show_button = Button(win,text='Show Data',bg='orange',fg='black',font='ariel 12 bold ',cursor='hand2',command=show)
show_button.place(x=510,y=417)




mainloop()