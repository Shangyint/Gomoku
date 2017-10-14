run main.py to start the game

#music will not work in Apple devices as I use winsound module (build in)

This is a solved game, which means black can win whatever how hard the white tries. 
However, actually solve this game may be extremely hard due to the massive data. 

To solve the problem, I used DFS algorithm and minimax algorithm 
to help my AI to make decision (of course, a grading function will be used to analyze the
board and return a score of each condition). 

I have several classes: 
Game: controls the game, take turns and help computer to make decision
Board: keeps track of the board, can also draw the board
StartScreen: draws the start screen and records the players input
DrawDia: infomation box drawing and processing

gomoku controlling file (tkinter)