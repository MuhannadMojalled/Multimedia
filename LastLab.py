def makeRectMovie1(directory ):
	for num in range (1 ,80): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,200)
		addRectFilled(canvas ,num * 6, num * 3, 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie

def makeRectMovie2(directory ):
	for num in range (1 ,30): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,200)
		addRectFilled(canvas ,300-(num*10) ,200-(num*7), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie


def makeRectMovie3(directory ):
	for num in range (1 ,30): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,200)
		addRectFilled(canvas ,300-(num*10), (num*5), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie

def makeRectMovie4(directory ):
	for num in range (1 ,30): #29 frames (1 to 29)
		canvas = makeEmptyPicture (300 ,200)
		addRectFilled(canvas ,(num*10), 200-(num*7), 50,50, red)
		# convert the number to a string
		numStr=str(num)
		if num < 10:
			writePictureTo(canvas ,directory+"\\ frame0"+numStr+".jpg")
		if num >= 10:
			writePictureTo(canvas ,directory+"\\ frame"+numStr+".jpg")
	movie = makeMovieFromInitialFile(directory+"\\ frame00.jpg");
	return movie


rectM = makeRectMovie1("C:\\Users\\muasu\\Desktop\\movie") 
playMovie(rectM) 
rectM = makeRectMovie2("C:\\Users\\muasu\\Desktop\\movie") 
playMovie(rectM) 
rectM = makeRectMovie3("C:\\Users\\muasu\\Desktop\\movie") 
playMovie(rectM) 
rectM = makeRectMovie4("C:\\Users\\muasu\\Desktop\\movie") 
playMovie(rectM) 
