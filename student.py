from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("NTCC-2024-FACE_RECOGNITION System")

        #==================================================variables=================================================================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # first Img
        img=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\s1.jpeg")
        img=img.resize((500,130),)
        self.photoimg=ImageTk.PhotoImage(img)

        F_1l=Label(self.root,image=self.photoimg)
        F_1l.place(x=0,y=0,width=500,height=130)

        #second img
        img1=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\s2.jpeg")
        img1=img1.resize((500,130),)
        self.photoimg1=ImageTk.PhotoImage(img1)

        F_1l=Label(self.root,image=self.photoimg1)
        F_1l.place(x=500,y=0,width=500,height=130)

        #third img3
        img2=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\s3.jpeg")
        img2=img2.resize((550,130),)
        self.photoimg2=ImageTk.PhotoImage(img2)

        F_1l=Label(self.root,image=self.photoimg2)
        F_1l.place(x=1000,y=0,width=550,height=130)


        #bg image
        img3=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\bg.jpeg")
        img3=img3.resize((1530,710),)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        mainframe=Frame(bg_img,bd=2,bg="white")
        mainframe.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(mainframe,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\s4.jpeg")
        img_left=img_left.resize((720,130),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        F_1l=Label(left_frame,image=self.photoimg_left)
        F_1l.place(x=20,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=740,height=115)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="read only")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        Subject_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        Subject_label.grid(row=0,column=2,padx=10)

        Subject_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="read only")
        Subject_combo["values"]=("Select course","FY","SY","TY","LY")
        Subject_combo.current(0)
        Subject_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)




        #Class Student Information 
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=740,height=300)

        #Student id
        Studentid_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        Studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        StudentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="read only")
        class_div_combo["values"]=("Select Division","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Roll no
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)




        #Date of birth
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        phone_label=Label(class_Student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_Student_frame,text="Teacher name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=730,height=35)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #button frame
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=730,height=35)

        #take photo sample
        take_photo_btn=Button(btn_frame1,command=self.gererate_dataset,text="Take Photo Sample",width=36,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.place(x=0,y=0,width=730,height=35)

        

        
        #right label frame
        right_frame=LabelFrame(mainframe,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=680,height=580)


        img_right=Image.open(r"C:\Users\GARV GAMBHIR\Desktop\NTCC-2024-FACE_RECOGNITION\images\s5.jpeg")
        img_right=img_right.resize((660,180),)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        F_1l=Label(right_frame,image=self.photoimg_right)
        F_1l.place(x=10,y=10,width=660,height=180)



        #=====================table frame===================================
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=665,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #================================================funtion declaration===============================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()                           
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
                self.root.destroy()
               

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #===========================================fetching data from database================================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
        mycursor=conn.cursor()
        mycursor.execute("Select* from Student")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===========================================get cursor================================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),


    #==============================================================update function======================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this students details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
                    mycursor=conn.cursor()
                    mycursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s, Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s, PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.va_std_id.get(),                                                                 
                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                self.root.destroy()
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #=========================================delete function=======================================================
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Details","Do you want to detele this record",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
                    mycursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successully Deleted","Successully Deleted Student details ",parent=self.root)
                self.root.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    

    #=========================================reset function=======================================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #=================================================Generating dataset or take photo sample=============================================
    def gererate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gagam@2005",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s, Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s, PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.va_std_id.get()==id+1                                                                
                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===========================Load predefined data on face frontals from opencv===========================================
                    
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #Minimum Neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)    
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data set generation completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)





    
        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

