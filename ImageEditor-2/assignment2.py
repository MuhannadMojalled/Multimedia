from tkinter import *
import customtkinter
from PIL import ImageTk, Image, ImageEnhance
from tkinter import filedialog
from jes4py import *


# open the image
def open_img():
    global file, img, pixels
    file = pickAFile()
    img = makePicture(file)
    pixels = getPixels(img)
    plabel1.pack(padx=5)
    slider1.pack()
    abutton1.pack(pady=5)
    plabel2.pack(padx=5)
    slider2.pack()
    abutton2.pack(pady=5)
    plabel3.pack(padx=5)
    slider3.pack()
    abutton3.pack(pady=5)


# Scale Down
def myScalingDown(img, sPercentage):
    x = 100 - sPercentage
    x = 100 / x
    src = img
    sourcex = 0
    w = getWidth(src)
    h = getHeight(src)
    canvas = makeEmptyPicture(w / x, h / x)
    for targetx in range(0, int((w - 1) / x)):
        sourceY = 0
        for targetY in range(0, int((h - 1) / x)):
            color = getColor(getPixel(src, sourcex, sourceY))
            setColor(getPixel(canvas, targetx, targetY), color)
            sourceY += x
        sourcex += x
    addText(src, w / 2, 0, "ORIGINAL")
    addText(canvas, (w / x) / 2, 0, " SCALED DOWN")
    explore(src)
    explore(canvas)


# Scale Up percentage
def myScalingUpP(img, sPercentage):
    src = img
    sPercentage = sPercentage / 100
    sPercentage = 1 + sPercentage
    sourcex = 0
    w = getWidth(src)
    h = getHeight(src)
    canvas = makeEmptyPicture(w * sPercentage, h * sPercentage)
    for targetx in range(0, int((w - 1) * sPercentage)):
        sourceY = 0
        for targetY in range(0, int((h - 1) * sPercentage)):
            color = getColor(getPixel(src, sourcex, sourceY))
            setColor(getPixel(canvas, targetx, targetY), color)
            sourceY += 1 / sPercentage
        sourcex += 1 / sPercentage
    addText(src, w / 2, 0, "ORIGINAL")
    addText(canvas, (w * sPercentage) / 2, 0, " SCALED UP")
    explore(src)
    explore(canvas)


# Scale Up Times
def myScalingUpTimes(img, sPercentage):
    src = img
    sourcex = 0
    w = getWidth(src)
    h = getHeight(src)
    canvas = makeEmptyPicture(w * sPercentage, h * sPercentage)
    for targetx in range(0, int((w - 1) * sPercentage)):
        sourceY = 0
        for targetY in range(0, int((h - 1) * sPercentage)):
            color = getColor(getPixel(src, sourcex, sourceY))
            setColor(getPixel(canvas, targetx, targetY), color)
            sourceY += 1 / sPercentage
        sourcex += 1 / sPercentage
    addText(src, w / 2, 0, "ORIGINAL")
    addText(canvas, (w * sPercentage) / 2, 0, " SCALED UP")
    explore(src)
    explore(canvas)


# Update Plabel 1
def slide1(value):
    plabel1.configure(text=(int(value), "%"))


# Update Plabel 2
def slide2(value):
    plabel2.configure(text=(int(value), "%"))


# Update Plable 3
def slide3(value):
    plabel3.configure(text=round(value, 1))


# setting the theme /apperance
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# creating the main window
root = customtkinter.CTk()

# setting the title and size of the window
root.title("Image Editor")
root.geometry("650x750")

# frame one
frame1 = customtkinter.CTkFrame(master=root, width=550, height=650)
frame1.pack(pady=10, padx=10)
frame1.pack_propagate(0)


# title lable 0
label = customtkinter.CTkLabel(frame1, text="Image Editor", font=("Arial", 25))
label.pack(padx=30, pady=20)

# image selectinng button
button1 = customtkinter.CTkButton(frame1, text="Select Image", command=open_img)
button1.pack(pady=10, padx=10)


# frame two
frame2 = customtkinter.CTkFrame(master=frame1, width=550, height=120)
frame2.pack(pady=10, padx=10)
frame2.pack_propagate(0)

# title lable 1
label1 = customtkinter.CTkLabel(frame2, text="Scale Down", font=("Arial", 15))
label1.pack(padx=30, pady=5)

# slider 1
slider1 = customtkinter.CTkSlider(
    frame2, from_=0, to=100, number_of_steps=10, command=slide1
)
slider1.set(0)

# Percentage lable 1
plabel1 = customtkinter.CTkLabel(frame2, text=slider1.get(), font=("Arial", 15))


# Apply button
global img
abutton1 = customtkinter.CTkButton(
    frame2, text="Apply", command=lambda: myScalingDown(img, int(slider1.get()))
)

# frame three
frame3 = customtkinter.CTkFrame(master=frame1, width=550, height=120)
frame3.pack(pady=10, padx=10)
frame3.pack_propagate(0)

# title lable 2
label2 = customtkinter.CTkLabel(frame3, text="Scale Up(Percentage)", font=("Arial", 15))
label2.pack(padx=30, pady=5)

# slider 2
slider2 = customtkinter.CTkSlider(
    frame3, from_=0, to=100, number_of_steps=10, command=slide2
)
slider2.set(0)

# Percentage lable 2
plabel2 = customtkinter.CTkLabel(frame3, text=slider1.get(), font=("Arial", 15))


# Apply button
abutton2 = customtkinter.CTkButton(
    frame3, text="Apply", command=lambda: myScalingUpP(img, int(slider2.get()))
)

# frame four
frame4 = customtkinter.CTkFrame(master=frame1, width=550, height=120)
frame4.pack(pady=10, padx=10)
frame4.pack_propagate(0)

# title lable 3
label3 = customtkinter.CTkLabel(frame4, text="Scale Up(Times)", font=("Arial", 15))
label3.pack(padx=30, pady=5)

## slider 3
slider3 = customtkinter.CTkSlider(
    frame4, from_=0, to=10, number_of_steps=100, command=slide3
)
slider3.set(0)

# Percentage lable 3
plabel3 = customtkinter.CTkLabel(frame4, text=slider1.get(), font=("Arial", 15))


# Apply button
abutton3 = customtkinter.CTkButton(
    frame4, text="Apply", command=lambda: myScalingUpTimes(img, round(slider3.get(), 1))
)


root.mainloop()
