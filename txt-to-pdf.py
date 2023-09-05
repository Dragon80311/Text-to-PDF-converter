
import tkinter 
import customtkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os
image= ''
# function to convert images to PDF
def images_to_pdf(images, pdf_name):
    try:
        # create a new pdf file
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", "Image has been successfully converted to PDF.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))
# function to select images
def select_image():
    global image
    image = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")), initialdir = "C:/")
    l2 = tk.CTkLabel(root,text="Please Select location and name for PDF").grid(row=2)
    b1= tk.CTkButton(root,text="Save",command= select_pdf).grid(row=3)
# function to select pdf name and path
def select_pdf():
    pdf = tk.filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", initialdir = "C:/", filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    images_to_pdf(image,pdf)
# create GUI
tk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
tk.set_default_color_theme("blue")
root = tk.CTk()  # defining Root for GUI
root.title("Convert Images to PDF")
root.geometry("230x300")
ll = tk.CTkLabel(root,text="Welcome to PDf converter \n Please choose image to be converted",anchor="center").grid(row=0)
convert_btn = tk.CTkButton(root, text="Select Image",anchor="center", command=select_image).grid(row=1)  
root.mainloop()


