import mysql.connector

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
import os

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root) :
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1530x790+0+0")

        #===========================variables================
        self.var_lemail=StringVar()
        self.var_lpas=StringVar()

        img=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\login.jpg")
        img=img.resize((1540,790),)
        self.photoimg=ImageTk.PhotoImage(img)

        F_1l=Label(self.root,image=self.photoimg)
        F_1l.place(x=0,y=0,width=1540,height=790)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\log1.jpeg")
        img1=img1.resize((100,100),)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimage=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimage.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=105)

        #label
        userName=lbl=Label(frame,text="User Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        userName.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_lemail,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=225)

        self.txtpassword=ttk.Entry(frame,textvariable=self.var_lpas,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=250,width=270)

        #loginbutton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register button
        registerbtn=Button(frame,text="New User",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=350,width=160)

        #forgotpassword
        forgotpasswordbtn=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpasswordbtn.place(x=20,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All the fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
            mycursor=conn.cursor()
            mycursor.execute("Select* from register where email=%s and password=%s",(
                                                                                    self.var_lemail.get(),
                                                                                    self.var_lpas.get()
                                                                                    ))
            row=mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid user name and password")
            else:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                
            conn.commit()
            conn.close()

    #==========================================reset pasword=================================================
    def reset(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.security_A_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_password_entry.get()=="":
             messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s and SecurityQ=%s and SecurityA=%s")
            values=(self.txtuser.get(),self.combo_security_Q.get(),self.security_A_entry.get())
            mycursor.execute(query,values)
            row=mycursor.fetchone()
            if row== None:
                messagebox.showerror("Error","Invalid Security Question or Security Answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.new_password_entry.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your Password Has Been Reset",parent=self.root2)
                self.root2.destroy()

    #==========================================forgot password window=========================================
    
    def forgot_password_window(self):
        if self.var_lemail.get()=="":
            messagebox.showerror("Error","Please enter the Email first to Reset the Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row== None:
                messagebox.showerror("Error","Invalid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Foret Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="Red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Teacher's Name","Your Pet Name","Your Favourite Sport")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.security_A_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_A_entry.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.new_password_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_password_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset,text="Reset Password",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=300)









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


        b2=Button(frame,command=self.return_login,image=self.photoimg3,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=440,y=520,width=200)

    #===============================function def===========================

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA=="" or self.var_pass=="" or self.var_comfpass=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        elif self.var_pass.get()!=self.var_comfpass.get():
            messagebox.showerror("Error","Please enter same Password",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already used,Please Try other email",parent=self.root)
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
            messagebox.showinfo("Success","Register Successfully",parent=self.root)
            self.root.destroy()

    def return_login(self):
        self.root.destroy()

class Face_Recognition_System:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # first Img
        img=Image.open(r"images\b1.jpeg")
        img=img.resize((500,130),)
        self.photoimg=ImageTk.PhotoImage(img)

        F_1l=Label(self.root,image=self.photoimg)
        F_1l.place(x=0,y=0,width=500,height=130)

        #second img
        img1=Image.open(r"images\b2.jpeg")
        img1=img1.resize((500,130),)
        self.photoimg1=ImageTk.PhotoImage(img1)

        F_1l=Label(self.root,image=self.photoimg1)
        F_1l.place(x=500,y=0,width=500,height=130)

        #third img3
        img2=Image.open(r"images\b3.jpeg")
        img2=img2.resize((550,130),)
        self.photoimg2=ImageTk.PhotoImage(img2)

        F_1l=Label(self.root,image=self.photoimg2)
        F_1l.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open(r"images\bg.jpeg")
        img3=img3.resize((1530,710),)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #==========================time=========================================================
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        

        #student button
        img4=Image.open(r"images\student.jpeg")
        img4=img4.resize((220,220),)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=400,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=300,width=220,height=40)


        #Detect Face button
        img5=Image.open(r"images\face detector.jpeg")
        img5=img5.resize((220,220),)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=700,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=300,width=220,height=40)
 

         #Attendance button
        img6=Image.open(r"images\attendance.jpeg")
        img6=img6.resize((220,220),)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)


        

        #train data button
        img8=Image.open(r"images\train data.jpeg")
        img8=img8.resize((220,220),)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=400,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=580,width=220,height=40)


        #Photos button
        img9=Image.open(r"images\photos.jpeg")
        img9=img9.resize((220,220),)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=700,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=580,width=220,height=40)



        #Exit button
        img11=Image.open(r"images\exit.jpeg")
        img11=img11.resize((220,220),)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=580,width=220,height=40)

    def open_image(self):
        os.startfile("Data")
    
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure you want to  exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return




    #========================Function buttons============================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

        
        
                                   




if __name__=="__main__":
   main()


