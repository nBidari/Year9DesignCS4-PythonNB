

a = 0
b = 0

x = 0
y = 0
sevenSaid = False



while sevenSaid == False:
	instruction = input("")

	x = 0
	y = 0

	if instruction[0] == "7":
		sevenSaid = True
	else:


		if instruction[0] == "1":
			x = instruction[4]
		elif instruction[0] == "2":
			print(x)
		else:

			

			elif instruction[0] == "3":
				x = x+y
			elif instruction[0] == "4":
				x = x*y
			elif instruction[0] == "5":
				x = x-y
			elif instruction[0] == "6":
				x = x/y


		if instruction [2] == "A":
			a = x
			b = y
		else:
			a = y
			b = x

	printer = [a,b,x,y]

	print(printer)