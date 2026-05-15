## playing board the snake
import pygame
class Board():
  def __init__(self, width, length):
    self.width = width
    self.length = length
    self.rectangle = [[1 for _ in range(length)] for _ in range(width)]
  
  def printBoard(self):
  
    for i in range(self.length):
      print("|  ", end="")
      for j in range(self.width):
        print(f"{self.rectangle[j][i]} ", end="")
      print(" |", end="")
      print("")
  
  def initBoard(self, screenWidth, screenLength, screen):
    color = (0,255,0)
    for i in range(self.length):
     
      for j in range(self.width):
        if color != (0,255,0):
          color = (0,255,0)
        else:
          color = (0,102,0)
        # print(screenLength/self.length)
        # print(f"Drawing at {screenLength/self.length * i, screenWidth/self.width * j}")
        pygame.draw.rect(screen,color,pygame.Rect(screenLength/self.length * i, screenWidth/self.width * j, screenLength/self.length, screenWidth/self.width))
 



board = Board(9,7)
board.printBoard()