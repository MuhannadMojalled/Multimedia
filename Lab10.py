def makeRectMovie1(directory ):
	for num in range (1 ,80): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,300)
		addRectFilled(canvas ,int(num * 3.1), int(num * 3.1), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie

def makeRectMovie2(directory ):
	for num in range (1 ,80): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,300)
		addRectFilled(canvas ,300-int(num*3.7) ,300-int(num*3.7), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie


def makeRectMovie3(directory ):
	for num in range (1 ,80): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,300)
		addRectFilled(canvas ,300-int(num*3.7), int(num*3.1), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie

def makeRectMovie4(directory ):
	for num in range (1 ,80): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,300)
		addRectFilled(canvas ,int(num*3.1), 300-int(num*3.7), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie


rectM = makeRectMovie4("C:\\Users\\muasu\\Desktop\\movie") 
playMovie(rectM) 

