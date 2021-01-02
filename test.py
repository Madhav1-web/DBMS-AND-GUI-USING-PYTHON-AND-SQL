from tkinter import ttk

import tkinter as tk

import mysql.connector  
from tkinter import * 
import tkinter as tk 
from tkinter import ttk
import mysql.connector  
from tkinter import * 
from tkcalendar import *
import datetime
import threading
from datetime import date
from datetime import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="buyerday",
    database = "project1",
    buffered = True,
    )

Username=None
passw=None
addrss=None
emil=None
lblfrstrow=None
lblsecrow=None
lblrdrow=None
lblfrtrow=None
lblfifrow=None
lblsixrow=None
ag=None
imagecalen=None
okbtn=None
submitbtn=None
title=None
label_1=None
f_dob=None
tree=None
button1=None
filterbtn=None


def View():


    

    my_cursor.execute("SELECT * FROM madhav")

    rows = my_cursor.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    mydb.close()


my_cursor = mydb.cursor()

root = tk.Tk() 
root.geometry("300x300") 
root.title("MENU")
menubar = Menu(root)
root.config(menu=menubar) 
   
C = Canvas(root, bg ="blue", height = 250, width = 300) 

cal=Calendar(root, selectmode="day", year=2020, month= 12, day =21)
def image():
    
    cal.pack(pady=20)
    

def rom():
    global DOB, temp
    dob_date=cal.get_date()
    DOB = tk.Entry(root, width = 35) 
    DOB.insert(END, "{}".format(dob_date))
    DOB.place(x = 150, y = 90, width = 100) 
    temp=datetime.strptime(dob_date, "%d/%m/%Y")
    global age
    today = date.today()
    age = today.year - temp.year - ((today.month, today.day) < (temp.month, temp.day))
    ag.insert(END,"{}".format(age))
    cal.pack_forget()
    
'''
def calen():
    my_label.config(text=cal.get_date())

'''

#submit function
def submit():
    
    my_cursor = mydb.cursor()

    #INSERT INTO TABLE
    a=Username.get()
    b=passw.get()
    c=addrss.get()
    '''
    d=DOB.get()
    '''
    e=emil.get()
    '''
    f=ag.get()
    '''
    g=cal.get_date()
    

    #password validations
    special_characters = "!@#$%^&*()-+?_=,<>/"

    contains_digit = any(map(str.isdigit, b))
    contains_aplhabet = any(map(str.isalpha,b))
    contains_special = any(characters in special_characters for characters in b)

    #email validations
    at_dot="@."
    check_for_at = any(characters in at_dot for characters in e)
    
    

    if a == '' :
        statement = tk.Label(root, text ="Username is null                        -", ) 
        statement.place(x = 150, y = 280)
        #Clear the text boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        DOB.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END)
    
    elif len(b) < 8:
        statement = tk.Label(root, text ="password shld have a minimum of 8 letters                                -", ) 
        statement.place(x = 150, y = 280)
        #Clear the text boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        DOB.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END)    

    elif contains_digit == False :
        statement = tk.Label(root, text ="Minimum requirement of 1 digit in the password is not fullfilled                       -", ) 
        statement.place(x = 150, y = 280)
        #Clear the text boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        DOB.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END) 

    elif contains_aplhabet == False :
        statement = tk.Label(root, text ="Minimum requirement of 1 letter in the password is not fullfilled                       -", ) 
        statement.place(x = 150, y = 280)
        #Clear the text boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        DOB.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END)

    elif contains_special == False :
        statement = tk.Label(root, text ="Minimum requirement of 1 special character in the password is not fullfilled                       -", ) 
        statement.place(x = 150, y = 280)
        #Clear the text boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        DOB.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END)         

    elif check_for_at == False:  
        statement = tk.Label(root, text ="Minimum requirement of 1 @ or 1 . in the email is not fullfilled                       -", ) 
        statement.place(x = 150, y = 280)
        #Clear the text boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        DOB.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END) 

    else:
        my_cursor.execute("INSERT INTO madhav (name, password, address, DT, email, age)  VALUES (%(Username)s, %(passw)s, %(addrss)s, %(DOB)s, %(emil)s, %(ag)s)",
            {
                'Username': Username.get(),
                'passw'   : passw.get(),
                'addrss'  : addrss.get(),
                'DOB'     : datetime.strptime(g, "%d/%m/%Y").strftime("%Y-%m-%d"),
                'emil'    : emil.get(),
                'ag'      : age
            })


        mydb.commit()
        my_cursor.close()

        # Clear The Text Boxes
        Username.delete(0,END)
        passw.delete(0,END)
        addrss.delete(0,END)
        emil.delete(0,END)
        ag.delete(0,END)
        DOB.delete(0,END)

        statement = tk.Label(root, text ="Record has been submitted                                                                     -", ) 
        statement.place(x = 150, y = 280)




def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()




def widget():
    global Username,passw,addrss,emil,lblfrstrow,lblsecrow,lblrdrow,lblfrtrow,lblfifrow,lblsixrow,ag,imagecalen,okbtn,submitbtn
    if Username is not None: Username.destroy()
    if passw is not None: passw.destroy()
    if addrss is not None: addrss.destroy()
    if emil is not None: emil.destroy()
    if lblfrstrow is not None: lblfrstrow.destroy()
    if lblsecrow is not None: lblsecrow.destroy()
    if lblrdrow is not None: lblrdrow.destroy()
    if lblfrtrow is not None: lblfrtrow.destroy()
    if lblfifrow is not None: lblfifrow.destroy()
    if lblsixrow is not None: lblsixrow.destroy()
    if ag is not None: ag.destroy()
    if imagecalen is not None: imagecalen.destroy()
    if okbtn is not None: okbtn.destroy()
    if submitbtn is not None: submitbtn.destroy()

    title= Label(root, text = "FILTERING USING dob and address")
    title.place(x=150, y=10)

        
    label_1=Label(root, text ="filter :-")
    label_1.place(x = 0, y = 50)
        
    f_dob=tk.Entry(root, width = 35) 
    f_dob.place(x = 150, y = 50, width = 100)

    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="Username")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="Password")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="Address")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Date")

    tree.column("#5", anchor=tk.CENTER)

    tree.heading("#5", text="Email")

    tree.column("#6", anchor=tk.CENTER)

    tree.heading("#6", text="Age")

    tree.column("#7", anchor=tk.CENTER)

    tree.heading("#7", text="ID")

    tree.pack()

    tree.place(x=0, y= 100)

    filterbtn=tk.Button(text="Filter", command = donothing)
    filterbtn.place(x=250, y=50)

    button1 = tk.Button(text="Display data", command=donothing)

    button1.place(x=0, y=400)



def ADDING():  
    
    global Username,passw,addrss,emil,lblfrstrow,lblsecrow,lblrdrow,lblfrtrow,lblfifrow,lblsixrow,ag,imagecalen,okbtn,submitbtn

    if title is not None: title.destroy()
    if label_1 is not None: label_1.destroy()
    if f_dob is not None: f_dob.destroy()
    if tree is not None: tree.destroy()
    if filterbtn is not None: filterbtn.destroy()
    if button1 is not None: button1.destroy()
    if Username is not None: Username.destroy()
    if passw is not None: passw.destroy()
    if addrss is not None: addrss.destroy()
    if emil is not None: emil.destroy()
    if lblfrstrow is not None: lblfrstrow.destroy()
    if lblsecrow is not None: lblsecrow.destroy()
    if lblrdrow is not None: lblrdrow.destroy()
    if lblfrtrow is not None: lblfrtrow.destroy()
    if lblfifrow is not None: lblfifrow.destroy()
    if lblsixrow is not None: lblsixrow.destroy()
    if ag is not None: ag.destroy()
    if imagecalen is not None: imagecalen.destroy()
    if okbtn is not None: okbtn.destroy()
    if submitbtn is not None: submitbtn.destroy()


    
    # Definging the first row 
    lblfrstrow = tk.Label(root, text ="Username -", ) 
    lblfrstrow.place(x = 50, y = 20) 

    Username = tk.Entry(root, width = 35) 
    Username.place(x = 150, y = 20, width = 100) 
           
    lblsecrow = tk.Label(root, text ="Password -") 
    lblsecrow.place(x = 50, y = 50) 
          
    passw = tk.Entry(root, show="*", width = 35) 
    passw.place(x = 150, y = 50, width = 100) 
          
    lblrdrow = tk.Label(root, text ="address -", ) 
    lblrdrow.place(x = 50, y = 70) 

    addrss = tk.Entry(root, width = 35) 
    addrss.place(x = 150, y = 70, width = 100) 

    lblfrtrow = tk.Label(root, text ="DOB -", ) 
    lblfrtrow.place(x = 50, y = 90) 

    lblfifrow = Label(root, text ="email -", ) 
    lblfifrow.place(x = 50, y = 110) 

    emil = tk.Entry(root, width = 35) 
    emil.place(x = 150, y = 110, width = 100) 

    lblsixrow = tk.Label(root, text ="age -", ) 
    lblsixrow.place(x = 50, y = 130)      

    ag = tk.Entry(root, width = 35) 
    ag.place(x = 150, y = 130, width = 100)

        
    imagecalen= Button(root, text ="c",  
                              bg ='blue', command = image)
    imagecalen.place(x=130, y=90, width = 10)

    okbtn = Button(root, text ="ok",  
                              bg ='white', command = rom) 
    okbtn.place(x = 150, y = 230, width = 55) 


    submitbtn = Button(root, text ="Submit",  
                              bg ='blue', command = submit) 
    submitbtn.place(x = 150, y = 320, width = 55) 


def filter_dob():

    tree.delete(*tree.get_children())

    global f_1

    temp = f_dob.get()
    print(temp)

    my_cursor.execute("SELECT * FROM madhav WHERE name = %(temp)s",
        {

            'temp': f_dob.get()
        })


    
    result=my_cursor.fetchall()

    for row in result:

        print(row) 

        tree.insert("", tk.END, values=row)
    

def View():

    tree.delete(*tree.get_children())

    my_cursor.execute("SELECT * FROM madhav")

    rows = my_cursor.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    




def searching():
    
    global title,label_1,f_dob,tree,button1,filterbtn

    


    try:
        lblsixrow.place_forget()
        lblfrtrow.place_forget()
        lblrdrow.place_forget()
        lblfifrow.place_forget()
        lblsecrow.place_forget()
        lblfrstrow.place_forget()
        submitbtn.destroy()
        imagecalen.destroy()
        okbtn.destroy()
        Username.destroy()
        passw.destroy()
        emil.place_forget()
        addrss.destroy()
        ag.destroy()
        DOB.destroy()
        title.place_forget()
        label_1.place_forget()
        f_dob.destroy()
        button1.destroy()
        tree.destroy()
        filterbtn.destroy()
    except:
        


        title= Label(root, text = "FILTERING USING dob and address")
        title.place(x=150, y=10)

        
        label_1=Label(root, text ="filter :-")
        label_1.place(x = 0, y = 50)
        
        f_dob=tk.Entry(root, width = 35) 
        f_dob.place(x = 150, y = 50, width = 100)

        tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Username")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Password")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Address")

        tree.column("#4", anchor=tk.CENTER)

        tree.heading("#4", text="Date")

        tree.column("#5", anchor=tk.CENTER)

        tree.heading("#5", text="Email")

        tree.column("#6", anchor=tk.CENTER)

        tree.heading("#6", text="Age")

        tree.column("#7", anchor=tk.CENTER)

        tree.heading("#7", text="ID")

        tree.pack()

        tree.place(x=0, y= 100)

        filterbtn=tk.Button(text="Filter", command = filter_dob)
        filterbtn.place(x=250, y=50)

        button1 = tk.Button(text="Display data", command=View)

        button1.place(x=0, y=400)



        
    else:
        lblsixrow.place_forget()
        lblfrtrow.place_forget()
        lblrdrow.place_forget()
        lblfifrow.place_forget()
        lblsecrow.place_forget()
        lblfrstrow.place_forget()
        submitbtn.destroy()
        imagecalen.destroy()
        okbtn.destroy()
        Username.destroy()
        passw.destroy()
        emil.place_forget()
        addrss.destroy()
        ag.destroy()
        DOB.destroy()
        title.place_forget()
        label_1.place_forget()
        f_dob.destroy()
        button1.destroy()
        tree.destroy()
        filterbtn.destroy()

        

        title= Label(root, text = "FILTERING USING dob and address")
        title.place(x=150, y=10)

        
        label_1=Label(root, text =" filter :-")
        label_1.place(x = 0, y = 50)
        
        f_dob=tk.Entry(root, width = 35) 
        f_dob.place(x = 150, y = 50, width = 100)

        tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Username")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Password")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Address")

        tree.column("#4", anchor=tk.CENTER)

        tree.heading("#4", text="Date")

        tree.column("#5", anchor=tk.CENTER)

        tree.heading("#5", text="Email")

        tree.column("#6", anchor=tk.CENTER)

        tree.heading("#6", text="Age")

        tree.column("#7", anchor=tk.CENTER)

        tree.heading("#7", text="ID")

        tree.pack()

        tree.place(x=0, y= 100)

        button1 = tk.Button(text="Display data", command=View)

        button1.place(x=0, y=400)

        filterbtn=tk.Button(text="Filter", command = donothing)
        filterbtn.place(x=250, y=50)
        

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Main", menu=filemenu)
filemenu.add_command(label="Insert", command=ADDING)
filemenu.add_command(label="Searching", command=searching)
filemenu.add_command(label="Save", command=widget)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
root.mainloop()