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
    lbl.configure(image='')  # Clear the image from the label
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)

def capture_frames():
    if capturing:
        image_capture()
        lbl.after(10, capture_frames)

capturing = False

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

toggle_btn = tk.Button(button_frame, text="Start Capture", command=lambda: toggle_capture(toggle_btn), width=20, height=2)
toggle_btn.pack(side=tk.LEFT, padx=5)

def toggle_capture(button):
    global capturing
    if capturing:
        capturing = False
        lbl.configure(image='')  # Clear the image from the label
        button.config(text="Start Capture")
    else:
        capturing = True
        button.config(text="Stop Capture")
        capture_frames()

root.mainloop()

cap.release()