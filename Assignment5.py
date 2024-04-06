from jes4py import *


#  Read from a new background and write into an old background
def qustion1():
    pict = makePicture("Picture11.png")
    bg = makePicture("Picture2.png")
    newBg = makePicture("Picture3.png")
    threshold = float(input("Please Enter The Threshold: "))

    for px in getPixels(pict):
        x = getX(px)
        y = getY(px)
        bgPx = getPixel(bg, x, y)
        pxcol = getColor(px)
        bgcol = getColor(bgPx)
        if distance(pxcol, bgcol) < threshold:
            newcol = getColor(getPixel(newBg, x, y))
            setColor(px, newcol)
    addText(
        pict,
        (int(getWidth(pict)) / 2) - 65,
        10,
        "from new background to old background",
        white,
    )
    explore(pict)


# Read from the foreground and write into the new background
def qustion2():
    foreground = makePicture("Picture11.png")
    bg = makePicture("Picture2.png")
    newBg = makePicture("Picture3.png")

    threshold = float(input("Please Enter The Threshold: "))
    for pixel in getPixels(foreground):
        x = getX(pixel)
        y = getY(pixel)
        ForeGroundPixel = getPixel(foreground, x, y)
        BackGroundPixel = getPixel(bg, x, y)
        ForeGroundColor = getColor(ForeGroundPixel)
        BackGroundColor = getColor(BackGroundPixel)
        new_bg_color = getColor(getPixel(newBg, x, y))
        if distance(ForeGroundColor, BackGroundColor) < threshold:
            setColor(ForeGroundPixel, new_bg_color)

        else:
            setColor(getPixel(newBg, x, y), ForeGroundColor)
    addText(
        foreground,
        (int(getWidth(foreground)) / 2) - 65,
        10,
        "from foreground to new background",
        white,
    )
    explore(foreground)


# Detect edges using the top left and bottom right pixel
def qustion3_A():
    og = makePicture("butterfly1.jpg")
    for x in range(1, getWidth(og) - 1):
        for y in range(1, getHeight(og) - 1):
            here = getPixel(og, x, y)
            top_left = getPixel(og, x - 1, y + 1)
            bottom_right = getPixel(og, x + 1, y - 1)

            hereL = (getRed(here) + getGreen(here) + getBlue(here)) / 3
            top_left_L = (getRed(top_left) + getGreen(top_left) + getBlue(top_left)) / 3
            bottom_right_L = (
                getRed(bottom_right) + getGreen(bottom_right) + getBlue(bottom_right)
            ) / 3

            if abs(hereL - top_left_L) > 5 and abs(hereL - bottom_right_L) > 5:
                setColor(here, black)
            else:
                setColor(here, white)
    addText(og, (int(getWidth(og)) / 2) - 75, 0, "TOP LEFT AND BOTTOM RIGHT", red)

    explore(og)


# Detect edges using left and right pixels
def qustion3_B():
    og = makePicture("butterfly1.jpg")
    for x in range(1, getWidth(og) - 1):
        for y in range(1, getHeight(og) - 1):
            here = getPixel(og, x, y)
            left = getPixel(og, x - 1, y)
            right = getPixel(og, x + 1, y)

            hereL = (getRed(here) + getGreen(here) + getBlue(here)) / 3
            left_L = (getRed(left) + getGreen(left) + getBlue(left)) / 3
            right_L = (getRed(right) + getGreen(right) + getBlue(right)) / 3

            if abs(hereL - left_L) > 5 and abs(hereL - right_L) > 5:
                setColor(here, black)
            else:
                setColor(here, white)
    addText(og, (int(getWidth(og)) / 2) - 65, 0, "LEFT AND RIGHT", red)
    explore(og)


# Detect edges using top and bottom pixels
def qustion3_C():
    og = makePicture("butterfly1.jpg")
    for x in range(1, getWidth(og) - 1):
        for y in range(1, getHeight(og) - 1):
            here = getPixel(og, x, y)
            top = getPixel(og, x, y + 1)
            bottom = getPixel(og, x, y - 1)

            hereL = (getRed(here) + getGreen(here) + getBlue(here)) / 3
            top_L = (getRed(top) + getGreen(top) + getBlue(top)) / 3
            bottom_L = (getRed(bottom) + getGreen(bottom) + getBlue(bottom)) / 3

            if abs(hereL - top_L) > 5 and abs(hereL - bottom_L) > 5:
                setColor(here, black)
            else:
                setColor(here, white)
    addText(og, (int(getWidth(og)) / 2) - 55, 0, "Top and Bottom", red)
    explore(og)


qustion3_A()
qustion3_B()
qustion3_C()
