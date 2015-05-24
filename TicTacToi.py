# refer to book 'Invent Your Own Computer Games with Python'
import random

# This function takes the board inputs details and draw it 
# argument board is a python list and its cntents could be X or O or a space character
def drawBoard(board):
	print
	print (' '+board[1]+' | '+board[2]+ ' | '+board[3]+' ')
	print ('------------')
	print (' '+board[4]+' | '+board[5]+ ' | '+board[6]+' ')
	print ('------------')
	print (' '+board[7]+' | '+board[8]+ ' | '+board[9]+' ')
	print
	
# This function lets the player decide their symbol and return a list of two items with first as a player symbol and second as a computer symbol
def chooseSymbol():
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		letter = raw_input('Do you want X or O: ').upper()
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

# This function returns 1 if player wants to play first else 0
def firstPlayer():
	turn = None
	while not(turn == 'Y' or turn == 'N'):
		turn = raw_input('Do you want to play first (y/n): ').upper()
	if turn == 'Y':
		return 1
	else:
		return 0

# It decides whether player wants to play again When a game finished
def playAgain():
	play = None
	while not(play == 'Y' or play == 'N'):
		play = raw_input('Do you want to play again (y/n): ').upper()
	if play == 'Y':
		return 1
	else:
		return 0

# whatever moves are chosen by either player, it will mark it in board
def makeMove(board, letter, move):
	board[move] = letter

# returns true if the corresponding argument le (letter) is winner
# each or condition defines a possible winning condition
def isWinner(bo, le):
	return((bo[1] == le and bo[2] == le and bo[3] == le) or		# upper row
			(bo[4] == le and bo[5] == le and bo[6] == le) or	# middle row
			(bo[7] == le and bo[8] == le and bo[9] == le) or	# bottom row
			(bo[1] == le and bo[4] == le and bo[7] == le) or	# left column
			(bo[2] == le and bo[5] == le and bo[8] == le) or	# middle column
			(bo[3] == le and bo[6] == le and bo[9] == le) or	# last column
			(bo[1] == le and bo[5] == le and bo[9] == le) or	# diagonal one
			(bo[3] == le and bo[5] == le and bo[7] == le))  	# diagonal two
			
# return true if board is free with given move
def isFree(board, move):
	return board[move] == ' ' 

# it helps in getting the move from player
def getPlayerMove(board):
	move = ''
	while True:
		move = raw_input("Enter Your Move: ")
		if move not in('1','2','3','4','5','6','7','8','9') or not isFree(board, int(move)):
			print 'Invalid Choice'
		else:
			return int(move)
			
# returns a copy of board
# this copy will be used while making the computer moves for checking winning and blocking conditions
def getBoardCopy(board):
	return board[:]
			
# returns a random possible choice from provided choice list named moveList
def chooseRandom(board, moveList):
	possibleMove = []
	for i in moveList:
		if isFree(board, i):
			possibleMove.append(i)
	
	if len(possibleMove) != 0:
		return random.choice(possibleMove)
	else:
		return None

# this function decides the appropriate move by computer		
def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter == 'O'
	else:
		playerLetter == 'X'
	
	#check whether computer can win
	for i in range (1,10):
		copy = getBoardCopy(board)
		if isFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i
	#check if player can win, block them
	for i in range (1,10):
		copy = getBoardCopy(board)
		if isFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i
			
	#try corner move
	i = chooseRandom(board, [1,3,7,9])
	if i != None:
		return i
		
	# try middle move
	if isFree(board, 5):
		return 5
	
	# try side move
	return chooseRandom(board, [2,4,6,8])

# returns true if no space available on board
def isBoardFull(board):
	for i in range(1,10):
		if isFree(board, i):
			return False
	return True

# displays the positional value information for moves
def displayInstructions():
	a = ['0','1','2','3','4','5','6','7','8','9']
	print('Moves are Defined as Follows: ')
	drawBoard(a)

# program begines from here
print
print('Welcome to Tic-Tac-Toi...')
displayInstructions()

while True:		# keeps playing untill player choose to quite
	board = [' ']*10
	playerLetter, computerLetter = chooseSymbol()
	turn = firstPlayer()
	if turn:
		print'OK, You go first'
	else:
		print'Cool, I go first'
	
	while True:		# run a single game until it results something
		if turn:	# its player turn
			drawBoard(board)
			move = getPlayerMove(board)
			makeMove(board, playerLetter, move)
			
			if isWinner(board, playerLetter):
				drawBoard(board)
				print'You Won...!'
				break
			elif isBoardFull(board):
				drawBoard(board)
				print"It's a Tie"
				break
			else:
				turn = 0	# make the turn for computer
				
		else:		# computer turn
			move = getComputerMove(board, computerLetter)
			makeMove(board, computerLetter, move)
			if isWinner(board, computerLetter):
				drawBoard(board)
				print 'I Won....!'
				break
			elif isBoardFull(board):
				drawBoard(board)
				print("It's a Tie")
				break
			else:
				turn = 1	# make the turn for player
	if not playAgain():		# one game finished here, ask if player wants another play
		print 'Bye'
		break
		
