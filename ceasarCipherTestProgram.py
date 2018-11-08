message = input("What is your message? ")
shift = input("What is your shift? ")
cipher = ""

message = list(message)

for i in range(len(message)-1):
	cipher = cipher + " " + str(chr(message[i]))

print(cipher)