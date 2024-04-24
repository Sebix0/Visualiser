import pygame, Grid
from settings import *

class BFS:
  def __init__(self, stateManager):
    self.stateManager = stateManager

    self.Grid = Grid.Grid(1000, 1000, cellSize)
    self.startSquare = None
    self.startSquareRect = None
    self.begin = False
    self.visited = []
    self.queue = []

  def logic(self):
    if self.begin and (len(self.visited) < self.Grid.size and len(self.queue) > 0):
      neighbours = self.Grid.getNeighbours(self.queue[0])
      for i in neighbours:
        col, row = self.queue[0][0], self.queue[0][1]
        col += neighbours[i][0]
        row += neighbours[i][1]
        if not ((col, row) in self.visited or (col, row) in self.queue):
          self.queue.append((col, row))
      self.visited.append(self.queue[0])
      self.queue.pop(0)

  def eventHandler(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        self.stateManager.setState(self.stateManager.prevState)
      
      if event.key == pygame.K_RETURN and self.startSquare != None:
        self.begin = not self.begin

      if event.key == pygame.K_ESCAPE and self.begin:
        self.startSquare = None
        self.startSquareRect = None
        self.begin = False
        self.visited = []
        self.queue = []
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.startSquare = self.Grid.getSquare(pygame.mouse.get_pos())
      self.startSquareRect = pygame.Rect((self.startSquare[0]*self.Grid.cellSize+2, self.startSquare[1] * self.Grid.cellSize+2), (self.Grid.cellSize-1, self.Grid.cellSize-1))
      self.queue.append(self.startSquare)
    

  def draw(self, win):
    win.fill((50, 50, 50))
    self.Grid.draw(win, (220, 220, 220))
    if self.startSquareRect != None:
      pygame.draw.rect(win, 'red', self.startSquareRect)
    for cell in self.visited:
      if cell == self.startSquare:
        continue
      elif len(self.queue) > 0 and self.queue[0]:
        pygame.draw.rect(win, 'blue', pygame.Rect((cell[0]*self.Grid.cellSize + 2, cell[1] * self.Grid.cellSize + 2), (self.Grid.cellSize - 1, self.Grid.cellSize - 1)))  
      pygame.draw.rect(win, 'violet', pygame.Rect((cell[0]*self.Grid.cellSize + 2, cell[1] * self.Grid.cellSize + 2), (self.Grid.cellSize - 1, self.Grid.cellSize - 1)))
    
    