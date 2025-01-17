from tkinter import *
import shutil
import time
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2
from subprocess import call
def callTrainer():
    call(["python", "trainer.py"])

if __name__ == "__main__":
    root = Tk()
    root.geometry('1350x720')
    root.minsize(1350, 720)
    root.state("zoomed")
    root.title("Advanced Criminal Identification System")

    # Adding a custom icon to the window
    root.iconbitmap(r"C:\Users\askar\Documents\Advanced Criminal Detection\icon.ico")

    Fullname = StringVar()
    Fathername = StringVar()
    Mothername = StringVar()
    Bodymark = StringVar()
    dob = StringVar()
    Nationality = StringVar()
    Crime = StringVar()
    gen = IntVar()
    rel = StringVar()
    blood = StringVar()
    file1 = ""

    # Updated background color
    root.configure(bg="#f0f0f0")

    image = Image.open("images.jpg")
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(image=photo, width=500, height=500, bg="#f0f0f0")
    photo_label.place(x=740, y=140)

    def ask():
        value = tmsg.askquestion("ACIS WARNING !", "Select all (*) mandatory fields.\n(name,gender,religion,crime,pic)\n\n If done already, then proceed. \n\n Will you like to proceed ?")
        if value == "yes":
            x = databaseEnter()
            if x == 1:
                tmsg.showinfo("Success", "New Face Recorded Successfully")
                root.destroy()
            else:
                tmsg.showinfo("Warning", "Please enter all (*) marked details")

    def getid():
        conn = sqlite3.connect('criminal.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute('select max(ID) from People')
        conn.commit()
        for row in cursor:
            for elem in row:
                x = elem
        return x

    def databaseEnter():
        name = Fullname.get()
        father = Fathername.get()
        mother = Mothername.get()
        bl = blood.get()
        if bl == "Select Blood Group":
            bl = None
        body = Bodymark.get()
        nat = Nationality.get()
        crime = Crime.get()
        Dob = dob.get()
        gen1 = ""
        gender = gen.get()
        if gender == 1:
            gen1 = 'Male'
        if gender == 2:
            gen1 = 'Female'
        religion = rel.get()
        if religion == "Select Religion":
            religion = None

        if name != "" and crime != "" and gen1 != "":
            conn = sqlite3.connect('criminal.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute('INSERT INTO People (Name,Gender,Father,Mother,Religion,Blood,Bodymark,Nationality,Crime) VALUES(?,?,?,?,?,?,?,?,?)',
                           (name, gen1, father, mother, religion, bl, body, nat, crime))
            conn.commit()
            x = getid()
            file = "images/user." + str(x) + ".png"
            newPath = shutil.copy('temp/1.png', file)
        else:
            return 0
        return 1

    def mfileopen():
        global file1
        file1 = filedialog.askopenfilename()
        print(file1)
        newPath = shutil.copy(file1, 'temp/1.png')
        image = Image.open('temp/1.png')
        image = image.resize((500, 500), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        photo_label.configure(image=photo)
        photo_label.image = photo
        label_ = Label(root, text=file1, width=70, font=("Arial", 8), bg="#f0f0f0")
        label_.place(x=260, y=630)

    label_10 = Label(root, text="Advanced Criminal Identification System", width=85, font=("bold", 20), anchor=CENTER, bg="blue", fg="white")
    label_10.place(x=0, y=0)

    label_0 = Label(root, text="Registration Form", width=95, font=("bold", 16), bg="#333", fg='white')
    label_0.place(x=70, y=42)

    label_1 = Label(root, text="Name    *", width=20, font=("bold", 12), bg="#f0f0f0")
    label_1.place(x=70, y=130)

    entry_1 = Entry(root, width=50, textvar=Fullname, font=("Arial", 12))
    entry_1.place(x=260, y=130)

    label_2 = Label(root, text="Father Name", width=20, font=("bold", 12), bg="#f0f0f0")
    label_2.place(x=70, y=180)

    entry_2 = Entry(root, width=50, textvar=Fathername, font=("Arial", 12))
    entry_2.place(x=260, y=180)

    label_3 = Label(root, text="Gender      *", width=20, font=("bold", 12), bg="#f0f0f0")
    label_3.place(x=70, y=280)

    Radiobutton(root, text="Male", padx=5, variable=gen, value=1, font=("Arial", 12), bg="#f0f0f0").place(x=260, y=280)
    Radiobutton(root, text="Female", padx=20, variable=gen, value=2, font=("Arial", 12), bg="#f0f0f0").place(x=315, y=280)

    label_4 = Label(root, text="Mother Name", width=20, font=("bold", 12), bg="#f0f0f0")
    label_4.place(x=70, y=230)
    entry_5 = Entry(root, width=50, textvar=Mothername, font=("Arial", 12))
    entry_5.place(x=260, y=230)

    label_4 = Label(root, text="Religion    *", width=20, font=("bold", 12), bg="#f0f0f0")
    label_4.place(x=70, y=330)
    list1 = ['Hindu', 'Muslim', 'Buddhist', 'Christian', 'Sikh', 'Jain', 'Others']
    droplist = OptionMenu(root, rel, *list1)
    droplist.config(width=30)
    rel.set('Select Religion')
    droplist.place(x=260, y=325)

    label_5 = Label(root, text="Blood Group", width=20, font=("bold", 12), bg="#f0f0f0")
    label_5.place(x=70, y=380)

    list2 = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'Not known']
    droplist = OptionMenu(root, blood, *list2)
    droplist.config(width=30)
    blood.set('Select Blood Group')
    droplist.place(x=260, y=380)

    label_6 = Label(root, text="Body Mark", width=20, font=("bold", 12), bg="#f0f0f0")
    label_6.place(x=70, y=430)

    entry_6 = Entry(root, width=50, textvar=Bodymark, font=("Arial", 12))
    entry_6.place(x=260, y=430)

    label_7 = Label(root, text="Nationality", width=20, font=("bold", 12), bg="#f0f0f0")
    label_7.place(x=70, y=480)

    entry_7 = Entry(root, width=50, textvar=Nationality, font=("Arial", 12))
    entry_7.place(x=260, y=480)

    label_8 = Label(root, text="Crime convicted        *", width=20, font=("bold", 12), bg="#f0f0f0")
    label_8.place(x=70, y=530)

    entry_8 = Entry(root, width=50, textvar=Crime, font=("Arial", 12))
    entry_8.place(x=260, y=530)

    label_9 = Label(root, text="Face Image    *", width=20, font=("bold", 12), bg="#f0f0f0")
    label_9.place(x=70, y=590)

    btn = Button(text="Select", width=20, command=mfileopen, font=("Arial", 10, "bold"), bg='#4CAF50', fg='white')
    btn.place(x=260, y=590)

    Button(root, text='Register', width=15, font=("Arial", 10, "bold"), bg='#FF5722', height=2, fg='white', command=ask).place(x=250, y=650)

    root.mainloop()
