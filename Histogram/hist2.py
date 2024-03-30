from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter
from PIL import Image, ImageTk
import numpy as np


def plot_histograms(image):
    # Calculate histograms for each channel R,G and B
    hist_red = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_blue = cv2.calcHist([image], [2], None, [256], [0, 256])

    # Plot histograms
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(hist_red, color="red", label="Red")
    ax.plot(hist_green, color="green", label="Green")
    ax.plot(hist_blue, color="blue", label="Blue")
    ax.set_title("Histograms for Red, Green, and Blue Channels")
    ax.set_xlabel("Pixel Intensity")
    ax.set_ylabel("Frequency")
    ax.legend()

    return fig


def openfn():
    # Let user selects the image
    global filename
    filename = filedialog.askopenfilename(title="Open")


def hist_equalize_color(image):
    b, g, r = cv2.split(image)

    # Initialize the histogram array
    histogram = np.zeros(256)

    # Iterate over each pixel in the image and update the histogram
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[r[i, j]] += 1
            histogram[g[i, j]] += 1
            histogram[b[i, j]] += 1

    # Normalize the histogram by dividing each bin by 3
    histogram /= 3

    # Calculate the cumulative distribution function (CDF) from the histogram
    cdf = histogram.cumsum()

    # Normalize the CDF
    cdf_normalized = ((cdf - cdf.min()) * 255) / (cdf.max() - cdf.min())

    # Map the pixel intensities of the original image to their corresponding equalized values
    equalized_image = cdf_normalized[image]

    # Convert the data type of the equalized image to uint8
    equalized_image = equalized_image.astype(np.uint8)

    return equalized_image


# Function to display histograms
def display_histogram():
    # Load the image
    global filename
    image = cv2.imread(filename)

    # Plot histograms and display inside the GUI
    fig = plot_histograms(image)

    # Convert the plot to an image and save it
    plt.tight_layout()
    plt.savefig("histogram.png")
    plt.close()

    # Load the saved image
    hist_image = Image.open("histogram.png")
    hist_image = customtkinter.CTkImage(hist_image, size=(450, 250))

    # Display the image in Tkinter window
    label_histogram.configure(image=hist_image)
    label_histogram.image = hist_image
    labelhist.pack(pady=10)
    label_histogram.pack(pady=5)

    # Plot histograms and display inside the GUI
    equalized_image = hist_equalize_color(image)
    fig = plot_histograms(equalized_image)

    # Convert the plot to an image and save it
    plt.tight_layout()
    plt.savefig("histogrameq.png")
    plt.close()

    # Load the saved image
    hist_imageeq = Image.open("histogrameq.png")
    hist_imageeq = customtkinter.CTkImage(hist_imageeq, size=(450, 250))

    # Display the image in Tkinter window
    label_histogrameq.configure(image=hist_imageeq)
    label_histogrameq.image = hist_imageeq
    labelhisteq.pack(pady=10)
    label_histogrameq.pack(pady=5)


def show_equalized_image():
    # Load the image
    global filename
    image = cv2.imread(filename)
    img = Image.open(filename)

    # Perform histogram equalization
    equalized_image = hist_equalize_color(image)

    # Convert image to RGB format for displaying in Tkinter
    equalized_image_rgb = cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB)

    # Convert image to PIL format
    img_equalized = Image.fromarray(equalized_image_rgb)
    img_equalized = customtkinter.CTkImage(img_equalized, size=(250, 250))

    # Display the image in Tkinter window
    label_equalized.configure(image=img_equalized)
    label_equalized.image = img_equalized

    # Pack the images and labels to the GUI
    img = customtkinter.CTkImage(img, size=(250, 250))
    og_img.configure(image=img)
    labelOg.pack(pady=5)
    og_img.pack(pady=5)
    labelEq.pack(pady=5)
    label_equalized.pack(pady=5)


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
frame1 = customtkinter.CTkFrame(master=root, width=680, height=630)
frame1.pack(side="left", anchor="ne", expand=True, pady=10, padx=10)
frame1.pack_propagate(0)

# frame two
frame2 = customtkinter.CTkFrame(master=root, width=280, height=630)
frame2.pack(side="right", anchor="nw", expand=True, pady=10, padx=10)
frame2.pack_propagate(0)

# main title label
label = customtkinter.CTkLabel(frame0, text="Image Histogram", font=("Arial", 25))
label.pack(padx=30, pady=10)

# Button to select image
btn_select = customtkinter.CTkButton(
    frame0,
    text="Select Image",
    command=lambda: (
        openfn(),
        show_equalized_image(),
        display_histogram(),
    ),
)
btn_select.pack(side="left", anchor="center", expand=True, pady=10)

# original image title
labelOg = customtkinter.CTkLabel(frame2, text="Original Image", font=("Arial", 20))

# Label to display the original image
og_img = customtkinter.CTkLabel(frame2, text="")

# equalized image title
labelEq = customtkinter.CTkLabel(frame2, text="Equalized Image", font=("Arial", 20))

# Label to display the equalized image
label_equalized = customtkinter.CTkLabel(frame2, text="")

# original histogram image label
label_histogram = customtkinter.CTkLabel(frame1, text="", font=("Arial", 20))

# original histogram title label
labelhist = customtkinter.CTkLabel(
    frame1, text="Original Histogram", font=("Arial", 20)
)

# Equalized histogram image label
label_histogrameq = customtkinter.CTkLabel(frame1, text="", font=("Arial", 20))

# equalized histogram title label
labelhisteq = customtkinter.CTkLabel(
    frame1, text="Equalized Histogram", font=("Arial", 20)
)

root.mainloop()
