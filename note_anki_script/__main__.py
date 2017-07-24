from utils import Tkinter, OpenPrograms, AddNotes, ReadTextDocument, AddNotes, ClosePrograms
import os

# Execute the program 
if __name__ == '__main__':
	# Tktinter interface and user input returns
	app = Tkinter()
	user_returns = app.runSetUp()
	destination_directory = user_returns[0]

	# opening, reading, and parsing the text document
	# returns a list of two lists (front_side_of_cards, back_sides....)
	instance_read_text_class = ReadTextDocument()
	sides_of_cards_lists = instance_read_text_class.run_ReadTextDocument(destination_directory)

	'''# opening Anki desktop
	open_anki = OpenPrograms()
	open_anki.run_open_program()

	# making the cards
	adding_notes = AddNotes()
	adding_notes.createNewCardSequence(user_returns, sides_of_cards_lists[0], sides_of_cards_lists[1])'''

	'''# close the programs
	ClosePrograms().runClosePrograms()'''