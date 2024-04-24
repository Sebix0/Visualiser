import pygame, Grid
from settings import *

class DFS: # do this after start menu
  def __init__(self, stateManager):
    self.stateManager = stateManager

    self.Grid = Grid.Grid(1000, 1000, cellSize)
    self.startSquare = None
    self.startSquareRect = None
    self.begin = False
    self.visited = []
    self.stack = []


  def logic(self):
    noNeighbours = True
    if self.begin and (len(self.visited) < self.Grid.size and len(self.stack) > 0):
      neighbours = self.Grid.getNeighbours(self.stack[-1])
      for i in neighbours:
        col, row = self.stack[-1][0], self.stack[-1][1]
        col += neighbours[i][0]
        row += neighbours[i][1]
        if not ((col, row) in self.visited or (col, row) in self.stack):
          self.stack.append((col, row))
          noNeighbours = False
        self.visited.append(self.stack[-1])
      if noNeighbours:
        self.stack.pop()


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
        self.stack = []

    if event.type == pygame.MOUSEBUTTONDOWN:
      self.startSquare = self.Grid.getSquare(pygame.mouse.get_pos())
      self.startSquareRect = pygame.Rect((self.startSquare[0]*self.Grid.cellSize + 2, self.startSquare[1] * self.Grid.cellSize + 2), (self.Grid.cellSize-1, self.Grid.cellSize - 1))
      self.stack.append(self.startSquare)
    

  def draw(self, win):
    win.fill((220, 220, 220))
    self.Grid.draw(win, (50, 50, 50))
    if self.startSquareRect != None:
      pygame.draw.rect(win, 'red', self.startSquareRect)
    for cell in self.visited:
      if cell == self.startSquare:
        continue
      elif cell in self.stack:
        pygame.draw.rect(win, 'chartreuse', pygame.Rect((cell[0]*self.Grid.cellSize + 2, cell[1] * self.Grid.cellSize + 2), (self.Grid.cellSize - 1, self.Grid.cellSize - 1)))
      else:
        pygame.draw.rect(win, 'violet', pygame.Rect((cell[0]*self.Grid.cellSize + 2, cell[1] * self.Grid.cellSize + 2), (self.Grid.cellSize - 1, self.Grid.cellSize - 1)))
    if len(self.stack) > 0:
      pygame.draw.rect(win, 'blue', pygame.Rect((self.stack[-1][0]*self.Grid.cellSize + 2, self.stack[-1][1] * self.Grid.cellSize + 2), (self.Grid.cellSize - 1, self.Grid.cellSize - 1)))
