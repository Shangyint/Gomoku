
class Board(object):


	def __init__(self,w=600,h=600):
		self.row, self.col = 15,15
		self.margin = 13
		self.cellSize = 41
		self.width,self.height = w,h
		self.initBoard()
		self.now = 'white'
		self.isWin = False
		self.pieceCount = 0

	def initBoard(self):
		self.board = []
		self.count = []
		for row in range(self.row):
			self.board.append([-1] * self.col)
		for row in range(self.row):
			self.count.append([0] * self.col)

	def drawBoard(self,canvas):
		canvas.create_rectangle(0,0,self.width,self.height,fill = "white")
		self.drawCrossLines(canvas)
		self.drawVerticalLines(canvas)
		self.drawSmallDots(canvas)
		self.drawOutline(canvas)
		self.drawPiece(canvas)


	def drawCrossLines(self,canvas):
		for rowLine in range(self.row):
			canvas.create_line(self.margin,self.margin+rowLine*self.cellSize,
				self.width-self.margin,self.margin+rowLine*self.cellSize)

	def drawVerticalLines(self,canvas):
		for colLine in range(self.col):
			canvas.create_line(self.margin+colLine*self.cellSize,self.margin,
				self.margin+colLine*self.cellSize,self.height-self.margin)

	def drawSmallDots(self,canvas):
		l = []
		radius = 2.5
		l.append((self.margin+3*self.cellSize,self.margin+3*self.cellSize))
		l.append((self.margin+11*self.cellSize,self.margin+3*self.cellSize))
		l.append((self.margin+3*self.cellSize,self.margin+11*self.cellSize))
		l.append((self.margin+11*self.cellSize,self.margin+11*self.cellSize))
		l.append((self.margin+7*self.cellSize,self.margin+7*self.cellSize))
		for c in l:
			canvas.create_oval(c[0]-radius,c[1]-radius,c[0]+radius,c[1]+radius,fill = 'black')

	def drawOutline(self,canvas):
		gap = 3
		canvas.create_line(self.margin-gap,self.margin-gap,
		self.width+gap-self.margin,self.margin-gap)
		canvas.create_line(self.margin-gap,self.height-self.margin+gap,
		self.width+gap-self.margin,self.height-self.margin+gap)
		canvas.create_line(self.margin-gap,self.margin-gap,
		self.margin-gap,self.height-self.margin+gap)
		canvas.create_line(self.margin-gap,self.height-self.margin+gap,
		self.width+gap-self.margin,self.height-self.margin+gap)
		canvas.create_line(self.width+gap-self.margin,self.height-self.margin+gap,
		self.width+gap-self.margin,self.margin-gap)	

	def checkBoard(self):
		result = False
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				if self.checkFromCell(self.board,row,col) and self.board[row][col]!=-1:
					self.isWin = True
					return True
		return False

	# checkFromCell and checkFromCellDirection
	# cited from course website, wordsearch
	def checkFromCell(self,board, startRow, startCol):
		result = False
		for index in range(8):
			if self.checkFromCellInDirection(board, startRow, startCol, index):
				return True        
		return False
	 
	def checkFromCellInDirection(self,board, startRow, startCol, index):
		(rows, cols) = (len(board), len(board[0]))
		dirs = [ (-1, -1), (-1, 0), (-1, +1),
				 ( 0, -1),          ( 0, +1),
				 (+1, -1), (+1, 0), (+1, +1) ]
		dirNames = [ "up-left"  ,   "up", "up-right",
					 "left"     ,         "right",
					 "down-left", "down", "down-right" ]
		(drow,dcol) = dirs[index]    
		for i in range(5):
			row = startRow + i*drow
			col = startCol + i*dcol
			if ((row < 0) or (row >= rows) or
				(col < 0) or (col >= cols) or
				(board[row][col] != board[startRow][startCol])):
				return False
		return True

	def drawPiece(self,canvas):
		for row in range(self.row):
			for col in range(self.col):
				if self.board[row][col] != -1:
					x = col * self.cellSize + self.margin
					y = row * self.cellSize + self.margin
					r = int(self.cellSize/2) - 2
					canvas.create_oval(x-r,y-r,x+r,y+r,fill = self.board[row][col])
					if self.board[row][col] == "white":
						fill = "black"
					else:
						fill = "white"
					if self.count[row][col] == self.pieceCount-1:
						canvas.create_rectangle(x-10,y-8,x+10,y+8,fill = "yellow")
						fill = "black"
					canvas.create_text(x,y,text = str(self.count[row][col]), fill = fill)

############################ checkers ############################
############################ important ############################

##### ideas from github, no code copied and pasted, no pseudo code 
##### copied as well, I use a new approach to calculate the score
##### https://github.com/WxnChen11/CSC180/blob/18049afaa526e42859caaca4ada4baa93670952f/labs/lab08/lab08.py
##### I believe my approach is better than this in website, however,
##### thank this code as it inspires me in some ways
	def getScore(self):
		self.initCount()
		self.dectRow()
		self.dectCol()
		self.dectDia()
		return self.caculate(self.blackCount,self.whiteCount)

	def caculate(self,bc,wc):
		res = 0
		# change this number to adjust the AI's style e.g. aggressive or defensive
		if self.now == 'black':
			for key in bc:
				if key == 5 and bc[key]>0:
					return 10000000
				elif key == (4,0):
					res+=bc[key]*5000
				elif key == (3,0):
					res+=bc[key]*50
				elif key == (4,1):
					res+=bc[key]*30
				elif key == (3,1) or key == (2,0):
					res+=bc[key]*10
				elif key == (2,1) or key == (1,0):
					res+=bc[key]*1
			for key in wc:
				if key == 5 and wc[key]>0:
					return -10000000
				elif key == (4,1) or key == (4,0):
					res-=wc[key]*100000
				elif key == (3,0):
					res-=wc[key]*1000
				elif key == (3,1) or key == (2,0):
					res-=wc[key]*10
				elif key == (2,1) or key == (1,0):
					res-=wc[key]*1
			return res
		elif self.now == 'white':
			for key in bc:
				if key == 5 and bc[key]>0:
					return 10000000
				elif key == (4,0) or key == (4,1) :
					res+=bc[key]*100000
				elif key == (3,0):
					res+=bc[key]*1000
				elif key == (3,1) or key == (2,0):
					res+=bc[key]*10
				elif key == (2,1) or key == (1,0):
					res+=bc[key]*1
			for key in wc:
				if key == 5 and wc[key]>0:
					return -10000000
				elif key == (4,0):
					res-=wc[key]*5000
				elif key == (3,0):
					res-=wc[key]*50
				elif key == (4,1):
					res-=wc[key]*30
				elif key == (3,1) or key == (2,0):
					res-=wc[key]*10
				elif key == (2,1) or key == (1,0):
					res-=wc[key]*1
			return res

	def initCount(self):
		# (x,y) x means the lenth of the run y means open or semi open
		self.blackCount = {5:0,
		(4,0):0,(4,1):0,
		(3,0):0,(3,1):0,
		(2,0):0,(2,1):0,
		(1,0):0,(1,1):0}
		self.whiteCount = {5:0,
		(4,0):0,(4,1):0,
		(3,0):0,(3,1):0,
		(2,0):0,(2,1):0,
		(1,0):0,(1,1):0}

	def dectRow(self):
		# result = 0
		for row in self.board:
			self.detectLine(row)
		# return result

	def dectCol(self):
		col = []
		for c in range(len(self.board[0])):
			for row in range(len(self.board)):
				col.append(self.board[row][c])
			self.detectLine(col)
			col = []

	def dectDia(self):
		diagonals = Board.get_backward_diagonals(self.board)+Board.get_forward_diagonals(self.board)
		for line in diagonals:
			self.detectLine(line)

# four staticmethod copy from stackoverflow 
# return all diagonals of a 2d list
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
	@staticmethod
	def get_backward_diagonals(grid):
		b = [None] * (len(grid) - 1)
		grid = [b[i:] + r + b[:i] for i, r in enumerate(Board.get_rows(grid))]
		return [[c for c in r if not c is None] for r in Board.get_cols(grid)]

	@staticmethod
	def get_forward_diagonals(grid):
		b = [None] * (len(grid) - 1)
		grid = [b[:i] + r + b[i:] for i, r in enumerate(Board.get_rows(grid))]
		return [[c for c in r if not c is None] for r in Board.get_cols(grid)]

	@staticmethod
	def get_rows(grid):
		return [[c for c in r] for r in grid]

	@staticmethod
	def get_cols(grid):
		return zip(*grid)

	def detectLine(self,line):
		strLine = self.transfer(line,'white')
		self.detect(strLine,'w')
		strLine = self.transfer(line,'black')
		self.detect(strLine,'b')

	def transfer(self,line,flag):
		if flag == 'white':
			strLine = 'b'
			for s in line:
				if s == -1:
					strLine += '0'
				elif s == 'black':
					strLine += 'b'
				elif s == 'white':
					strLine += 'w'
			strLine += 'b'
		elif flag == 'black':
			strLine = 'w'
			for s in line:
				if s == -1:
					strLine += '0'
				elif s == 'black':
					strLine += 'b'
				elif s == 'white':
					strLine += 'w'
			strLine += 'w'
		return strLine

	def detect(self,strLine,flag):
		while strLine.find(flag) != -1:
			gap = 0
			start = strLine.find(flag)
			block = 0
			if strLine[start-1] not in ['0',flag]:
				block = 1
			sRest = strLine[start+1:]
			run = 1
			for i in range(len(sRest)):
				if sRest[i] == flag:run+=1
				elif sRest[i] == '0':
					if sRest[i+1] == flag and run != 4 and (run ==2 and sRest[i+2]!=flag) and run<6:
						gap += 1
						continue
					else:break
				else:
					block+=1
					break
			strLine = strLine[start+gap+run:]
			if block < 2:
				self.modify(flag,run,block)

	def modify(self,flag,run,block):
		if flag == 'w':
			if run == 5: self.whiteCount[5]+=1
			elif run<6: self.whiteCount[(run,block)]+=1
		elif flag == 'b':
			if run == 5: self.blackCount[5]+=1
			elif run<6: self.blackCount[(run,block)]+=1