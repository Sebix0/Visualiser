

class StateManager:
  def __init__(self, currentState):
    self.currentState = currentState
    self.prevState = None

  def getState(self):
    return self.currentState

  def getPrevState(self):
    return self.getPrevState

  def setState(self, state):
    self.prevState = self.currentState
    self.currentState = state

  

   