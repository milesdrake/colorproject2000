from graphics import *
import os
#imports from the graphics library and the os module.
#the graphics library makes the window and the image on screen possible
#the os module helps us display the names of all the images in the directory

def getlist():
	directory = os.listdir()
	for i in range(len(directory)):
		item = directory[i]
		if str(item[len(item)-1:]) == "f":
			print(item[0:len(item)-4])
#this chunk of code goes through the folder that this document is in and displays the name of all of the things that have the extension ".gif"

getlist()
#this runs the function defined above. The reason its written as a function is because it is necessary to have functions for this project.

picture = str(input("Which picture do you want? "))
#asks the user which picture they want, they type in the name of the image they want from the list that has just been displayed

win = GraphWin(width = 1000, height = 800)
win.setCoords(0, 0, 1000, 800)
#draws the window on the screen

message = Text(Point(500,750),"Click a color")
message.setSize(30)
message.draw(win)
#tells the user to click on whichever color they want changed

image1 = Image(Point(500,400),picture + ".gif")
image1.draw(win)
#draws the image chosen by the user in the middle of the window

widthim = image1.getWidth()
heightim = image1.getHeight()
#finds the width and the height of the image

xdiff = 500 - widthim/2
ydiff = 400 - heightim/2
#finds the distance from the side and the top of the image to the side and the top of the window

point = win.getMouse()
win.close()
#finds the point in the WINDOW where the user clicks

ximage = point.getX() - xdiff
yimage = point.getY() - ydiff
#translates the point in the window to a point on the IMAGE using the data gathered about the distance of the image to the edge of the window
#for some reason I think that this is not very accurate. It might have to do with when the image runs up against the edge of the window

colorpoint = image1.getPixel(int(ximage),int(yimage))
print(colorpoint)
#finds the color of the image at the point that was just found

above = (int(input("How big of a range? (0 - 255):")))/2
#the range of colors that are to be changed. if only a very specific color pixel was changed it would be super boring

rpoint1 = (colorpoint[0] - above)
rpoint2 = (colorpoint[0] + above)
#makes the range of the red part of RGB

gpoint1 = (colorpoint[1] - above)
gpoint2 = (colorpoint[1] + above)
#makes the range of the green part of RGB

bpoint1 = (colorpoint[2] - above)
bpoint2 = (colorpoint[2] + above)
#makes the range of the blue part of RGB

color1 = input("What color to change to? (type the name of a color like 'red'): ")
#allows the user to choose what color they want to change specific parts of the image to

win = GraphWin(width = 1000, height = 800)
win.setCoords(0, 0, 1000, 800)
#redraws the window

image1.draw(win)
#redraws the image

column = -1
row = -1
#sets some variables to negative one for ease of use in the for loops

for i in range(widthim-1):
	row = -1
	column = column + 1
	for i in range(heightim-1):
		row = row + 1
		color = image1.getPixel(int(column),int(row))
		if rpoint1 < color[0] < rpoint2 and gpoint1 < color[1] < gpoint2 and bpoint1 < color[2] < bpoint2:
			image1.setPixel(int(column),int(row),color1)
#goes through every pixel in the entire image. If the rgb values of that pixel are within the ranges specified, the pixel will be changed to the color entered by the user earlier

imagename = str(color1) + picture + ".gif"
image1.save(imagename)
#saves the image under a temporary name of the color and the and name of the starting image
#the reason it saves before it asks the user whether or not they want to save it is because its too hard
#to try to save it after the window has been closed already

point1 = win.getMouse()
win.close()
#close the window when the user clicks on the image

value = 1
while value == 1:
	save = str(input("Would you like to save your image? (yes or no): "))

	if save == "yes":
		name = input("Enter a name for your image: ")
		os.rename(imagename,name + ".gif")
		value = 0
		#keeps the file and renames it to whatever the user chooses 
	elif save == "no":
		os.remove(imagename)
		value = 0
		#deletes the image
	else:
		value = 1
		#sends us back to the question because a valid answer was not given

