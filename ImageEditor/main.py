from tkinter import *
import customtkinter
from PIL import ImageTk, Image, ImageEnhance
from tkinter import filedialog
from jes4py import *


# Find the image
def openfn():
    filename = filedialog.askopenfilename(title="Open")
    return filename


# open the image
def open_img():
    global filename, img, tk_img, panel, source
    filename = openfn()
    img = Image.open(filename)
    tk_img = customtkinter.CTkImage(img, size=(450, 450))
    panel = customtkinter.CTkLabel(frame1, text="", image=tk_img)
    source = makePicture(filename)
    panel.pack()
    button3.pack(pady=10)
    button12.pack(pady=10)
    button13.pack(pady=10)
    button4.pack(pady=10)
    button5.pack(pady=10)
    button6.pack(pady=10)
    button7.pack(pady=10)
    button8.pack(pady=10)
    button9.pack(pady=10)
    button10.pack(pady=10)
    button11.pack(pady=10)


# remove the image
def remove_image():
    try:
        panel.pack_forget()
        button3.pack_forget()
        button12.pack_forget()
        button13.pack_forget()
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        button9.pack_forget()
        button10.pack_forget()
        button11.pack_forget()
    except:
        return


# Horizontal Bottom to Top Reflection
def reflectionHBtoT():
    global source
    mirrorPoint = int(getHeight(source) / 2)
    height = int(getHeight(source))

    for x in range(0, getWidth(source)):
        for y in range(0, mirrorPoint):
            topPixel = getPixel(source, x, y)
            bottomPixel = getPixel(source, x, height - y - 1)
            color = getColor(bottomPixel)
            setColor(topPixel, color)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Horizontal Top to Bottom Reflection
def reflectionHTtoB():
    global source
    mirrorPoint = int(getHeight(source) / 2)
    height = int(getHeight(source))

    for x in range(0, getWidth(source)):
        for y in range(0, mirrorPoint):
            topPixel = getPixel(source, x, y)
            bottomPixel = getPixel(source, x, height - y - 1)
            color = getColor(topPixel)
            setColor(bottomPixel, color)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Vertical Reflection Right to Left
def reflectionVRtoL():
    global source
    mirrorPoint = int(getWidth(source) / 2)
    width = getWidth(source)

    for y in range(0, getHeight(source)):
        for x in range(0, mirrorPoint):
            leftPixel = getPixel(source, x, y)
            rightPixel = getPixel(source, width - x - 1, y)
            color = getColor(rightPixel)
            setColor(leftPixel, color)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Vertical Reflection Left to Right
def reflectionVLtoR():
    global source
    mirrorPoint = int(getWidth(source) / 2)
    width = getWidth(source)

    for y in range(0, getHeight(source)):
        for x in range(0, mirrorPoint):
            leftPixel = getPixel(source, x, y)
            rightPixel = getPixel(source, width - x - 1, y)
            color = getColor(leftPixel)
            setColor(rightPixel, color)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Reflection D1 bottom to top
def reflictionD1BtoT():
    global source

    for x in range(getWidth(source)):
        for y in range(x, getHeight(source)):
            sourceC = getPixel(source, x, y)
            target = getPixel(source, y, x)
            color = getColor(sourceC)
            setColor(target, color)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Reflection D1 top to bottom
def reflictionD1TtoB():
    global source
    height = int(getHeight(source))
    width = int(getWidth(source))

    for x in range(getWidth(source)):
        for y in range(x, getHeight(source)):
            sourceC = getPixel(source, y, x)
            target = getPixel(source, x, y)
            color = getColor(sourceC)
            setColor(target, color)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Reflection D2 bottom to top
def reflictionD2BtoT():
    global source
    height = int(getHeight(source))
    width = int(getWidth(source))

    for y in range(height):
        for x in range(width - y):
            pixel1 = getPixel(source, x, y)
            pixel2 = getPixel(source, width - y - 1, height - x - 1)
            color2 = getColor(pixel2)
            setColor(pixel1, color2)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Reflection D2 top to bottom
def reflictionD2TtoB():
    global source
    height = int(getHeight(source))
    width = int(getWidth(source))

    for y in range(height):
        for x in range(width - y):
            pixel1 = getPixel(source, x, y)
            pixel2 = getPixel(source, width - y - 1, height - x - 1)
            color1 = getColor(pixel1)
            setColor(pixel2, color1)

    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Rotate Left
def rotateL():
    global source
    targetX = 0
    width = getWidth(source)
    height = getHeight(source)
    canvas = makeEmptyPicture(width * 1.5, height * 1.5)
    for sourceX in range(0, width):
        targetY = 0
        for sourceY in range(0, height):
            color = getColor(getPixel(source, sourceX, sourceY))
            setColor(getPixel(canvas, targetY, width - (sourceX - 1)), color)
            targetY = targetY + 1
        targetX = targetX + 1
    source = canvas
    writePictureTo(canvas, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Rotate Right
def rotateR():
    global source
    width = getWidth(source)
    height = getHeight(source)
    canvas = makeEmptyPicture(width * 1.5, height * 1.5)
    for sourceX in range(0, width):
        for sourceY in range(0, height):
            color = getColor(getPixel(source, sourceX, sourceY))
            setColor(getPixel(canvas, height - sourceY - 1, sourceX), color)
    source = canvas
    writePictureTo(canvas, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Reset image
def resetImage():
    global source, filename
    source = makePicture(filename)
    writePictureTo(source, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# setting the theme /apperance
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# creating the main window
root = customtkinter.CTk()

# setting the title and size of the window
root.title("Image Editor")
root.geometry("1000x850")

# frame zero
frame0 = customtkinter.CTkFrame(master=root, width=960, height=100)
frame0.pack(pady=10, padx=10)
frame0.pack_propagate(0)

# frame one
frame1 = customtkinter.CTkFrame(master=root, width=680, height=600)
frame1.pack(side="left", anchor="ne", expand=True, pady=10, padx=10)
frame1.pack_propagate(0)

# frame two
frame2 = customtkinter.CTkFrame(master=root, width=280, height=600)
frame2.pack(side="right", anchor="nw", expand=True, pady=10, padx=10)
frame2.pack_propagate(0)

# title lable 0
label = customtkinter.CTkLabel(frame0, text="Image Editor", font=("Arial", 25))
label.pack(padx=30, pady=10)

# title lable 1
label = customtkinter.CTkLabel(frame1, text="Image", font=("Arial", 25))
label.pack(padx=30, pady=10)

# title lable 2
label = customtkinter.CTkLabel(frame2, text="Controls", font=("Arial", 25))
label.pack(padx=30, pady=10)

# image selectinng button
button1 = customtkinter.CTkButton(frame0, text="select Image", command=open_img)
button1.pack(side="left", anchor="e", expand=True, pady=10, padx=10)

# image removing button
button2 = customtkinter.CTkButton(frame0, text="Remove Image", command=remove_image)
button2.pack(side="right", anchor="w", expand=True, pady=10)

# Horizontal reflection Bottom to Top button
button3 = customtkinter.CTkButton(
    frame2, text="H Reflection B to T", command=reflectionHBtoT
)

# Horizontal reflection Top to Bottom button
button12 = customtkinter.CTkButton(
    frame2, text="H Reflections T to B", command=reflectionHTtoB
)

# Vertical reflection Right to Left button
button13 = customtkinter.CTkButton(
    frame2, text="V Reflection L to R", command=reflectionVLtoR
)

# Vertical reflection Left to Right button
button4 = customtkinter.CTkButton(
    frame2, text="V Reflection R to L", command=reflectionVRtoL
)

# Diagonal D1 bottom to top refliction button
button5 = customtkinter.CTkButton(
    frame2, text="D1 Reflection B to T", command=reflictionD1BtoT
)

# Diagonal D1 top to bottom refliction button
button6 = customtkinter.CTkButton(
    frame2, text="D1 Reflection T to B", command=reflictionD1TtoB
)

# Diagonal D2 bottom to top refliction button
button7 = customtkinter.CTkButton(
    frame2, text="D2 Reflection B to T", command=reflictionD2BtoT
)

# Diagonal D2 top to bottom refliction button
button8 = customtkinter.CTkButton(
    frame2, text="D2 Reflection T to B", command=reflictionD2TtoB
)

# left rotation button
button9 = customtkinter.CTkButton(frame2, text="Rotate Left", command=rotateL)

# right rotation button
button10 = customtkinter.CTkButton(frame2, text="Rotate right", command=rotateR)

# rest image button
button11 = customtkinter.CTkButton(frame2, text="reset image", command=resetImage)


root.mainloop()
