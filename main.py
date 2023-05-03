import AcronymDictionary

Choice = -1

while Choice != "0":

	Choice = input("Please select 1 to lookup an Acronym\n"
				   "2 to add a new Acromyn\n"
				   "or 0 (zero) to exit")

	if Choice == "1":

		key = input("What Acyonym would you like to enter? ")

		for key, value in AcronymDictionary.AcronymDict.items():
			print("Acronym: " + str(key), "Meaning: " + str(value))

	elif Choice == "2":
		

	elif Choice == "0":
		exit();


