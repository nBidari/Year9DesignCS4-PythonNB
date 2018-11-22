import tkinter as tk

#This example is the same cade of Demo2, but the code 
#has been optimized for better algorithm design. 

def mouseClicked(event):
	#Optimization 3: I changed the if statements to elif statements
	#this means that once one condition is satisfied the other conditions
	#don't have to be evaluated. 
	if (event.x > 100 and event.x < 200 and event.y > 100 and event.y < 200 ):
		canvas.config(bg = "blue")
	elif (event.x > 300 and event.x < 400 and event.y > 200 and event.y < 300 ):
		canvas.config(bg = "yellow")
	elif (event.x > 0 and event.x < 100 and event.y > 400 and event.y < 500 ):
		canvas.config(bg = "red")
	
def mouseEnter(event):
	print("Enter")


def mouseMove(event):
	#print("Moving")
	#print(event) #prints information about teh event that called method
	#print(event.x) #prints the x location of mouse on canvas
	#print(event.y) #prints the y location of mouse on canvas

	x = event.x
	y = event.y


	#print(x//100)
	#print(y//100)
	#Optimization 4:  We can reduce all the code in this section to three lines
	#We need to leverage 
	#	1) 2D Lists
	#	A two 2D list is a way to collect data of the same type in a row and column format
	list = [["A","B","C","D","E"],["F","G","H","I","J"],["K","L","M","N","O"],["P","Q","R","S","T"],["U","V","W","X","Y"]]
	#	The above list can be visualize as and we can image it in rows and columns
	#			 columns
	#	 	  0  1  2  3  4
	# 		0 A  B  C  D  E
	#  		1 F  G  H  I  J
	# rows	2 K  L  M  N  O
	#  		3 P  Q  R  S  T
	#  		4 U  V  W  X  Y
	#	
	#  Letter H is located in row 1 column 2 so we access it by writing 
	#  list[1][2]
	#
	#	2) Interger Division
	#		Integer divison is when we divide an leave off the decimals.  In python we indicate
	#		integer division using //
	#			
	#			Examples:
	#				11//2 = 5
	#				17//5 = 3
	#				9//10 = 0
	#
	#		If we integer divide the x and y position of the mouse by 100 we get the row and column index
	#		of the letter in the list
	#		
	#			Example:
	#				event.x = 234
	#				event.y = 122
	#				This puts us in L square location (2,1)
	#				234//100 = 2
	#				122//100 = 1
	#				by integer dividing by 100 we get the row and column
	row = y//100
	col = x//100
	print(list[row][col])
	
def mouseLeave(event):
	print("Leaving")

root = tk.Tk()

canvas = tk.Canvas(root, bg = "red", width = 500, height = 500)
canvas.pack()



#Optimization 1: We can use a loop to print out 
#the horizontal and vertical loops.  This gives us
#the ability to be creative by changing intx and 
#inty

#inc must be a factor of width 
incx = 100
incy = 100

for i in range(incx,500,incx):
	canvas.create_line(i,0,i,500)

#Vertical Lines
for i in range(incy,500,incy):
	canvas.create_line(0,i,500,i)


#Optimization 2: We can use two concepts here
#1. A loop to manage position of the letters.  I noticed that
#	there was a pattern for each line 50, 150, 250, 350, 450
#	I set the loop parameters so that it counted through those 
#	values and used them for the x position of the letters
#2. All characters are mapped to integer values.  This is 
#	standardized across all languages.  
#	To change a char to an int we use the ord function
#	ord('a') --> 97
#	To change an int to a char we use the chr function
#	chr(97) --> 'a'
#	This is called casting, which is the process of changing
#	one type to another. 
#	How can we use this? 
#	Since we know that there is a pattern in the letters being
#	displayed we can set up a counter using their decimal (int)
#	value, stated in the ASCII table. 
#	http://www.asciitable.com/
#	values ord("A") --> 65
#	values ord("F") --> 65 + 5
#	values ord("K") --> 65 + 10
#	values ord("P") --> 65 + 15
#	values ord("U") --> 65 + 20
#	We create a decValue to keep track of the decimal value
#	and we create a ctr value to move increase the decValue 
#	each time the loop runs.  

decValue = 65
ctr = 0
for i in range(50,500,100):
	canvas.create_text(i,50, text = chr(decValue + ctr))
	canvas.create_text(i,150, text = chr(decValue + 5 + ctr))
	canvas.create_text(i,250, text = chr(decValue + 10 + ctr))
	canvas.create_text(i,350, text = chr(decValue + 15 + ctr))
	canvas.create_text(i,450, text = chr(decValue + 20 + ctr))
	ctr = ctr + 1

#Because these are unique lines that patterning isn't as easy I left
#them unchanged
canvas.create_text(150,165, text = "clickable - B")
canvas.create_text(350,265, text = "clickable - Y")
canvas.create_text(50,465, text = "clickable - R")

canvas.bind("<Enter>",mouseEnter)
canvas.bind("<Motion>",mouseMove)
canvas.bind("<Leave>",mouseLeave)
canvas.bind("<Button-1>",mouseClicked)

root.mainloop()
