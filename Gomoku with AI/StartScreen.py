from tkinter import *
import time
import random
import winsound


class StartScreen:


	def __init__(self,width,height,data):
		winsound.PlaySound('01 Once Upon a Time.wav', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
		self.canvas = data.canvas
		self.width = width
		self.height = height
		self.player1 = "human"
		self.isStart = False
		self.chooseOppo = False
		self.chooseColor = False
		self.fontSize = 300	
		self.isOver = False
		self.info = []
		self.textcolor = True
		self.isChooseDiffcult = False
		self.mode = 0
		
	def keyPressedWrapper(self,event):
		if event.keysym == "Return" and self.isStart == False:
			self.chooseOppo = True
			self.isStart = True		

	def mousePressedWrapper(self,event):
		if self.chooseOppo == True:
			if event.x<self.width/2:
				self.player2 = "human"
			elif event.x>self.width/2:
				self.player2 = "computer"
			self.chooseOppo = False
			self.chooseColor = True
			return
		if self.chooseColor == True:
			if event.x<self.width/2:
				self.player2,self.player1 = self.player1,self.player2
			self.info = [(self.player1,"black"),(self.player2,"white")]
			if self.player1 == 'computer' or self.player2 == 'computer':
				self.isChooseDiffcult = True
				self.chooseColor = False
			else:
				self.isChooseDiffcult = False
				self.isOver = True
			return
		if self.isChooseDiffcult:
			if event.x<self.width/2:
				self.mode = 1
			else:self.mode = 2
			self.info.append(self.mode)
			self.isOver = True


			#self.canvas.delete(ALL)

	def drawEverything(self):
		if self.isStart == False:
			self.drawStartScreening()
		elif self.chooseOppo:
			self.drawChoicePage()
		elif self.chooseColor:
			self.drawChoiceColorPage()
		elif self.isChooseDiffcult:
			self.drawDiffcultPage()


	def drawChoicePage(self):

		self.canvas.create_rectangle(0,0,self.width/2,self.height,fill = "white")
		self.canvas.create_rectangle(self.width/2,0,self.width,self.height,fill = "black")
		# self.canvas.create_text(self.width/2,30,text = "click to choos",anchor = E,fill = "black",font = ("Fixedsys", 25))
		# self.canvas.create_text(self.width/2,30,text = "e your opponent",anchor = W,fill = "white",font = ("Fixedsys", 25))
		self.canvas.create_text(50,self.height/2,text = "Human", fill = "black",anchor = W,font = ("Fixedsys", 40))
		self.canvas.create_text(self.width/4,self.height/2+35,text = """ Yes\n I have a friend play with me""", fill = "black",font = ("Fixedsys", 8))		
		self.canvas.create_text(self.width/4*3,self.height/2,text = "Computer", fill = "white",font = ("Fixedsys", 40))
		self.canvas.create_text(self.width/4*3,self.height/2+35,text = """ Damn\n I need to play with computer""", fill = "white",font = ("Fixedsys", 8))
		# self.canvas.create_text(self.width/2,60,text = "check the ru",anchor = E,fill = "black",font = ("Fixedsys", 25))
		# self.canvas.create_text(self.width/2,60,text = "le online :)",anchor = W,fill = "white",font = ("Fixedsys", 25))


	def drawStartScreening(self):
		self.canvas.create_rectangle(0,0,self.width,self.height,fill = "black")	

		self.canvas.create_text(self.width/2,self.height/3,text = 'GOMOKU', font = ('Courier',self.fontSize,'bold'),fill = "white")
		if self.textcolor:
			fill = "white"
		else: fill = "black"
		self.canvas.create_text(self.width/2,self.height*2/3,text = 'Press enter to start', font = ('Fixedsys',15), fill = fill)
		

	def	drawChoiceColorPage(self):
		self.canvas.create_rectangle(0,0,self.width/2,self.height,fill = "black")
		self.canvas.create_rectangle(self.width/2,0,self.width,self.height,fill = "white")
		# self.canvas.create_text(self.width/2,30,text = "click to choos",anchor = E,fill = "black",font = ("Fixedsys", 25))
		# self.canvas.create_text(self.width/2,30,text = "e your opponent",anchor = W,fill = "white",font = ("Fixedsys", 25))
		self.canvas.create_text(50,self.height/2,text = "White", fill = "white",anchor = W,font = ("Fixedsys", 40))
		self.canvas.create_text(self.width/4,self.height/2+35,text = """ Oh!\n I'm good at defense      """, fill = "white",font = ("Fixedsys", 8))		
		self.canvas.create_text(self.width/4*3,self.height/2,text = "Black    ", fill = "Black",font = ("Fixedsys", 40))
		self.canvas.create_text(self.width/4*3,self.height/2+35,text = """ Attack\n Take turn first and ATTACKKKKK""", fill = "black",font = ("Fixedsys", 8))
		# self.canvas.create_text(self.width/2,60,text = "check the ru",anchor = E,fill = "black",font = ("Fixedsys", 25))
		# self.canvas.create_text(self.width/2,60,text = "le online :)",anchor = W,fill = "white",font = ("Fixedsys", 25))

	def drawDiffcultPage(self):
		self.canvas.create_rectangle(0,0,self.width/2,self.height,fill = "white")
		self.canvas.create_rectangle(self.width/2,0,self.width,self.height,fill = "black")
		# self.canvas.create_text(self.width/2,30,text = "click to choos",anchor = E,fill = "black",font = ("Fixedsys", 25))
		# self.canvas.create_text(self.width/2,30,text = "e your opponent",anchor = W,fill = "white",font = ("Fixedsys", 25))
		self.canvas.create_text(50,self.height/2,text = "  Easy", fill = "black",anchor = W,font = ("Fixedsys", 40))
		self.canvas.create_text(self.width/4,self.height/2+35,text = """ Easy, and \n he doesn't even think in the game""", fill = "black",font = ("Fixedsys", 8))		
		self.canvas.create_text(self.width/4*3,self.height/2,text = "Hard", fill = "white",font = ("Fixedsys", 40))
		self.canvas.create_text(self.width/4*3,self.height/2+35,text = """ Hard, but \n he needs more time to make decision""", fill = "white",font = ("Fixedsys", 8))
		# self.canvas.create_text(self.width/2,60,text = "check the ru",anchor = E,fill = "black",font = ("Fixedsys", 25))
		# self.canvas.create_text(self.width/2,60,text = "le online :)",anchor = W,fill = "white",font = ("Fixedsys", 25))
