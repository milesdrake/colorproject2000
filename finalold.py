#this is my final project.
#currently it takes all of one range of color from an image and turns it dark red. Right now its not that exciting but I am looking to add more customization.
#perhaps in future versions the user will be able to enter their own image, the range of colors to replace, and the color to replace it with.
#also, an option to save the final image will be added

from graphics import *

picture = str(input("Which picture do you want? "))

red = int(input("red: "))
green = int(input("green: "))
blue = int(input("blue: "))

color1 = input("What color to change to? ")

win = GraphWin(width = 1000, height = 800)
win.setCoords(0, 0, 1000, 800)

image1 = Image(Point(500,400),picture + ".gif")

image1.draw(win)

column = -1
row = -1

for i in range(image1.getWidth()-1):
	row = -1
	column = column + 1
	for i in range(image1.getHeight()-1):
		row = row + 1
		color = image1.getPixel(int(column),int(row))
		print(color)

		if color[0] >red and color[1] < green and color[2] <blue:
			image1.setPixel(int(column),int(row),color1)


point1 = win.getMouse()