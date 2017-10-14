from Board import *
import copy
import random

class Game(object):
	def __init__(self,info,data):
		self.canvas = data.canvas
		self.player1 = info[0]
		self.player2 = info[1]
		if len(info) == 3:
			self.mode = info[2]
		self.notCurrentPlayer = self.player2
		self.inComputerTurn = False

		self.currentPlayer = self.player1
		self.board = Board(data.width,data.height)
		self.board.pieceCount = 1
		self.rowcolSeq = []
		self.cutOffDepth = 5
		self.inSelectHuman = False
	
	def humanTurn(self,event):
		self.humanKeyPressedWrapper(event)

	def computerTurn(self):
		if self.currentPlayer[0] == "computer":
			if self.mode ==  1:
				self.computerWrapper()
			else:
				self.minimaxWrapper()
			# print(self.board.getScore())
			# print("done")
			self.alternateTurn()
			self.inComputerTurn = False
			self.board.pieceCount+=1

	def takeTurn(self,event):
		if self.currentPlayer[0] == "human" and self.inComputerTurn == False:
			self.inSelectHuman = True
			self.humanTurn(event)
			if self.human == True:
				# print("Human!")
				self.board.drawPiece(self.canvas)
				self.canvas.update()
				self.alternateTurn()
				# print(self.board.getScore())
				# print(self.board.blackCount)
				# print(self.board.whiteCount)
				self.board.pieceCount+=1
			self.inSelectHuman = False

	def humanKeyPressedWrapper(self,event):
		self.human = False
		margin = self.board.margin
		x=event.x+self.board.cellSize/2-margin
		y=event.y+self.board.cellSize/2-margin
		w=self.board.col*self.board.cellSize 
		h=self.board.row*self.board.cellSize 
		if 0<x<w and 0<y<h:
			col,row = int(x // self.board.cellSize), int(y//self.board.cellSize)
			if self.board.board[row][col]==-1:
				self.inputInfo(row,col)
				self.human = True
			
	def alternateTurn(self):
		if self.currentPlayer == self.player1:
			self.currentPlayer = self.player2
			self.notCurrentPlayer = self.player1
		else:
			self.currentPlayer = self.player1
			self.notCurrentPlayer = self.player2

	def inputInfo(self,row,col):
		self.board.board[row][col]=self.currentPlayer[1]
		self.board.count[row][col]=self.board.pieceCount
		self.rowcolSeq.append((row,col))
		self.board.checkBoard()
		
		

	def minimaxWrapper(self):
		playerSaver = self.currentPlayer
		if self.rowcolSeq == []:
			self.inputInfo(7, 7)
			return
		if len(self.rowcolSeq) == 1:
			self.inputInfo(self.rowcolSeq[0][0], self.rowcolSeq[0][1]+1)
			return
		if self.currentPlayer[1] == 'black':
			depth = 0
		else:
			depth = 1
		listOfMoves = self.getPossibleMoves()
		self.decisionList = []
		row,col = self.minimax(listOfMoves,depth)
		self.currentPlayer = playerSaver
		self.inputInfo(row, col)
		


	def getPossibleMoves(self):
		res = []
		board = self.board.board
		for row in range(len(board)):
			for col in range(len(board[0])):
				if board[row][col] == -1 and self.isConnected(row,col):
					res.append((row,col))
		return res

	def getPossibleScore(self,board,player):
		pass

	# minimize the possible points
	# change number'1' to '2' will increase calculating time however make the ai stronger
	def isConnected(self,row,col):
		rowLow,colLow = row - 1, col - 1
		if rowLow<0:rowLow = 0
		if colLow<0:colLow = 0
		rowHigh,colHigh = row + 1, col + 1
		if rowHigh>14:rowHigh = 14
		if colHigh>14:colHigh = 0
		for row in range(rowLow,rowHigh+1):
			for col in range(colLow,colHigh+1):
				if self.board.board[row][col] != -1:
					return True
		return False

	def minimax(self,l,depth):
		#self.minimax
		#scorelists
		
		#tempBoard = Board()
		#tempBoard.board = copy.deepcopy(self.board.board)

		scores = {}
		self.scores = []
		tempL = {}
		####improve the speed however weaker the ai

		# for moves in l:
		# 	self.board.board[moves[0]][moves[1]] = self.currentPlayer[1]
		# 	self.board.now = self.currentPlayer[1]
		# 	self.scores.append((self.board.getScore(),moves[0],moves[1]))
		# 	self.board.board[moves[0]][moves[1]] = -1
		# if self.currentPlayer[1] == 'black':
		# 	s = sorted(self.scores,key = lambda tup:tup[0],reverse = True)[:5]
		# else:
		# 	s = sorted(self.scores,key = lambda tup:tup[0],reverse = False)[:5]
		# l = []
		# for e in s:
		# 	l.append((e[1],e[2]))
		for moves in l:
			# row = moves[0]
			# col = moves[1]
			# if 
			self.board.board[moves[0]][moves[1]] = self.currentPlayer[1]
			if self.board.checkBoard() == True:
				self.board.isWin = False
				self.board.board[moves[0]][moves[1]] = -1
				return (moves[0],moves[1])
			self.alternateTurn()
			lnext = self.getPossibleMoves()
			self.scores = []
			for m in lnext:
				
				self.board.board[m[0]][m[1]] = self.currentPlayer[1]
				self.board.now = self.currentPlayer[1]
				self.scores.append((self.board.getScore()))
				# print(self.board.getScore(), end = " ")
				self.board.board[m[0]][m[1]] = -1
				#def sorter(t):
				#return t[0]
			# print()
			if self.currentPlayer[1] == 'black':
				score = max(self.scores)
			else:
				score = min(self.scores)
			# print(moves,' ',score)
			scores[moves] = score
			self.alternateTurn()
			self.board.board[moves[0]][moves[1]] = -1
			inverse = [(value, key) for key, value in scores.items()]
		if self.currentPlayer[1] == 'white':

			return min(inverse)[1]
		else:
			return max(inverse)[1]

			# if self.currentPlayer[1] == 'black':
			# 	maxValue = maxValue = self.scores[0][0]
			# 	res = []
			# 	for tup in self.scores:
			# 		if tup[0]>maxValue:
			# 			maxValue = tup[0]
			# 			res = [(tup[1],tup[2])]
			# 		elif tup[0] == maxValue:
			# 			res+=[(tup[1],tup[2])]
			# 	row,col = random.choice(res)
			# 	self.inputInfo(row, col)
			# 	return
			# else:
			# 	maxValue = self.scores[0][0]
			# 	res = []
			# 	for tup in self.scores:
			# 		if tup[0]<maxValue:
			# 			maxValue = tup[0]
			# 			res = [(tup[1],tup[2])]
			# 		elif tup[0] == maxValue:
			# 			res+=[(tup[1],tup[2])]
			# 	row,col = random.choice(res)
			# 	self.inputInfo(row, col)
			# 	return








		# if depth == self.cutOffDepth:
		# 	return
		


	def computerWrapper(self):

		self.scores = []
		if self.rowcolSeq == []:
			self.inputInfo(7, 7)
			return
		if len(self.rowcolSeq) == 1:
			self.inputInfo(self.rowcolSeq[0][0], self.rowcolSeq[0][1]+1)
			return
		for row in range(len(self.board.board)):
			for col in range(len(self.board.board[0])):
				if self.board.board[row][col] == -1:
					self.board.board[row][col] = self.currentPlayer[1]
					self.board.now = self.currentPlayer[1]
					self.scores.append((self.board.getScore(),row,col))
					self.board.board[row][col] = -1
		if self.currentPlayer[1] == 'black':
			maxValue = self.scores[0][0]
			res = []
			for tup in self.scores:
				if tup[0]>maxValue:
					maxValue = tup[0]
					res = [(tup[1],tup[2])]
				elif tup[0] == maxValue:
					res+=[(tup[1],tup[2])]
			row,col = random.choice(res)
			self.inputInfo(row, col)
			return
		else:
			maxValue = self.scores[0][0]
			res = []
			for tup in self.scores:
				if tup[0]<maxValue:
					maxValue = tup[0]
					res = [(tup[1],tup[2])]
				elif tup[0] == maxValue:
					res+=[(tup[1],tup[2])]
			row,col = random.choice(res)
			self.inputInfo(row, col)
			return



