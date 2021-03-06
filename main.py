from PIL import Image, ImageTk
import glob
import math
import random
import Augmentor
import os

noimg = Image.open("data/image/stored/noimage.png")
noimg.save('done.png') #Set initial 'noimage' message

def openwater():
    global water_image
    water_image = tkinter.filedialog.askopenfilename(title='open')

def file_prompt():
    global current_image
    current_image = tkinter.filedialog.askopenfilename(title='open')
    return current_image

def display_img(initt):

    #Check if the 'no image' image or the product image is needed to be displayed
    if initt == True:
        x = "done.png" #Display 'no image' or product
    else:
        x = file_prompt() #Prompts user to pick new image

    #Set Blank Image, needed for removing old image otherwise it results in a messy stack of layers after continued use
    white_img = Image.new('RGB', (500, 500), (255, 255, 255))
    img = ImageTk.PhotoImage(white_img)
    panel = tk.Label(r, image=img)
    panel.image = img
    panel.grid(row=1, column=4)

    #Set New Image
    img = Image.open(x)
    img_w, img_h = img.size
    img.thumbnail((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(r, image=img)
    panel.image = img
    panel.grid(row=1, column=4)

def apply():
    img = Image.open(current_image)
    img3 = Image.open(current_image)
    base_w, base_h = img.size

    water = Image.open(water_image).convert("RGBA")
    water.save("data/image/logo/logo.png")

    files = glob.glob("data/image/logo/output/*") #Erases all old files left in output
    for f in files:
        os.remove(f)

    p = Augmentor.Pipeline("data/image/logo")
    p.random_distortion(probability=float(int(probability_entry.get()) / 100), grid_width=int(grid_W_entry.get()), grid_height=int(grid_H_entry.get()), magnitude=int(distortion_entry.get())) #Distorts watermark based on parameters
    p.sample(1) #Saves distorted watermark to logo/output in a png format

    img2 =  Image.open((glob.glob("data/image/logo/output/*.png"))[0]) #Augmentor doesn't allow set paths so you must pull the first file in a specific directory
    mark_w, mark_h = img2.size
    new_w, new_h = (random.randint(0, base_w - mark_w), random.randint(0, base_h - mark_h)) #Randomize placement position of watermark
    img3.paste(img2, (new_w, new_h), img2)
    img3.putalpha(140) #Sets opacity of watermark
    img.paste(img3, img3) #Pastes watermark over image

    img.save('done.png') #Saves the product image
    display_img(True) #Updates image display


####Tkinter section
import tkinter as tk
import tkinter.filedialog

r = tk.Tk()
r.title('Watermarker')

display_img(True)

dinsert = tk.StringVar()
pinsert = tk.StringVar()
g_w_insert = tk.StringVar()
g_h_insert = tk.StringVar()

btn = tk.Button(r, text='Select Image', width=25, command= lambda:display_img(False)).grid(row=2, column=1)
btn = tk.Button(r, text='Select Watermark', width=25, command=openwater).grid(row=3, column=1)
button = tk.Button(r, text='Produce Image', width=25, command=apply).grid(row=4, column=1)

#Distortion
dinsert.set('25')
distortion_entry_label = tk.Label(r, text="Distortion").grid(row=2, column=5)
distortion_entry = tk.Entry(r, textvariable=dinsert)
distortion_entry.grid(row=2, column=6)

#Probability
pinsert.set('100')
probability_entry_label = tk.Label(r, text="Probability %").grid(row=3, column=5)
probability_entry = tk.Entry(r, textvariable=pinsert)
probability_entry.grid(row=3, column=6)

#Grid Width
g_w_insert.set('4')
grid_W_entry_label = tk.Label(r, text="Grid Width").grid(row=4, column=5)
grid_W_entry = tk.Entry(r, textvariable=g_w_insert)
grid_W_entry.grid(row=4, column=6)

#Grid Height
g_h_insert.set('4')
grid_H_entry_label = tk.Label(r, text="Grid Height").grid(row=5, column=5)
grid_H_entry = tk.Entry(r, textvariable=g_h_insert)
grid_H_entry.grid(row=5, column=6)

r.resizable(0, 0)
r.mainloop()
