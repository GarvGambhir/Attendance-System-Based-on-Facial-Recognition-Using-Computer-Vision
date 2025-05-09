from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2.face
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN THE DATASET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        img_top=Image.open(r"images\fr1.jpeg")
        img_top=img_top.resize((1530,325),)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        F_1l=Label(self.root,image=self.photoimg_top)
        F_1l.place(x=0, y=55, width=1530, height=325)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"images\fr2.jpeg")
        img_bottom=img_bottom.resize((1530,325),)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        F_1l=Label(self.root,image=self.photoimg_bottom)
        F_1l.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==========================train the classifier=======================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")
        self.root.destroy()



        
        








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()