import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from detection import load_yolo, detect_objects

# Inicializar YOLO
net, output_layers, classes = load_yolo()

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Camera feedback")
root.geometry("1280x720")

lbl = Label(root)
lbl.pack()

def image_capture():
    ret, frame = cap.read()
    if ret:
        outputs, width, height = detect_objects(frame, net, output_layers)
        
        # Exibir imagem no Tkinter
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)

def start_capture():
    global capturing
    capturing = True
    toggle_btn.config(text="Stop Capture")
    capture_frames()

def stop_capture():
    global capturing
    capturing = False
    lbl.configure(image='')
    toggle_btn.config(text="Start Capture")

def capture_frames():
    if capturing:
        image_capture()
        lbl.after(10, capture_frames)

capturing = False

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

toggle_btn = tk.Button(button_frame, text="Start Capture", command=lambda: start_capture() if not capturing else stop_capture(), width=20, height=2)
toggle_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
cap.release()
