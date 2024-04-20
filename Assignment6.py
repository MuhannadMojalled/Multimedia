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
    button14.pack(pady=10)
    button5.pack(pady=10)
    button6.pack(pady=10)
    button7.pack(pady=10)
    button8.pack(pady=10)
    textf.pack(pady=10)
    button15.pack(pady=10)
    button11.pack(pady=10)


# remove the image
def remove_image():
    try:
        panel.pack_forget()
        button3.pack_forget()
        button12.pack_forget()
        button13.pack_forget()
        button4.pack_forget()
        button14.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        button11.pack_forget()
        button15.pack_forget()
        textf.pack_forget()
    except:
        return


# simple average
def simpleAverage():
    global source
    height = int(getHeight(source))
    width = int(getHeight(source))
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 2):
        for v in range(1, height - 2):
            sum = 0
            for j in range(-1, 2):
                for i in range(-1, 2):
                    p = getPixel(source, u + i, v + j)
                    sum += getRed(p) + getBlue(p) + getGreen(p)
            q = int(sum / 9)
            color = makeColor(q, q, q)
            setColor(getPixel(blank, u, v), color)

    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Weighted Average
def weightedAverage():
    global source
    height = getHeight(source)
    width = getWidth(source)
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 1):
        for v in range(1, height - 1):
            # Apply weights to neighboring pixel intensities
            intensity = (
                0.5 * getRed(getPixel(source, u - 1, v - 1))
                + 1.0 * getRed(getPixel(source, u, v - 1))
                + 0.5 * getRed(getPixel(source, u + 1, v - 1))
                + 1.0 * getRed(getPixel(source, u - 1, v))
                + 2.0 * getRed(getPixel(source, u, v))
                + 1.0 * getRed(getPixel(source, u + 1, v))
                + 0.5 * getRed(getPixel(source, u - 1, v + 1))
                + 1.0 * getRed(getPixel(source, u, v + 1))
                + 0.5 * getRed(getPixel(source, u + 1, v + 1))
            )

            # Compute the weighted average intensity
            new_intensity = int(intensity / 10)  # Total weight is 10

            color = makeColor(new_intensity, new_intensity, new_intensity)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Min Filter
def minFilter():
    global source
    height = int(getHeight(source))
    width = int(getHeight(source))
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 2):
        for v in range(1, height - 2):
            sum = []
            for j in range(-1, 2):
                for i in range(-1, 2):
                    p = getPixel(source, u + i, v + j)
                    sumc = getRed(p) + getBlue(p) + getGreen(p)
                    sum.append(sumc)
            q = int(min(sum))
            color = makeColor(q, q, q)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# max Filter
def maxFilter():
    global source
    height = int(getHeight(source))
    width = int(getHeight(source))
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 2):
        for v in range(1, height - 2):
            sum = []
            for j in range(-1, 2):
                for i in range(-1, 2):
                    p = getPixel(source, u + i, v + j)
                    sumc = getRed(p) + getBlue(p) + getGreen(p)
                    sum.append(sumc)
            q = int(max(sum))
            color = makeColor(q, q, q)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# Vertical Reflection Left to Right
def medianFilter():
    global source
    height = int(getHeight(source))
    width = int(getHeight(source))
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 2):
        for v in range(1, height - 2):
            sum = []
            for j in range(-1, 2):
                for i in range(-1, 2):
                    p = getPixel(source, u + i, v + j)
                    sumc = getRed(p) + getBlue(p) + getGreen(p)
                    sum.append(sumc)
            sum.sort()
            c = sum[int(len(sum) / 2)]
            q = int(c)
            color = makeColor(q, q, q)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# laplacian Filter
def laplacianFilter():
    global source
    height = getHeight(source)
    width = getWidth(source)
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 1):
        for v in range(1, height - 1):
            sum = 0
            for j in range(-1, 2):
                for i in range(-1, 2):
                    p = getPixel(source, u + i, v + j)
                    intensity = (
                        getRed(p) + getBlue(p) + getGreen(p)
                    ) / 3  # Convert to grayscale
                    sum += intensity
            new_intensity = int(sum / 9)  # Average intensity
            color = makeColor(new_intensity, new_intensity, new_intensity)
            setColor(getPixel(blank, u, v), color)

    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# sobel Filter
def sobelFilter():
    global source
    height = getHeight(source)
    width = getWidth(source)
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 1):
        for v in range(1, height - 1):
            # Calculate horizontal gradient
            gx = (
                -1 * getRed(getPixel(source, u - 1, v - 1))
                + 0 * getRed(getPixel(source, u, v - 1))
                + 1 * getRed(getPixel(source, u + 1, v - 1))
                + -2 * getRed(getPixel(source, u - 1, v))
                + 0 * getRed(getPixel(source, u, v))
                + 2 * getRed(getPixel(source, u + 1, v))
                + -1 * getRed(getPixel(source, u - 1, v + 1))
                + 0 * getRed(getPixel(source, u, v + 1))
                + 1 * getRed(getPixel(source, u + 1, v + 1))
            )

            # Calculate vertical gradient
            gy = (
                -1 * getRed(getPixel(source, u - 1, v - 1))
                + -2 * getRed(getPixel(source, u, v - 1))
                + -1 * getRed(getPixel(source, u + 1, v - 1))
                + 0 * getRed(getPixel(source, u - 1, v))
                + 0 * getRed(getPixel(source, u, v))
                + 0 * getRed(getPixel(source, u + 1, v))
                + 1 * getRed(getPixel(source, u - 1, v + 1))
                + 2 * getRed(getPixel(source, u, v + 1))
                + 1 * getRed(getPixel(source, u + 1, v + 1))
            )

            # Compute magnitude of gradient
            magnitude = int((gx**2 + gy**2) ** 0.5)

            color = makeColor(magnitude, magnitude, magnitude)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# prewitt Filter
def prewittFilter():
    global source
    height = getHeight(source)
    width = getWidth(source)
    blank = makeEmptyPicture(width, height)
    for u in range(1, width - 1):
        for v in range(1, height - 1):
            # Calculate horizontal gradient
            gx = (
                -1 * getRed(getPixel(source, u - 1, v - 1))
                + 0 * getRed(getPixel(source, u, v - 1))
                + 1 * getRed(getPixel(source, u + 1, v - 1))
                + -1 * getRed(getPixel(source, u - 1, v + 1))
                + 0 * getRed(getPixel(source, u, v + 1))
                + 1 * getRed(getPixel(source, u + 1, v + 1))
            )

            # Calculate vertical gradient
            gy = (
                -1 * getRed(getPixel(source, u - 1, v - 1))
                + -1 * getRed(getPixel(source, u - 1, v))
                + -1 * getRed(getPixel(source, u - 1, v + 1))
                + 1 * getRed(getPixel(source, u + 1, v - 1))
                + 1 * getRed(getPixel(source, u + 1, v))
                + 1 * getRed(getPixel(source, u + 1, v + 1))
            )

            # Compute magnitude of gradient
            magnitude = int((gx**2 + gy**2) ** 0.5)

            color = makeColor(magnitude, magnitude, magnitude)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# robert Filter
def robertFilter():
    global source
    height = getHeight(source)
    width = getWidth(source)
    blank = makeEmptyPicture(width, height)
    for u in range(0, width - 1):
        for v in range(0, height - 1):
            # Calculate horizontal gradient
            gx = getRed(getPixel(source, u, v)) - getRed(getPixel(source, u + 1, v + 1))

            # Calculate vertical gradient
            gy = getRed(getPixel(source, u + 1, v)) - getRed(getPixel(source, u, v + 1))

            # Compute magnitude of gradient
            magnitude = int((gx**2 + gy**2) ** 0.5)

            color = makeColor(magnitude, magnitude, magnitude)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
    imgN = Image.open("./newImage.png")
    tk_img = customtkinter.CTkImage(imgN, size=(450, 450))
    panel.configure(image=tk_img)


# generalized avg filter
def generlizedAverage():
    global source
    height = getHeight(source)
    width = getWidth(source)
    blank = makeEmptyPicture(width, height)
    filter_size = int(textf.get())

    half_size = filter_size // 2

    for u in range(half_size, width - half_size):
        for v in range(half_size, height - half_size):
            sum_red = 0
            sum_green = 0
            sum_blue = 0

            for i in range(-half_size, half_size + 1):
                for j in range(-half_size, half_size + 1):
                    pixel = getPixel(source, u + i, v + j)
                    sum_red += getRed(pixel)
                    sum_green += getGreen(pixel)
                    sum_blue += getBlue(pixel)

            # Compute average color values
            avg_red = int(sum_red / (filter_size**2))
            avg_green = int(sum_green / (filter_size**2))
            avg_blue = int(sum_blue / (filter_size**2))

            color = makeColor(avg_red, avg_green, avg_blue)
            setColor(getPixel(blank, u, v), color)
    writePictureTo(blank, "./newImage.png")
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
button1 = customtkinter.CTkButton(frame0, text="Select Image", command=open_img)
button1.pack(side="left", anchor="e", expand=True, pady=10, padx=10)

# image removing button
button2 = customtkinter.CTkButton(frame0, text="Remove Image", command=remove_image)
button2.pack(side="right", anchor="w", expand=True, pady=10)

# simpleAverage button
button3 = customtkinter.CTkButton(frame2, text="Simple Average", command=simpleAverage)

# weighted Average button
button12 = customtkinter.CTkButton(
    frame2, text="Weighted Average", command=weightedAverage
)

# medianFilter button
button13 = customtkinter.CTkButton(frame2, text="Median Filter", command=medianFilter)

# minFilter button
button4 = customtkinter.CTkButton(frame2, text="Min Filter", command=minFilter)

# maxFilter button
button14 = customtkinter.CTkButton(frame2, text="Max Filter", command=maxFilter)


# laplacian Filter button
button5 = customtkinter.CTkButton(
    frame2, text="Laplacian Filter", command=laplacianFilter
)

# sobel Filter button
button6 = customtkinter.CTkButton(frame2, text="Sobel Filter", command=sobelFilter)

# prewitt Filter button
button7 = customtkinter.CTkButton(frame2, text="Prewitt Filter", command=prewittFilter)

# robert Filter button
button8 = customtkinter.CTkButton(frame2, text="Robert’s Filter", command=robertFilter)


# the text feild
textf = customtkinter.CTkEntry(frame2, placeholder_text="Filter Size")

# generalized avg button
button15 = customtkinter.CTkButton(
    frame2, text="generlized Average", command=generlizedAverage
)

# rest image button
button11 = customtkinter.CTkButton(frame2, text="reset image", command=resetImage)


root.mainloop()
