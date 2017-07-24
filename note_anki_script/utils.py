# To Do List
#	0 - set up tkinter for user inputs (complete)
# 	i - open both programs (complete)
#	ii - parse .txt (complete)
#	iii - input into anki deck
#	iv - move .txt file and close programs

# 0 - tkinter
from tkinter import *

class Tkinter(object):
	def __init__(self):
		self.root = None
		self.path_name_string = None
		self.deck_name_string = None
		self.card_type_int = None
		self.returns = None

	def firstLabel(self, root):
		# first label - path string
		(Label(root, bg='lightgreen', text="Copy and paste full path here please: ")).pack()
		# field for path name
		self.path_name_string = StringVar()
		Entry(root, textvariable=self.path_name_string).pack()

	def secondLabel(self, root):
		# second label - deck string
		(Label(root, bg='lightgreen', text="Exact name of the deck please: ")).pack()
		# field for deck name
		self.deck_name_string = StringVar()
		Entry(root, textvariable=self.deck_name_string).pack()

	def thirdLabel(self, root):
		# third label - card type int
		self.card_type_int = IntVar()
		(Checkbutton(root, text="Do you want reverse cards as well? ", variable=self.card_type_int)).pack()

	def onGoBtnClick(self):
		return_values = [self.path_name_string.get(), self.deck_name_string.get(), self.card_type_int.get()]
		self.returns = return_values 
		self.root.destroy()

	def runSetUp(self):
		self.root = Tk()
		self.firstLabel(self.root)
		self.secondLabel(self.root)
		self.thirdLabel(self.root)
		Button(self.root, text="GO!", command=self.onGoBtnClick).pack()
		self.root.mainloop()
		return self.returns



# 1 - open both programs
import pyautogui
import time 
from os.path import isfile, join as pjoin
import os 
import re
pyautogui.PAUSE = .5

class OpenPrograms(object):
	def __init__(self):
		None

	# pyautogui way to open a program
	def open_anki_desktop(self):
		pyautogui.press('win')
		pyautogui.typewrite('anki')
		pyautogui.press('enter')
		time.sleep(10)

	# pyautogui way to expand current window to full screen
	def expand_anki_desktop(self):
		pyautogui.hotkey('win', 'up')

	def run_open_program(self):
		self.open_anki_desktop()
		self.expand_anki_desktop()



class ReadTextDocument(object):
	def __init__(self):
		self.text_file = None
		self.list_of_lines = []
		self.list_of_front_sides = []
		self.list_of_back_sides = []

	def findTextFile(self, destination_directory):
		# 'destination_directory' is the string of the file path
		# need to find the txt document in the directory 
		files_in_destination_folder = [f for f in os.listdir(destination_directory)
			if isfile(pjoin(destination_directory, f))]

		for line in files_in_destination_folder:
			if line.endswith('.txt'):
				self.text_file = line


	def openTextFile(self, text_file):
		# opening, reading the txt document, and returning python list of lines
		opened_text_file = open(self.text_file, 'r')
		for line in opened_text_file:
			self.list_of_lines.append(line.strip())

	def parseText(self, list_of_lines, list_of_front_sides, list_of_back_sides):
		for item in list_of_lines:
			front_side = re.findall('(.*)\s-\s', item)
			self.list_of_front_sides.extend(front_side)

			back_side = re.findall('\s-\s(.*)', item)
			self.list_of_back_sides.extend(back_side)

	def moveTextFile(self, destination_directory, text_file):
		os.rename(os.path.join(destination_directory, self.text_file),os.path.
			join(destination_directory, 'old_text_files', self.text_file))
		

	def run_ReadTextDocument(self, destination_directory):
		self.findTextFile(destination_directory)
		self.openTextFile(self.text_file)
		self.parseText(self.list_of_lines, self.list_of_front_sides, self.list_of_back_sides)
		self.moveTextFile(destination_directory, self.text_file)
		return [self.list_of_front_sides, self.list_of_back_sides]


class AddNotes(object):
	def __init__(self):
		self.deck_name = None
		self.card_type = None

	# Sortcuts and screen positions
	# 	- a = add card
	# 	- ctrl + d = select a target deck
	#	- ctrl + n = change notecard type
	# 	- ctrl + enter = enter / add that card

	def createNewCardSequence(self, user_returns, list_of_front_sides, list_of_back_sides):
		# getting user inputs
		self.deck_name = user_returns[1]
		if user_returns[2] == 0:
			self.card_type = 'one_sided'
		elif user_returns[2] == 1: 
			self.card_type = 'double_sided'

		# actions only needed to be done one time per text_file
		pyautogui.typewrite('a')
		# adds a new card
		pyautogui.hotkey('ctrl', 'n')
		# opens card type menu (only need to do this once)
		if self.card_type == 'one_sided':
			pyautogui.typewrite('basic')
			pyautogui.press('enter')
		if self.card_type == 'double_sided':
			pyautogui.typewrite('rev')
			# rev triggers reverse / double sided cards
			pyautogui.press('enter')

		pyautogui.hotkey('ctrl', 'd')
		# opens deck menu
		pyautogui.typewrite(self.deck_name)
		# inputs the user inputed deck_name
		pyautogui.press('enter')


		# loops through cards to be added
		'''or front, back in zip(list_of_front_sides, list_of_back_sides):
			pyautogui.typewrite(front)
			pyautogui.press('tab')
			pyautogui.typewrite(back)
			pyautogui.hotkey('ctrl', 'enter')
			time.sleep(2)'''




class ClosePrograms(object):
	# functions to close programs and to move directories
	def __init__(self):
		None

	def closeCurrentWindow(self):
		pyautogui.hotkey('alt', 'f4')

	def runClosePrograms(self):
		self.closeCurrentWindow()
		self.closeCurrentWindow()





		






















