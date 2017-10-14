from tkinter import * 

class Window(object):
	def __init__(self,width,height):
		self.root = Tk()
		self.root.title("Gomoku, you gonna enjoy it")

	def quit(self):
		self.root.destroy