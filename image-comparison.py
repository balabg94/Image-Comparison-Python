#Startup-Box Task 1. Image Comparison

from Tkinter import *
import tkMessageBox
import Tkinter
from itertools import izip
from PIL import Image,ImageTk
import urllib, cStringIO
import win32console
import win32gui

win=win32console.GetConsoleWindow()       # For closing command window 
win32gui.ShowWindow(win,0)


def entrybox1(event):                     # Pasting url from clipboard to the first entry box
    clipboard = root.clipboard_get()
    if clipboard.startswith('http'):
        ent1.delete(0, 'end')
        ent1.insert(0,clipboard)

def entrybox2(event):                     # Pasting url from clipboard to the second entry box
    clipboard = root.clipboard_get()
    if clipboard.startswith('http'):
        ent2.delete(0, 'end')
        ent2.insert(0,clipboard)

def compare():                          #comparing two images   
    feedback.set("Loading. Please wait untill images are being fetched and compared.")        # printing loading message
    label3.update_idletasks()
    try:
        comment = StringVar()
        img1 = image1.get()
        img2 = image2.get()
        
        file1 = cStringIO.StringIO(urllib.urlopen(img1).read())                         # fetching images from url
        file2 = cStringIO.StringIO(urllib.urlopen(img2).read())
        
        i1 = Image.open(file1)
        i2 = Image.open(file2)
        i1 = i1.resize((250, 250), Image.ANTIALIAS)
        i2 = i2.resize((250, 250), Image.ANTIALIAS) 
        
        window = Toplevel(root)                                                         # creating new window for printing result
        window.geometry('600x350+305+220')
        window.wm_title("Result")
        
        printimage1 = i1.resize((200, 200), Image.ANTIALIAS)                            # printing image1 on new window
        imga = ImageTk.PhotoImage(printimage1)
        panel = Label(window, image = imga)
        panel.pack()

        comnt = Label(window,text="",textvariable = comment,font=("Helvetica", 12))
        comnt.pack()

        printimage2 = i2.resize((200, 200), Image.ANTIALIAS)                            # printing image2 on new window
        imgb = ImageTk.PhotoImage(printimage2)
        panel1 = Label(window, image = imgb)
        panel1.pack()
        
        pairs = izip(i1.getdata(), i2.getdata())                                        # Calculating simillarity
        if len(i1.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
            
        ncomponents = i1.size[0] * i1.size[1] * 3
        percent =  int(100 - ((dif / 255.0 * 100) / ncomponents))
        value = "Simillarity rank (/100) : " + str(percent)
        
        label4 = Label(window,text=value,font=("Helvetica", 16))                        # Printing similarity rank
        label4.pack()

        label5 = Label(window,text="VS",font=("Helvetica", 14))                        # Printing similarity rank
        label5.pack()

        if percent >= 85 and percent <= 95:
            comment.set("Almost simillar")
        elif percent > 95:
            comment.set("Simillar")
        elif percent <= 5:
            comment.set("Disimillar")
        elif percent >= 50 and percent <= 85:
            comment.set("Partially simillar")
        elif percent >5 and percent < 50:
            comment.set("Not so simillar")
        feedback.set("")                                                                # deleting loading message
        label3.update_idletasks()
        
        quitButton = Button(window, text = "Quit",font=(12), command = window.destroy)
        quitButton.pack()
        
        panel.place(x=60,y=10)                                                          # placing widgets in new window
        panel1.place(x=350,y=10)
        label4.place(x=200,y=230)
        label5.place(x=290,y=105)
        comnt.place(x=255,y=270)
        quitButton.place(x=300,y=300)
        window.mainloop()
    except:
        tkMessageBox.showerror( "Error ", "There is some error. Please try again. ")    #printing error ,essage
        feedback.set("")
        label3.update_idletasks()
      

                 #the UI box configurations
    
        
root = Tk()                            
root.wm_title("Compare Images")
root.geometry('600x200+220+180')
image1 = StringVar()
image2 = StringVar()
feedback = StringVar() 

label1=Label(text = "Image 1 Url : ")
label1.pack()

ent1 = Entry(bd=5,textvariable = image1, width=70)      #entry box 1
ent1.pack()
ent1.bind('<Button-1>', entrybox1)                      #when clicked on this entry, entrybox1() is executed

label2=Label(text = "Image 2 Url : ")
label2.pack()

ent2 = Entry(bd=5,textvariable = image2, width=70)      #entry box 2
ent2.pack()
ent2.bind('<Button-1>', entrybox2)                      #when clicked on this entry, entrybox2() is executed

b1 = Button(text = "Compare",command = compare)
b1.pack()
quitButn = Button(root, text = "Quit", command = root.destroy)
quitButn.pack()

           
label3 = Label(text="",textvariable=feedback)
label3.pack()


b1.place(x = 250,y=100)             #placing widgets in positions
quitButn.place(x=330,y=100)
label1.place(x = 50,y=10)
label2.place(x = 50,y=50)
ent1.place(x=150,y=10)
ent2.place(x=150,y=50)
label3.place(x=150,y=150)
root.mainloop()                     #looping
