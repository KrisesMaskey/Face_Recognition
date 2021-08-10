#Necessary import for program to run
import PIL
import pytesseract
import cv2
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import glob
import face_recognition
import numpy as np
import tkinter.ttk
import tkinter.font as tkFont
from PIL import Image,ImageTk

# method to create Sign-Up GUI 
def open_url(url):
    window = wlcm_scrn = tkinter.Toplevel()
    window.title("Welcome to SecuroServ")
    window.geometry('300x400')
    window.configure(background = "#ef4e6e");
    img_url = "C:/Users/Krises Maskey/Documents/NetBeansProjects/Inventory_Management_System/icons8-user-male-500.png"
    photo = Image.open(img_url)
    resize = ImageTk.PhotoImage(photo.resize((170, 170),Image.ANTIALIAS))
    imframe = tk.Frame(window, width=150, height=150)
    imframe.place(relx=0.5, rely=0.2, anchor=CENTER)
    lbl_img = tk.Label(imframe, image=resize, bg="#ef4e6e")
    lbl_img.pack()
    a = Label(window ,text = "First Name", bg="#ef4e6e").place(relx=0.25, rely=0.45, anchor=CENTER)
    b = Label(window ,text = "Last Name", bg="#ef4e6e").place(relx=0.25, rely=0.55, anchor=CENTER)
    c = Label(window ,text = "Username", bg="#ef4e6e").place(relx=0.25, rely=0.65, anchor=CENTER)
    d = Label(window ,text = "Password", bg="#ef4e6e").place(relx=0.25, rely=0.75, anchor=CENTER)
    a1 = Entry(window)
    a1.place(relx=0.65, rely=0.45, anchor=CENTER)
    b1 = Entry(window)
    b1.place(relx=0.65, rely=0.55, anchor=CENTER)
    c1 = Entry(window)
    c1.place(relx=0.65, rely=0.65, anchor=CENTER)
    d1 = Entry(window)
    d1.place(relx=0.65, rely=0.75, anchor=CENTER)
    def clicked():
        if len(a1.get()) == 0 or b1.index("end") == 0 or c1.index("end") == 0 or d1.index("end") == 0:
            messagebox.showerror("Error Dialog", "Please fill all the details in the fields")
        else:
            #INITIALIZE DATABASE MODEL HERE-------
            messagebox.showinfo("Success Dialog", "Successfully Registered")
    btn = tk.Button(window ,text="Register", command=clicked, bg="#14a0dc").place(relx=0.5, rely=0.88, anchor=CENTER)
    window.mainloop()

#Initializing Tkinter GUI
root = Tk()
root.geometry("750x450")
root.configure(bg="#75A1D0")

#Initializing image frame to show face from camera
imageFrame = tk.Frame(root, width=100, height=100)
imageFrame.grid(row=0, column=0, padx=510, pady=68)
lmain = tk.Label(imageFrame, bg="#75A1D0")
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
canvas=Canvas(root)

#Background image for GUI
path_bg = "C:/Users/Krises Maskey/Documents/NetBeansProjects/Inventory_Management_System/background.jpg"
img_bg = Image.open(path_bg)
resize = ImageTk.PhotoImage(img_bg.resize((500, 600),Image.ANTIALIAS))
imgframe_bg = tk.Frame(root, width=150, height=150)
imgframe_bg.place(relx=0.3, rely=0.35, anchor=CENTER)
lbl_bg = tk.Label(imgframe_bg, image=resize)
lbl_bg.pack()

#User Profile image for GUI
path = "C:/Users/Krises Maskey/Documents/NetBeansProjects/Inventory_Management_System/icons8-user-male-500.png"
img = Image.open(path)
re_size = ImageTk.PhotoImage(img.resize((170, 170),Image.ANTIALIAS))
imgframe = tk.Frame(root, width=150, height=150)
imgframe.place(relx=0.8, rely=0.35, anchor=CENTER)
lbl = tk.Label(imgframe, image=re_size, bg="#75A1D0")
lbl.pack()

#Username & Password Field
user = Entry(root, text="Username", show="", width=25)
pass_ = Entry(root, text="Password", show="*", width=25)
user.place(relx=0.8, rely=0.61, anchor=CENTER)
pass_.place(relx=0.8, rely=0.67, anchor=CENTER)

#Login Button
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
btn = tk.Button(root, text ="  Login  ", font=fontStyle, bg="#90EE90")
btn.place(relx=0.8, rely=0.78, anchor=CENTER)

#INITIALIZE DATABASE MODEL HERE
#---------------------------------------------------------#

#Signup Button
fontStyle = tkFont.Font(family="Lucida Grande", size=8)
label = Label( root, text=" SignUp ? ", bg="#75A1D0", font=fontStyle)
label.place(relx=0.8, rely=0.85, anchor=CENTER)
label.bind("<Button>", open_url)

#Title 
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
label = Label( root, text="   SecuroServ   ", relief=GROOVE, bg="#ffb327", font=fontStyle)
label.place(relx=0.81, rely=0.1, anchor=CENTER)
canvas.config(width=10,height=400, bg="#75A1D0", highlightthickness=0)  

#Canvas values  
line=canvas.create_line(10, 0, 10, 400,fill='#C0C0C0',width=2)
canvas.place(relx=0.6, rely=0.5, anchor=CENTER)


# make array of sample pictures with encodings
known_face_encodings = []
known_face_names = []
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'known_people/')

# make an array of all the saved jpg files' paths
list_of_files = [f for f in glob.glob(path + '*.jpg')]

# find number of known faces
number_files = len(list_of_files)
names = list_of_files.copy()

for i in range(number_files):
    globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
    globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
    known_face_encodings.append(globals()['image_encoding_{}'.format(i)])

    # Create array of known names
    names[i] = names[i].replace("known_people/", "")  
    known_face_names.append(names[i])

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
c=0
count =0

#Show User Profile image after face_recognition authentication fails
def show():
    imgframe.place(relx=0.8, rely=0.35, anchor=CENTER)
    lbl.pack()
    
#method to authenticate face with known_people folder images    
def show_frame():
    global c, count
    btn.configure(state=DISABLED)
        
    imgframe.place_forget()
    lbl.pack_forget()
    process_this_frame = True
    face_locations = []
    face_encodings = []
    face_names = []
    name=""
    ret, frame = cap.read()
    if ret:
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)
        rgb_small_frame = small_frame[:, :, ::-1]
        cv2image = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        
        lmain.imgtk = imgtk
        #lmain.imgtk.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lmain.configure(image=imgtk)
        
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                
                #Show Authentication status 
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    c += 1
                    if c==5:
                        messagebox.showinfo("Success Dialog", "You've successfully logged in!")
                        root.destroy()
                                                                  
                else:
                    count += 1
                    if count ==5 :
                        messagebox.showerror("Error Dialog", "Authentication Failed" +"\n" "Please Login using Username & Password")
                        imageFrame.grid_remove()
                        lmain.grid_remove()
                        cap.release()
                        show()
                        return
                        
                                                                 
                face_names.append(name)

        process_this_frame = not process_this_frame
        lmain.after(10, show_frame)
        
#Face Recognition Button
fontStyle = tkFont.Font(family="Lucida Grande", size=10)
btn = tk.Button(root, text ="  --> Face Recognition <--  ",bd=0, highlightthickness=0, font=fontStyle, bg="#75A1D0", command=show_frame)
btn.place(relx=0.8, rely=0.535, anchor=CENTER)

root.mainloop()
