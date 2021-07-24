from Tkinter import *
from tkMessageBox import *
import sqlite3
root=Tk()
root.title("Database Read/Write")
#root.attributes('-fullscreen',True)

Label(root,text="VOTING PANNEL",font="CalibriLight 15 bold",bg="white",padx=15).pack(side=TOP)
class App:
    
    def __init__(self,m):
        
        frame = Frame(m,bg="lightgreen")
        frame.pack()
        self.zx=StringVar()
        self.v=IntVar()
        a = StringVar()
        b = StringVar()
        a1 = StringVar()
        b1 = StringVar()
        c = StringVar()
        self.vairable=StringVar()
        self.sql=StringVar()
        self.sql1=StringVar()
        self.sql2=StringVar()
        self.word=StringVar()
        self.w=OptionMenu(frame,self.vairable,"ADMIN","GUEST")
        self.w.grid(row=4,column=0)
        self.ab=StringVar()
        self.ab1=StringVar()
        self.ab2=StringVar()
        
        self.v0=IntVar()
        self.button3=Button(frame, text=  "SIGN UP", padx=5,width=5 ,height=1,command=self.newwin,fg="red",bg="lightblue",bd=7)
        self.button3.grid(row=8,column=1)
        self.button4=Button(frame, text='LOGIN', padx=5,width=4,height=1,command=self.Error,fg="white",bg="blue",bd=7)
        self.button4.grid(row=4,column=1)
        self.button15 = Button(frame,  text = 'EXIT', padx=5,width=5,height=1, command=self.Quit,fg="red",bg="lightblue",bd=7)
        self.button15.grid(row=8,column=5)
        self.button3=Button(frame, text=  "ABOUT",width=5 ,height=1,command=self.aboutus,fg="red",bd=7,bg="lightblue")
        self.button3.grid(row=8,column=0)

        self.label=Label(frame,text="Enter your ID",bg="lightgreen",font=5)
        self.label.grid(row=1,column=0)
        self.label=Label(frame,text="If you have not Registered yet!",bg="lightgreen",font="bold 11")
        self.label.grid(row=7,column=1)
        self.label=Label(frame,text="Enter your password",bg="lightgreen",font=5)
        self.label.grid(row=3,column=0)
        
        self.a = Entry(frame,bd=8)
        self.a.grid(row=1,column=1)
        self.c = Entry(frame,show='*',bd=8)
        self.c.grid(row=3,column=1 )
        
    def close(self):
        q1=self.vairable.get()
        self.con=sqlite3.connect('devanjali')
        self.cur = self.con.cursor()
        v0= StringVar()
        cv=self.a.get()
        s=self.c.get()
        print s
        self.cur.execute('select fname from xxxx where Passw =?',(s,))
        r=(self.cur.fetchall())
        print(r)
        

        
        if(q1=="ADMIN"):
            if(s == 'Pandey'):
   
                r3=Tk()
                ab=''
                r3.title("Admin Pannel")
                self.label=Label(r3,text="WELCOME ADMIN",font="CalibriLight 15 bold",fg="blue")
                self.label.grid(row=0,column=1)
                self.label1=Label(r3,text="Your information is in encripted form.......")
                self.label1.grid(row=1,column=0)
                self.label=Label(r3,text="search within the database as you want ADMIN by fname",font="CalibriLight 11 bold")
                self.label.grid(row=6,column=0)
                self.sql = "SELECT Fname FROM xxxx WHERE Passw =?"
                def readData():
                    for row in self.cur.execute(self.sql, [(s)]):
                    
                        self.ab=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
    
                    
               
                readData()
            
            
                self.sql1 = "SELECT email FROM xxxx WHERE Passw =?"
                def readData1():
                    for row in self.cur.execute(self.sql1, [(s)]):
                    
                        self.ab1=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
       
               
                readData1()
                self.sql2 = "SELECT Passw FROM xxxx WHERE Passw =?"
                def readData2():
                    for row in self.cur.execute(self.sql2, [(s)]):
                    
                        self.ab2=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
    
              
                readData2()
                self.label29=Label(r3,text=self.ab)
                self.label29.grid(row=2,column=1)
                self.label28=Label(r3,text=self.ab1)
                self.label28.grid(row=3,column=1)
                self.label27=Label(r3,text=self.ab2)
                self.label27.grid(row=4,column=1)
                self.button9=Button(r3, text=  "LIST ALL", padx=5,width=5 ,height=1,command=self.printit,fg="red",bg="black",bd=7)
                self.button9.grid(row=5,column=1)
                self.d=Entry(r3)
                self.d.grid(row=6,column=1)
                self.button6 = Button(r3,  text = 'SEARCH', padx=5,width=5,height=1, command=self.search,fg="blue",bg="black",bd=7)
                self.button6.grid(row=7,column=1)
                self.label21=Label(r3,text="Name",font="CalibriLight 9 bold",fg="red")
                self.label21.grid(row=2,column=0)
                self.label22=Label(r3,text="Email ID",font="CalibriLight 9 bold",fg="red")
                self.label22.grid(row=3,column=0)
                self.label23=Label(r3,text="Paswword",font="CalibriLight 9 bold",fg="red")
                self.label23.grid(row=4,column=0)
                self.a.delete(0,END)
                self.c.delete(0,END)
                r3.geometry("700x300")
                r3.mainloop()
            else:
                s=showerror(title="ERROR",message="Incorect ID or Password")
            
        elif(q1=="GUEST"):
            self.sql2 = "SELECT Passw FROM xxxx WHERE Passw =?"
            def readData2():
                for row in self.cur.execute(self.sql2, [(s)]):
                    
                    self.ab2=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
            readData2()
            self.sql1 = "SELECT email FROM xxxx WHERE Passw =?"
            def readData1():
                
                for row in self.cur.execute(self.sql1, [(s)]):
                    
                    self.ab1=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
            readData1()
            if(s == self.ab2 and cv == self.ab1):
                
                r3=Tk()
                r3.title("Guest window")
                
                self.label1=Label(r3,text="your information is in encripted form...",font="-weight bold")
                self.label1.grid(row=1,column=0)
                self.cur.execute('select * from xxxx where Passw =?',(s,))
                f=(self.cur.fetchall())

                self.sql = "SELECT Fname FROM xxxx WHERE Passw =?"
                def readData():
                    for row in self.cur.execute(self.sql, [(s)]):
                    
                        self.ab=(str(row).replace(')',' ').replace('(',' ').replace('u\'',' ').replace("'"," ").replace(",",""))
                readData()
                self.sql1 = "SELECT email FROM xxxx WHERE Passw =?"
                def readData1():
                    for row in self.cur.execute(self.sql1, [(s)]):
                    
                        self.ab1=(str(row).replace(')',' ').replace('(',' ').replace('u\'',' ').replace("'"," ").replace(",",""))
    
                
                self.label=Label(r3,text="Welcome"+self.ab,fg="red",font=9)
                self.label.grid(row=0,column=1,columnspan=4)
                readData1()
                self.sql2 = "SELECT Passw FROM xxxx WHERE Passw =?"
                def readData2():
                    for row in self.cur.execute(self.sql2, [(s)]):
                    
                        self.ab2=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
                readData2()
                
                l1=IntVar()
                self.label29=Label(r3,text=self.ab)
                self.label29.grid(row=2,column=1)
                self.label28=Label(r3,text=self.ab1)
                self.label28.grid(row=3,column=1)
                self.label27=Label(r3,text=self.ab2)
                self.label27.grid(row=4,column=1)
                self.label21=Label(r3,text="Name",font="CalibriLight 11 bold",fg="red")
                self.label21.grid(row=2,column=0)
                self.label22=Label(r3,text="Email ID",font="CalibriLight 11 bold",fg="red")
                self.label22.grid(row=3,column=0)
                self.label23=Label(r3,text="Paswword",font="CalibriLight 11 bold",fg="red")
                self.label23.grid(row=4,column=0)
                
                self.label124=Label(r3,text="Please Give Your VOTE Here",fg="green",font="-weight bold")
                self.label124.grid(row=5,column=0)
               
                self.button64 = Button(r3, text = 'VOTE IT', padx=20,width=5,height=1, command=self.storevote,fg="orange")
                self.button64.grid(row=10,column=1,columnspan=3,pady=5)
                

                self.radiobutton0=Radiobutton(r3,text="Vote1",padx=20,variable=self.v0,value=1)
                self.radiobutton0.grid(row=9,column=0)
                self.radiobutton11=Radiobutton(r3,text="Vote2",variable=self.v0,value=2)
                self.radiobutton11.grid(row=9,column=1)
                self.radiobutton2=Radiobutton(r3,text="Vote3",variable=self.v0,value=3)
                self.radiobutton2.grid(row=9,column=2)
                self.radiobutton3=Radiobutton(r3,text="Vote4",padx=20,variable=self.v0,value=4)
                self.radiobutton3.grid(row=9,column=3)
                m1=(self.v0.get())
                print (m1)
                self.label32=Label(r3,text="Vote For Mr X",font="CalibriLight 8 bold")
                self.label32.grid(row=6,column=0)
                self.label33=Label(r3,text="Vote For Mr. Y",font="CalibriLight 8 bold")
                self.label33.grid(row=6,column=1)
                self.label34=Label(r3,text="Vote For Mr. Z",font="CalibriLight 8 bold")
                self.label34.grid(row=6,column=2)
                self.label35=Label(r3,text="Vote For Mr. XYZ",font="CalibriLight 8 bold")
                self.label35.grid(row=6,column=3)
                self.a.delete(0,END)
                self.c.delete(0,END)
                
                r3.geometry("700x300")
                r3.mainloop()
                
            else:
                s=showerror(title="Error",message="Incorrect Email ID OR Password")    
           
     
        self.a.delete(0,END)
        self.c.delete(0,END)
    
    def printit(self):
        self.con=sqlite3.connect('devanjali')
        self.cur = self.con.cursor()
        self.cur.execute('SELECT * FROM xxxx')
        print(self.cur.fetchall())
    def search(self):
        self.con=sqlite3.connect('devanjali')
        self.cur = self.con.cursor()
        s=self.d.get()
        self.cur.execute("select fname,Passw from xxxx where fname =(?)",(s,))
        print(self.cur.fetchall())


    def newwin(self):
        self.r1=Tk()
        frame2 = Frame(self.r1,bg="lightblue")
        frame2.pack()
        
        f= IntVar()
        self.r1.geometry("725x192")
        self.r1.title("Register")
        self.con=sqlite3.connect('devanjali')
        self.cur = self.con.cursor()
        self.label=Label(frame2,text="Register your information to this page",fg="black",bg="lightblue",font="CalibriLight 17 bold")
        self.label.grid(row=0,column=1)
        
        self.button7 = Button(frame2,text = 'REGISTER', padx=10,width=10,height=2,fg="orange",bg="lightgreen",font=3,command=self.Error1,bd=7)
        self.button7.grid(row=5,column=1)
       
        self.radiobutton=Radiobutton(frame2,text="Male",bg="lightblue",font="CalibriLight 11 bold",padx=20,variable=self.v,value=0)
        self.radiobutton.grid(row=4,column=0)
        self.radiobutton1=Radiobutton(frame2,text="Female",bg="lightblue",font="CalibriLight 11 bold",padx=20,variable=self.v,value=2)
        self.radiobutton1.grid(row=4,column=1)
        
        self.label=Label(frame2,text="First Name",fg="orange",font="CalibriLight 11 bold",bg="lightblue")
        self.label.grid(row=1,column=0)
        self.label=Label(frame2,text="Last Name",fg="orange",font="CalibriLight 11 bold",bg="lightblue")
        self.label.grid(row=1,column=2)
        self.label=Label(frame2,text="Email ID",fg="orange",font="CalibriLight 11 bold",bg="lightblue")
        self.label.grid(row=2,column=0)
        self.label=Label(frame2,text="Password",fg="orange",font="CalibriLight 11 bold",bg="lightblue")
        self.label.grid(row=3,column=0)
        
        
        
        self.e = Entry(frame2,bd=4)
        self.e.grid(row=1,column=1)
        self.f = Entry(frame2,bd=4)
        self.f.grid(row=1,column=3)
        self.g = Entry(frame2,bd=4)
        self.g.grid(row=2,column=1)
        self.h=Entry(frame2,bd=4)
        self.h.grid(row=3,column=1)
        self.r1.mainloop()
    def insert1(self):
        
        self.con=sqlite3.connect('devanjali')
        self.cur = self.con.cursor()
        #self.cur.execute("CREATE TABLE xxxx(fname stringvar(10),lname stringvar(10),email stringvar(10),Passw stringvar(10))")
        x = (self.e.get())
        x1 =(self.f.get())
        y= self.g.get()
        z =(self.h.get())
        as1=self.v.get()
        print as1
        self.cur.execute("insert into xxxx( fname,lname,email,Passw)  values(?, ?, ?,?)",(x,x1,y,z))
        self.con.commit()
        self.dest()
        return
    def Error(self):
        if(str(self.a.get())==''or str(self.c.get())==''):
            s=showerror(title="ERROR",message="Fill the entries")
            #root.destroy()
        else:
            self.close()
    def Error1(self):
        if(str(self.e.get())==''or str(self.h.get())==''or str(self.g.get())==''or str(self.h.get())==''):
            s=showerror(title="ERROR",message="Fill the entries")
        else:
            self.insert1()
    def Quit(self):
        root.destroy()
    def dest(self):
        self.r1.destroy()
    def aboutus(self):
        
        self.master=Tk()
        self.master.attributes('-fullscreen',True)

        shortcutbar = Frame(self.master, height=30, bg='black')
        toolbar = Label(shortcutbar, text='Jaypee University of Engineering & Technology(Guna)',bg='black',fg='white',height=2,font='Times 16 bold')
        toolbar.pack(side=TOP,fill=X,expand=YES)
        shortcutbar.pack(expand=NO, fill=X)
        Label(self.master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(self.master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(self.master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(self.master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(self.master, text='\n\n\n\n\n\n\nThe project is designed by',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
        Label(self.master, text='Name:             Devanjali Pandey (171b046)',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
        Label(self.master, text='\nUnder the guiadence of',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
        Label(self.master, text='Dr. Mahesh Kumar',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
        
    
        s = Frame(self.master, height=30, bg='skyblue')
        Button(s, text='EXIT',width=16,height=1,bg='lightgrey',fg='black',font='Times 12 bold',command=self.master.destroy).pack(side=LEFT, anchor=SW)
        s.pack(side=BOTTOM,expand=NO, fill=X)
        Label(self.master, text='ADMIN ID:devanjali       PASSWORD:Pandey',fg='black',font='Times 13').pack(side=BOTTOM,anchor=CENTER)
    def storevote(self):
        self.con=sqlite3.connect('devanjali')
        self.cur = self.con.cursor()
        #self.cur.execute("CREATE TABLE vote(nameC stringvar(10),Age stringvar(10),Vote number(10))")
        e2=(self.v0.get())
        #print type(e2)
        #print e2
        r8=Tk()
        r8.title("Voting")
        r8.geometry("200x200")
        z0=StringVar()
        k2=IntVar()
        if(e2 == 1):
            z0= 'Mr X'
            k2=25
        elif(e2== 2):
            z0= 'Mr Y'
            k2=50
        elif(e2== 3):
            z0= 'Mr Z'
            k2=43
        else:
            z0= 'Mr XYZ'
            k2=35
        self.label=Label(r8,text="THANKS FOR VOTING"+" "+z0,font="Times 9 bold",fg="blue")
        self.label.grid(row=0,column=1)
        self.cur.execute("insert into vote(nameC,Age,Vote)  values(?, ?,?)",(z0,k2,e2))
        r8.mainloop()
#root.geometry('700x300')
app = App(root)
root.mainloop()
