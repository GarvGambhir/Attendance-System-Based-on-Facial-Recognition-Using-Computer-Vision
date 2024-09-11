from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        #====================================variables===============================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_contact=StringVar()
        self.var_pass=StringVar()
        self.var_comfpass=StringVar()

        #===============================bg image===============
        img=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\reg1.jpeg")
        img=img.resize((1540,790),)
        self.photoimg=ImageTk.PhotoImage(img)

        F_1l=Label(self.root,image=self.photoimg)
        F_1l.place(x=0,y=0,width=1540,height=790)

        #============================mainframe======================================
        frame=Frame(self.root,bg="white")
        frame.place(x=340,y=100,width=850,height=600)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),bg="white",fg="Blue")
        register_lbl.place(x=280,y=20)

        #========================labels and entry==============================================
        #========================1row===========================================
        fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",20,"bold"))
        fname_entry.place(x=50,y=135,width=300)

        lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="white")
        lname.place(x=450,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",20,"bold"))
        lname_entry.place(x=450,y=135,width=300)

        #====================================row2===========================================
        contact=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact.place(x=50,y=200)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",20,"bold"))
        contact_entry.place(x=50,y=235,width=300)

        email=Label(frame,text="Email Id",font=("times new roman",20,"bold"),bg="white")
        email.place(x=450,y=200)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",20,"bold"))
        email_entry.place(x=450,y=235,width=300)

         #====================================row3===========================================
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",20,"bold"),bg="white")
        security_Q.place(x=50,y=300)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",20,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Teacher's Name","Your Pet Name","Your Favourite Sport")
        self.combo_security_Q.place(x=50,y=335)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="white")
        security_A.place(x=450,y=300)

        security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",20,"bold"))
        security_A_entry.place(x=450,y=335,width=300)

         #====================================row4===========================================
        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=400)

        password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",20,"bold"))
        password_entry.place(x=50,y=435,width=300)

        confirm_p=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        confirm_p.place(x=450,y=400)

        confirm_p_entry=ttk.Entry(frame,textvariable=self.var_comfpass,font=("times new roman",20,"bold"))
        confirm_p_entry.place(x=450,y=435,width=300)

        #===================checkbutton=========================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree With The Terms and Condition",font=("times new roman",10,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=480)

        #=======================button==================================================
        img1=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\reg2.jpeg")
        img1=img1.resize((200,50),)
        self.photoimg2=ImageTk.PhotoImage(img1)


        b1=Button(frame,image=self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=200,y=520,width=200)

        img3=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\reg3.png")
        img3=img3.resize((200,50),)
        self.photoimg3=ImageTk.PhotoImage(img3)


        b2=Button(frame,image=self.photoimg3,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=440,y=520,width=200)

    #===============================function def===========================

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA=="" or self.var_pass=="" or self.var_comfpass=="":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_comfpass.get():
            messagebox.showerror("Error","Please enter same Password")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already used,Please Try other email")
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")
            
        







if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
