from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
from time import strftime
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # 2nd image
        img_right = Image.open(r"images\fr4.jpeg")
        img_right = img_right.resize((1550, 700))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        F_1l = Label(self.root, image=self.photoimg_right)
        F_1l.place(x=0, y=55, width=1550, height=700)

        # button
        b1_1 = Button(F_1l, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=550, y=450, width=500, height=60)


    #====================================attendance==========================================================
    def mark_attendance(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myData=f.readlines()
            name_list=[]
            for line in myData:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")


    

    # ================================face Recognition=========================================================
    
    def face_recog(self):
        def draw_boundary(img, classifier, scalefactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Gagam@2005", database="face_recognizer")
                mycursor = conn.cursor()
                mycursor.execute("select Name from student where Student_id=" + str(id))
                n = mycursor.fetchone()
                n = "+".join(n)

                mycursor.execute("select Roll from student where Student_id=" + str(id))
                r = mycursor.fetchone()
                r = "+".join(r)

                mycursor.execute("select Dep from student where Student_id=" + str(id))
                d = mycursor.fetchone()
                d = "+".join(d)

                mycursor.execute("select Student_id from student where Student_id=" + str(id))
                i = mycursor.fetchone()
                i = "+".join(i)

                if confidence < 90:
                    cv2.putText(img, f"ID:{i}", (x, y- 75), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
