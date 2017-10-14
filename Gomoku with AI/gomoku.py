from tkinter import *
import time
import random
from StartScreen import *
from Window import *
from Board import *
from Game import *
from DrawDia import *
import winsound

# barebones copy from course webs

def init(data):
	data.s = StartScreen(data.width, data.height,data)
	data.isStart = False
	data.anitime = 0
	data.drawWin = DrawDia(data)
	data.drawIns = DrawDia(data)
	data.drawDiff = DrawDia(data)
	data.drawColor = DrawDia(data)


def mousePressed(event, data):
	if not data.s.isOver:
		data.s.mousePressedWrapper(event)
	elif data.isStart and data.g.board.isWin == False and data.g.inComputerTurn == False and not data.g.inSelectHuman:
		data.g.takeTurn(event)


def keyPressed(event, data):
	if event.keysym == "r":
		init(data)
	if not data.s.isOver:
		data.s.keyPressedWrapper(event)
		redrawAll(data.canvas, data)


def timerFired(data):
	if not data.s.isOver and data.s.fontSize > 80:
		data.s.fontSize -= 2

	if not data.s.isOver and data.anitime%600 == 0:
		data.s.textcolor = not data.s.textcolor
		data.anitime+=10
	else:
		data.anitime+=10
	if data.s.isOver and data.isStart == False:
		data.g = Game(data.s.info,data)

		data.isStart = True
	if data.isStart	== True and data.g.currentPlayer[0]=='computer' and not data.g.board.isWin:
		data.g.inComputerTurn = True
		#redrawAll(data.canvas, data)
		data.g.computerTurn()

	if data.isStart	== True and data.g.board.isWin:

		data.drawWin.onTimerFired()
		# print(data.d.text,' ',data.d.textPos)
	if not data.s.isOver and data.s.chooseOppo:
		data.drawIns.onTimerFired()
	if not data.s.isOver and data.s.isChooseDiffcult:
		data.drawDiff.onTimerFired()
	if not data.s.isOver and data.s.chooseColor:
		data.drawColor.onTimerFired()

def redrawAll(canvas, data):
	

	if not data.s.isOver:
		data.s.drawEverything()
	if not data.s.isOver and data.s.chooseOppo:
		data.drawIns.drawChooseOppo(canvas)
	if not data.s.isOver and data.s.isChooseDiffcult:
		data.drawDiff.drawChooseDiff(canvas)
	if not data.s.isOver and data.s.chooseColor:
		data.drawColor.drawChooseColor(canvas)
	elif data.isStart:
		data.g.board.drawBoard(data.canvas)
		if data.g.board.isWin:
			data.drawWin.drawWin(canvas, data.g.notCurrentPlayer[1].upper(),data.g.notCurrentPlayer[0],data.g.currentPlayer[0])
			
			# canvas.create_text(data.width/2+25,data.height/6,
			# 	text = data.g.notCurrentPlayer[1].upper() + " WINS!!",font = ("Fixedsys", 60))
			# canvas.create_text(data.width/2,data.height/8*7,
			# 		text = "Press 'r' to restart the game",font = ("Fixedsys", 30))

			# if data.g.notCurrentPlayer[0] =='computer':
			# 	canvas.create_text(data.width/2+25,data.height/6,
			# 	text = data.g.notCurrentPlayer[1].upper() + " WINS!!",font = ("Fixedsys", 60),fill = 'red')
			# 	canvas.create_text(data.width/2+40,data.height/2-30,
			# 		text = 'OH!', font = ("Fixedsys", 230),fill = "red")
			# 	canvas.create_text(data.width/2,data.height/2+150,
			# 		text = 'you were beaten by a computer!', font = ("Fixedsys", 28),fill = "red")
			# 	canvas.create_text(data.width/2,data.height/8*7,
			# 		text = "Press 'r' to restart the game",font = ("Fixedsys", 30),fill = "red")



def run(width=300, height=300):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	def timerFiredWrapper(canvas, data):
		timerFired(data)
		redrawAllWrapper(canvas, data)
		canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
		
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	data.timerDelay = 10 # milliseconds
	
	# create the root and the canvas
	data.root = Tk()
	#data.root.resizable(0,0)
	data.root.title("Gomuku")
	data.canvas = Canvas(data.root, width=data.width, height=data.height)
	data.canvas.pack()
	init(data)
	
	# set up events
	data.canvas.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, data.canvas, data))
	data.root.bind("<Key>", lambda event:
							keyPressedWrapper(event, data.canvas, data))
	timerFiredWrapper(data.canvas, data)
	data.root.mainloop()  # blocks until window is closed

#run(600,600)