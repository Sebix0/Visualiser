import pygame

class Grid: #create this later after creating a functional start menu
  def __init__(self, width, height, cellSize):
    self.width = width
    self.height = height
    self.size = width*height
    self.cellSize = cellSize
    self.Grid = [0 for i in range(self.size)]

  def getNeighbours(self, pos):
    directions = {
      'left': (-1, 0), 
      'up': (0, -1), 
      'right': (1, 0), 
      'down': (0, 1)   
    }
    x,y = pos
    if x == 0:
      del directions['left']
    elif x == self.width//self.cellSize:
      del directions['right']

    if y == 0:
      del directions['up']
    elif y == self.height//self.cellSize:
      del directions['down']

    return directions
    
  def getSquare(self, pos):
    mx, my = pos
    x, y = mx//self.cellSize, my//self.cellSize
    return (x, y)


  def draw(self, win, lineColor):
    for row in range(self.height//self.cellSize):
      pygame.draw.line(win, lineColor, (0, row * self.cellSize + 1), (self.width, row * self.cellSize + 1))
    for col in range(self.width//self.cellSize):
      pygame.draw.line(win, lineColor, (col * self.cellSize + 1, 0), (col * self.cellSize + 1, self.height))
