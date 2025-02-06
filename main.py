import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Camera feedback")
root.geometry("1280x720")

lbl = Label(root)
lbl.pack()

def image_capture():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)

def start_capture():
    global capturing
    capturing = True
    start_btn.config(state=tk.DISABLED)
    stop_btn.config(state=tk.NORMAL)
    capture_frames()

def stop_capture():
    global capturing
    capturing = False
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)

def capture_frames():
    if capturing:
        image_capture()
        lbl.after(10, capture_frames)

capturing = False

start_btn = tk.Button(root, text="Start Capture", command=start_capture)
start_btn.pack()

stop_btn = tk.Button(root, text="Stop Capture", command=stop_capture)
stop_btn.pack()

root.mainloop()

cap.release()