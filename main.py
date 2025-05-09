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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()