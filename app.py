import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from functions import yolo_real_time, yolo_image_input

def show_main_menu():
    
    clear_window()
    label = tk.Label(root, text="Choose detection mode:", font=("Helvetica", 16), fg="white", bg="#2C3E50")
    label.pack(pady=20)

    button_real_time = tk.Button(root, text="Real-Time Detection", command=real_time_screen, 
        font=("Helvetica", 12), 
        bg="#1ABC9C", 
        fg="white", 
        relief="raised", 
        padx=20, 
        pady=10)
    
    button_real_time.pack(pady=10)

    button_image_input = tk.Button(root, text="Detect from Image Input", command=image_input_screen, 
        font=("Helvetica", 12), 
        bg="#3498DB", 
        fg="white", 
        relief="raised", 
        padx=20, 
        pady=10)
    
    button_image_input.pack(pady=10)

def real_time_screen():
    
    clear_window()

    button_back = tk.Button(root, text="Back to Main Menu", command=show_main_menu, 
        font=("Helvetica", 12), 
        bg="#E74C3C", 
        fg="white", 
        relief="raised", 
        padx=20, 
        pady=10)
    
    button_back.pack(pady=10)

    video_label = tk.Label(root)
    video_label.pack()

    yolo_real_time(video_label)

def image_input_screen():
    
    clear_window()

    button_back = tk.Button(root, text="Back to Main Menu", command=show_main_menu, 
        font=("Helvetica", 12), 
        bg="#E74C3C", 
        fg="white", 
        relief="raised", 
        padx=20, 
        pady=10)
    
    button_back.pack(pady=10)

    image_label = tk.Label(root)
    image_label.pack()

    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

    if image_path:
        yolo_image_input(image_path, image_label)

def clear_window():
    
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.geometry("800x600")  
root.title("YOLO Detection")
root.config(bg="#2C3E50")  

show_main_menu()

root.mainloop()