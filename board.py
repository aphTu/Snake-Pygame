## playing board the snake
import pygame
import math
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
  # is the snake head currently in a valid square or not
  def validPosition(self, x, y, screenLength, screenWidth):
    actual_x = x/(screenLength/self.length)
    actual_y = y/(screenWidth/self.width)
    print(f"acutal_x:{actual_x}")
    print(f"actual_y: {actual_y}")
    # print(f"actual_x -0.3: {(actual_x-0.3).is_integer()}")
    # print(f"actual_x +0.3: {(actual_x+0.3).is_integer()}")
    # print(f"actual_y -0.3: {(actual_y-0.3).is_integer()}")
    # print(f"actual_y +0.3: {(actual_y+0.3).is_integer()}")
    # upper_x = math.ceil(actual_x) - 0.49
    # lower_x = math.floor(actual_x) + 0.49
    # upper_y = math.ceil(actual_y) + 0.5
    # lower_y = math.floor(actual_y) - 0.5
    # print(upper_x, lower_x, upper_y, lower_y)
    # print(f"x: {lower_x <= actual_x <= upper_x}")
    # print(f"y: {lower_y <= actual_y and actual_y <= upper_y}")
    # print(upper_y)
    # print(actual_y >= upper_y)
    # if (actual_x <= upper_x and actual_x >= lower_x) and (lower_y <= actual_y <= upper_y):
    return True
    return False



board = Board(9,7)
board.printBoard()