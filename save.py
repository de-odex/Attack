import os.path
def read1(var, line):
	try:
		readfile = open("save.txt", "r")
		data = readfile.readlines()
		var = int(data[line])
		readfile.close()
	except IOError:
		print("No value.")
	except ValueError:
		print("Error reading save. Restarting...")
	
	return var


def save(var):
	try:
		readfile = open("save.txt", "a")
		readfile.write(str(var) + "\n")
		readfile.close()
	except IOError:
		print("Unable to save.")
		
def save1(var):
	try:
		PATH = "./save.txt"
		if os.path.isfile(PATH):
			readfile = open("save.txt", "w")
			readfile.write(str(var) + "\n")
			readfile.close()
		else:
			readfile = open("save.txt", "a")
			readfile.write(str(var) + "\n")
			readfile.close()
	except IOError:
		print("Unable to save.")
