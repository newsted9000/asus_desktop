import pyautogui
import time
import os
from os.path import isfile, join as pjoin

monkerPath = 'D:\MonkerSolver\savedRuns\ip_4B_19March2017'

monkerImage = 'openPosition.png'
treePos = (78,46)
newPos = (36,81)
rangePos = (128,81)
solvePos = (177,49)
startPos = (59,113)
topNode = (81,110)
topNodeBranch1 = (111,133)
allInPos = (646,473)
addPos = (738,522)
removePos = (801,519)
AclubsPos = (42,171)
deuceHeartPos = (389,231)
topLeftCorner = (1,1)
bottomRightCorner = (1004,711)
gyazoButton = (514,871)
savePos = (136,116)
settingsPos = (279,49)
saveDefPos = (636,175)

stackSize = '33'
potSize = '33'
rangeList = ['xxyz:([K-T][K-T][K-8][K-8],[Q-9][Q-9][Q-7][Q-7])!RR, xxyy:([K-T][K-T][K-7][K-7],[Q-8][Q-8][Q-6][Q-6],[T-7][T-7][T-5][T-5]), RR:(765+,875+,865+)!(RRR, A, wxyz)', 'AA, AKK']
typeOfPot = '4B_OPmustCH'
date = '22March2017'

kuberFlopsList = ['3s3dKs', '7s7d6s','QsQd7s','2d3sAs','2s4d8c','2s5dQc','2s6dQc','2d9sKs','2sQsKd','3s5d8c','3sTdJc','3sJsAd','4s6sJd','4s9dTc','4sTsJd','4dTsKs','5s6dTc','5s6dAc','5d7s9s','5s9sKd','7d8sTs','7d8sJs','7sQsAs','7sKsAd','8s9dAc']
kuberFlopNum = len(kuberFlopsList)
quarterPotHotKey = 'a'

minutesToRunSim = 10
secondsToRunSim = minutesToRunSim * 60 

tempList = ['2s6dQc', '4s9dT2', '5s6dTc', '5s9sKd', '7d8sJs', '7sQsAs']





class monkerInterface:

	def __init__(self):
		None

	def openProgram(self):
		pyautogui.press('win')
		pyautogui.typewrite('monker')
		pyautogui.press('enter')

	def testOpenPostion(self, monkerImage):

		if pyautogui.locateOnScreen(monkerImage) == (499, 84, 50, 43):
			return True

	def newSimOmaha(self, newPos, stackSize, potSize):
		pyautogui.click(newPos)
		pyautogui.press('tab')
		pyautogui.press('tab')		
		pyautogui.press('right')
		pyautogui.press('tab')		
		pyautogui.press('right')		
		pyautogui.press('tab')
		pyautogui.press('tab')		
		pyautogui.press('enter')

		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('backspace')
		pyautogui.press('backspace')
		pyautogui.press('backspace')
		pyautogui.typewrite(stackSize)
		pyautogui.press('tab')
		pyautogui.press('backspace')
		pyautogui.press('backspace')
		pyautogui.press('backspace')
		pyautogui.typewrite(stackSize)
		pyautogui.press('tab')			
		pyautogui.press('backspace')
		pyautogui.typewrite(potSize)
		pyautogui.press('tab')		
		pyautogui.press('enter')

	def enterRanges(self, rangePos, rangeList):
		# O = ip, 1 = op
		pyautogui.click(rangePos)
		pyautogui.typewrite(rangeList[1])
		pyautogui.press('tab')
		pyautogui.typewrite(rangeList[0])
		pyautogui.hotkey('alt', 'f4')

	def treeBuilder(self, topNode, topNodeBranch1, allInPos, addPos, removePos, quarterPotHotKey):
		pyautogui.click(topNodeBranch1)
		pyautogui.click(allInPos)
		pyautogui.click(removePos)
		pyautogui.click(topNodeBranch1)
		pyautogui.typewrite(quarterPotHotKey)


	def destFolder(self, monkerPath, board, kuberNumber, settingsPos, saveDefPos):
		#newFile = pjoin(monkerPath, kuberNumber)
		#os.makedirs(newFile)
		pyautogui.click(settingsPos)
		pyautogui.click(saveDefPos)
		pyautogui.typewrite(monkerPath)
		pyautogui.typewrite('/')
		pyautogui.typewrite(kuberNumber)
		pyautogui.press('enter')		

	def solveTab(self, solvePos):
		pyautogui.click(solvePos)

	def enterBoard(self, AclubsPos, deuceHeartPos, board):
		clubLine = AclubsPos[1]
		heartLine = deuceHeartPos[1]
		aceLine = AclubsPos[0]
		deuceLine = deuceHeartPos[0]
		distanceDownSuits = (heartLine - clubLine) / 3
		distanceAcrossRanks = (deuceLine - aceLine) / 12
		card1 = board[0:2]
		card2 = board[2:4]
		card3 = board[4:6]

		# Card 1 Rank
		if card1[0] == 'A': rankCard1 = aceLine
		elif card1[0] == 'K': rankCard1 = aceLine + distanceAcrossRanks
		elif card1[0] == 'Q': rankCard1 = aceLine + (distanceAcrossRanks * 2)
		elif card1[0] == 'J': rankCard1 = aceLine + (distanceAcrossRanks * 3)
		elif card1[0] == 'T': rankCard1 = aceLine + (distanceAcrossRanks * 4)
		elif card1[0] == '9': rankCard1 = aceLine + (distanceAcrossRanks * 5)
		elif card1[0] == '8': rankCard1 = aceLine + (distanceAcrossRanks * 6)
		elif card1[0] == '7': rankCard1 = aceLine + (distanceAcrossRanks * 7)
		elif card1[0] == '6': rankCard1 = aceLine + (distanceAcrossRanks * 8)
		elif card1[0] == '5': rankCard1 = aceLine + (distanceAcrossRanks * 9)
		elif card1[0] == '4': rankCard1 = aceLine + (distanceAcrossRanks * 10)
		elif card1[0] == '3': rankCard1 = aceLine + (distanceAcrossRanks * 11)
		elif card1[0] == '2': rankCard1 = aceLine + (distanceAcrossRanks * 12)

		# Card 1 Suit
		if card1[1] == 'c': suitcard1 = clubLine
		elif card1[1] == 's': suitcard1 = clubLine + distanceDownSuits
		elif card1[1] == 'd': suitcard1 = clubLine + (distanceDownSuits * 2)
		elif card1[1] == 'h': suitcard1 = heartLine

		# Card 2 Rank
		if card2[0] == 'A': rankcard2 = aceLine
		elif card2[0] == 'K': rankcard2 = aceLine + distanceAcrossRanks
		elif card2[0] == 'Q': rankcard2 = aceLine + (distanceAcrossRanks * 2)
		elif card2[0] == 'J': rankcard2 = aceLine + (distanceAcrossRanks * 3)
		elif card2[0] == 'T': rankcard2 = aceLine + (distanceAcrossRanks * 4)
		elif card2[0] == '9': rankcard2 = aceLine + (distanceAcrossRanks * 5)
		elif card2[0] == '8': rankcard2 = aceLine + (distanceAcrossRanks * 6)
		elif card2[0] == '7': rankcard2 = aceLine + (distanceAcrossRanks * 7)
		elif card2[0] == '6': rankcard2 = aceLine + (distanceAcrossRanks * 8)
		elif card2[0] == '5': rankcard2 = aceLine + (distanceAcrossRanks * 9)
		elif card2[0] == '4': rankcard2 = aceLine + (distanceAcrossRanks * 10)
		elif card2[0] == '3': rankcard2 = aceLine + (distanceAcrossRanks * 11)
		elif card2[0] == '2': rankcard2 = aceLine + (distanceAcrossRanks * 12)

		# Card 2 Suit
		if card2[1] == 'c': suitcard2 = clubLine
		elif card2[1] == 's': suitcard2 = clubLine + distanceDownSuits
		elif card2[1] == 'd': suitcard2 = clubLine + (distanceDownSuits * 2)
		elif card2[1] == 'h': suitcard2 = heartLine

		# Card 3 Rank
		if card3[0] == 'A': rankcard3 = aceLine
		elif card3[0] == 'K': rankcard3 = aceLine + distanceAcrossRanks
		elif card3[0] == 'Q': rankcard3 = aceLine + (distanceAcrossRanks * 2)
		elif card3[0] == 'J': rankcard3 = aceLine + (distanceAcrossRanks * 3)
		elif card3[0] == 'T': rankcard3 = aceLine + (distanceAcrossRanks * 4)
		elif card3[0] == '9': rankcard3 = aceLine + (distanceAcrossRanks * 5)
		elif card3[0] == '8': rankcard3 = aceLine + (distanceAcrossRanks * 6)
		elif card3[0] == '7': rankcard3 = aceLine + (distanceAcrossRanks * 7)
		elif card3[0] == '6': rankcard3 = aceLine + (distanceAcrossRanks * 8)
		elif card3[0] == '5': rankcard3 = aceLine + (distanceAcrossRanks * 9)
		elif card3[0] == '4': rankcard3 = aceLine + (distanceAcrossRanks * 10)
		elif card3[0] == '3': rankcard3 = aceLine + (distanceAcrossRanks * 11)
		elif card3[0] == '2': rankcard3 = aceLine + (distanceAcrossRanks * 12)

		# Card 3 Suit
		if card3[1] == 'c': suitcard3 = clubLine
		elif card3[1] == 's': suitcard3 = clubLine + distanceDownSuits
		elif card3[1] == 'd': suitcard3 = clubLine + (distanceDownSuits * 2)
		elif card3[1] == 'h': suitcard3 = heartLine


		pyautogui.click(rankCard1, suitcard1)
		pyautogui.click(rankcard2, suitcard2)
		pyautogui.click(rankcard3, suitcard3)

	def startButton(self, startPos):
		pyautogui.click(startPos)

	def saveTree(self, savePos, typeOfPot, kuberNumber, board, date):
		pyautogui.click(savePos)
		pyautogui.typewrite(typeOfPot)
		pyautogui.typewrite('_')
		pyautogui.typewrite(kuberNumber)
		pyautogui.typewrite('_')
		pyautogui.typewrite(board)
		pyautogui.typewrite('_')
		pyautogui.typewrite(date)
		pyautogui.press('enter')

	def screenShot(self, gyazoButton, topLeftCorner, bottomRightCorner):
		pyautogui.click(gyazoButton)
		pyautogui.moveTo(topLeftCorner)
		pyautogui.dragTo(bottomRightCorner, button='left')
		time.sleep(5)
		pyautogui.hotkey('alt', 'f4')

	def exitProgram(self):
		pyautogui.hotkey('alt', 'f4')

# Calling Functions in a loop of the kuberFlopsList

for i, flops in enumerate(kuberFlopsList):

	board = flops
	kuberNumber = str(i + 19)
	for tempboard in tempList:
		if tempboard == flops:
			# create instance of the class
			testingClass = monkerInterface()
			# opening the program (and waiting for it to load)
			testingClass.openProgram()
			time.sleep(5)
			# creating a new sim
			testingClass.newSimOmaha(newPos, stackSize, potSize)
			# entering the ranges
			testingClass.enterRanges(rangePos, rangeList)
			# building the tree structure
			testingClass.treeBuilder(topNode, topNodeBranch1, allInPos, addPos, removePos, quarterPotHotKey)
			# go to the settings tab
			#testingClass.destFolder(monkerPath, board, kuberNumber, settingsPos, saveDefPos)
			# go to the solve tab
			testingClass.solveTab(solvePos)
			# entering the board cards (and wait)
			testingClass.enterBoard(AclubsPos, deuceHeartPos, board)
			time.sleep(2)
			# starting the program (bug forces to start,stop, then start again)
			testingClass.startButton(startPos)
			time.sleep(10)
			testingClass.startButton(startPos)
			time.sleep(10)
			testingClass.startButton(startPos)
			# wait while the sims run and print countdown timer
			time.sleep(secondsToRunSim / 2)
			print (secondsToRunSim / 2)
			time.sleep(secondsToRunSim / 4)
			print (secondsToRunSim / 4)
			time.sleep(secondsToRunSim / 4 - 10)
			print (10)
			time.sleep(10)
			# stopping the sim
			testingClass.startButton(startPos)
			# save the sim	
			testingClass.saveTree(savePos, typeOfPot, kuberNumber, board, date)
			# screenshot of the results
			testingClass.screenShot(gyazoButton, topLeftCorner, bottomRightCorner)
			time.sleep(5)
			# exit the program (and wait to close)
			testingClass.exitProgram()
			time.sleep(5)
