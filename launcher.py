import sys
import os.path
import os
import urllib.request
import zipfile
import shutil
import basegame
# VERSION 0.5.0
# UNDER GPL V3 LICENSE
# Check my github: https://github.com/de-odex/Attack
version = 500
alpha = 0
beta = 0


# functions
def end():
	input("Press Enter to continue...")
	sys.exit()


def enter():
	input("Press Enter to continue...")


def clr():
	os.system('cls')


def readver(var, line):
	try:
		readfile = open("latest.txt", "r")
		data = readfile.readlines()
		var = int(data[line])
		readfile.close()
	except IOError:
		print("!")
	except ValueError:
		print("?")
		open("latest.txt", "w")
	except:
		print(";")
	return var


def rungame():
	basegame.main()


def update():
	print("Updating...")
	full_path_to_zip = "C:\\Attack\\temp\\Attack_update.zip"
	destination_path = "C:\\Attack\\update"
	source_zip = zipfile.ZipFile(full_path_to_zip, 'r')
	for name in source_zip.namelist():
		if name.find('.py') != -1:
			source_zip.extract(name, destination_path)
			source_zip.close()
	shutil.copy('C:\\Attack\\update\\Attack-master\\basegame.py', 'C:\\Attack\\')
	shutil.rmtree('C:\\Attack\\temp\\')
	shutil.rmtree('C:\\Attack\\update\\')
	clr()
	print("Updated!")
	runlatest()


def runlatest():
	shutil.rmtree('C:\\Attack\\temp\\')
	shutil.rmtree('C:\\Attack\\update\\')
	rungame()


def check():
	print("Checking for updates...")
	latest = 0
	os.mkdir("C:\\Attack\\temp\\")
	os.mkdir("C:\\Attack\\update\\")
	try:
		urllib.request.urlretrieve('https://github.com/de-odex/Attack/archive/master.zip', 'C:\\Attack\\temp\\Attack_update.zip')
	except:
		print("No Internet.")
	full_path_to_zip = "C:\\Attack\\temp\\Attack_update.zip"
	destination_path = "C:\\Attack\\update"
	source_zip = zipfile.ZipFile(full_path_to_zip, 'r')
	for name in source_zip.namelist():
		if name.find('latest.txt') != -1:
			source_zip.extract(name, destination_path)
			source_zip.close()
	shutil.copy('C:\\Attack\\update\\Attack-master\\latest.txt', 'C:\\Attack\\')
	latest = readver(latest, 0)
	if version < latest:
		upd8 = input("Do you want to update? (1/0): ")
		try:
			upd8 = int(upd8)
		except ValueError:
			clr()
			print("Number please!")
			upd8 = 1
		if upd8 == 1:
			clr()
			update()
		else:
			enter()
			clr()
	else:
		print("No updates detected.")
		runlatest()


check()
