from tkinter import *
class DrawDia(object):
	def __init__(self,data):
		self.y = data.height
		self.x = data.width-50
		self.height = 180
		self.text = ""
		self.textPos = 0
		self.textCount = 0

	def onTimerFired(self):
		if self.y > 600-self.height:
			self.y -= 1
		if self.y < 600-self.height +2 and self.textPos<=len(self.text):
			if self.textCount%80 == 0:
				self.textPos+=1
				self.textCount+=10
			else:
				self.textCount+=10

	def drawWin(self,canvas,winner,player,another):
		self.height = 180
		self.text ="* " + winner + " WINS"
		if player == "computer":
			self.text+="\n* Wait You were beaten by a...\n  COMPUTER??"
			self.text+="\n* try hard next time or..."
		self.text+="\n* Press r to restart the game"
		if player == "human" and another == "human":
			self.text+="\n* Yo, playing with a human is...\n  not that fun, try a ...\n* COMPUTER!"
		self.text = self.text.upper()
		self.drawBox(canvas)
		self.drawText(canvas)

	def drawBox(self,canvas):
		canvas.create_rectangle(44,self.y-2,self.x+5,self.y+self.height,fill = 'white')
		canvas.create_rectangle(48,self.y+2,self.x+1,self.y+self.height-3,fill = 'black')

	def drawText(self,canvas):
		text = self.text[:self.textPos] + "_"
		canvas.create_text(56,self.y+10,anchor = NW, text = text, fill = "white", font = ("Fixedsys",22))

	def drawChooseOppo(self,canvas):
		self.height = 180
		self.text = "* CLICK EITHER SIDE OF SCREEN\n  TO SET UP THE GAME\n* CLICK TO PUT YOUR STONES\n  ANYWHERE AVAILABLE IN BOARD\n* ENJOY.....HOPEFULLY"
		self.drawBox(canvas)
		self.drawText(canvas)

	def drawChooseDiff(self,canvas):
		self.height = 180
		self.text = "* WELL..\n* TELL YOU THE TRUTH\n* EVEN ME, SOMETIMES...\n* CAN'T BEAT THE COMPUTER..."
		self.drawBox(canvas)
		self.drawText(canvas)

	def drawChooseColor(self,canvas):
		self.height = 180
		self.text = "* THE GOAL IS TO HAVE FIVE \n  STONES IN A ROW\n* TURN BASED\n* GET FIVE FAST TO WIN!"
		self.drawBox(canvas)
		self.drawText(canvas)