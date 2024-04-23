import pygame, heading
from settings import *


class Menu:
  def __init__(self, stateManager):
    self.stateManager = stateManager
    
    self.startDFS = heading.Heading('Depth First Search', (0, -200), (500, 1200), 48)
    self.startBFS = heading.Heading('Breadth First Search', (500, 0), (500, 1200), 48)
  
  def logic(self):
    if self.startDFS.hover():
      if self.startDFS.bgColor == None:
        self.startDFS.bgColor = (139, 195, 74)
    else:
      if self.startDFS.bgColor == (139, 195, 74):
        self.startDFS.bgColor = None
    if self.startBFS.hover():
      if self.startBFS.bgColor == None:
        self.startBFS.bgColor = (240, 98, 146)
    else:
      if self.startBFS.bgColor == (240, 98, 146):
        self.startBFS.bgColor = None

  def eventHandler(self, event):
    if self.startDFS.onClick(event):
      self.stateManager.setState('DFS')
    if self.startBFS.onClick(event):
      self.stateManager.setState('BFS')

  def draw(self, win):
    win.fill((200, 200, 200))
    self.startDFS.drawHeading(win)
    self.startBFS.drawHeading(win)