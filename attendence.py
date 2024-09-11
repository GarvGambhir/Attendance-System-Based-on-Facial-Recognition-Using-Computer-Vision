from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import csv
import cv2
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=========================variables==========================
        self.var_attendid=StringVar()
        self.var_attendroll=StringVar()
        self.var_attendname=StringVar()
        self.var_attendtdep=StringVar()
        self.var_attendtime=StringVar()
        self.var_attenddate=StringVar()
        self.var_attend_attendance=StringVar()


        # first Img
        img=Image.open(r"images\s1.jpeg")
        img=img.resize((800,200),)
        self.photoimg=ImageTk.PhotoImage(img)

        F_1l=Label(self.root,image=self.photoimg)
        F_1l.place(x=0,y=0,width=800,height=200)

        #second img
        img1=Image.open(r"images\s2.jpeg")
        img1=img1.resize((800,200),)
        self.photoimg1=ImageTk.PhotoImage(img1)

        F_1l=Label(self.root,image=self.photoimg1)
        F_1l.place(x=800,y=0,width=800,height=200)

        #bg image
        img3=Image.open(r"images\bg.jpeg")
        img3=img3.resize((1530,710),)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendence MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="darkblue",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        mainframe=Frame(bg_img,bd=2,bg="white")
        mainframe.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(mainframe,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"images\s4.jpeg")
        img_left=img_left.resize((720,130),)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        F_1l=Label(left_frame,image=self.photoimg_left)
        F_1l.place(x=5,y=0,width=720,height=130)

        leftside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        leftside_frame.place(x=0,y=135,width=720,height=370)


        #=========labels and entry=========================
        #Attendence id
        Attendenceid_label=Label(leftside_frame,text="Attendence ID:",font=("times new roman",12,"bold"),bg="white")
        Attendenceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendenceID_entry=ttk.Entry(leftside_frame,width=20,textvariable=self.var_attendid,font=("times new roman",12,"bold"))
        AttendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll no
        Rollno_label=Label(leftside_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        Rollno_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Rollno_entry=ttk.Entry(leftside_frame,width=20,textvariable=self.var_attendroll,font=("times new roman",12,"bold"))
        Rollno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        Name_label=Label(leftside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(leftside_frame,width=20,textvariable=self.var_attendname,font=("times new roman",12,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        Department_label=Label(leftside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Department_entry=ttk.Entry(leftside_frame,width=20,textvariable=self.var_attendtdep,font=("times new roman",12,"bold"))
        Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #time
        time_label=Label(leftside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(leftside_frame,width=20,textvariable=self.var_attendtime,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        Date_label=Label(leftside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(leftside_frame,width=20,textvariable=self.var_attenddate,font=("times new roman",12,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendence 
        Attendence_label=Label(leftside_frame,text="Attendence:",font=("times new roman",12,"bold"),bg="white")
        Attendence_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.Attendence_combo=ttk.Combobox(leftside_frame,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),width=18,state="read only")
        self.Attendence_combo["values"]=("Status","Present","Absent")
        self.Attendence_combo.current(0)
        self.Attendence_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #button frame
        btn_frame=Frame(leftside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=730,height=35)

        #import button
        import_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        #export button
        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        


        #right label frame
        right_frame=LabelFrame(mainframe,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)


        #====================scroll bar table============================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Attendance_table=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)


        self.Attendance_table.heading("id",text="Attendance ID")
        self.Attendance_table.heading("roll",text="Roll no")
        self.Attendance_table.heading("name",text="Name")
        self.Attendance_table.heading("department",text="Department")
        self.Attendance_table.heading("time",text="Time")
        self.Attendance_table.heading("date",text="Date")
        self.Attendance_table.heading("attendance",text="Attendance")


        self.Attendance_table.column("id",width=100)
        self.Attendance_table.column("roll",width=100)
        self.Attendance_table.column("name",width=100)
        self.Attendance_table.column("department",width=100)
        self.Attendance_table.column("time",width=100)
        self.Attendance_table.column("date",width=100)
        self.Attendance_table.column("attendance",width=100)


        self.Attendance_table["show"]="headings"
        self.Attendance_table.pack(fill=BOTH,expand=1)
        self.Attendance_table.bind("<ButtonRelease>",self.get_cursor)


    #=====================================fetch data=================================
    def fetch_data(self,rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
    
    #=======================================Export data======================================================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO DATA","No Data To Export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata: 
                    exp_write.writerow(i)
                messagebox.showinfo("DATA EXPORTED","Data has been exported to "+os.path.basename(fin)+"successfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    
    #======================get cursor=================================
    def get_cursor(self,event=""):
        cursor_focus=self.Attendance_table.focus()
        content=self.Attendance_table.item(cursor_focus)
        data=content["values"]

        self.var_attendid.set(data[0]),
        self.var_attendroll.set(data[1]),
        self.var_attendname.set(data[2]),
        self.var_attendtdep.set(data[3]),
        self.var_attendtime.set(data[4]),
        self.var_attenddate.set(data[5]),
        self.var_attend_attendance.set(data[6]),

    
        
        




















if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()