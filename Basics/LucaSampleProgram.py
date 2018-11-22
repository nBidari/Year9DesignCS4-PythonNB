toxic = ["doo doo", "wee wee", "kaka", "swear", "bad", "Kanye is not comepletely garbage"]

sample = input("Enter Conversation Here: ")

def toxicityCalculator(phrase):

	for i in range(len(phrase)-1):

		for x in range(len(toxic)-1):
			if phrase[x:]


output = toxicityCalculator(sample)