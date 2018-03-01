# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition() #It returns pacmans next position 
        newFood = successorGameState.getFood()  # it gives us the position from the successors state to the food
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        #If the next state is the  winning state that means that the game ends
        if successorGameState.isWin():
          return float("inf")

        #Now we obtain the distance to the closest ghost
        #If the agent index is >=1 it means its a Ghost, so we compute the distance from our
        #next position to the nearest ghost from pacman current position

        ghostDist = util.manhattanDistance(newPos, currentGameState.getGhostPosition(1))
        if ghostDist <= 1:
          ghostDist = -200

        #We add the substracting values to the score we had obtained until now 
        score = ghostDist + successorGameState.getScore()

        food = newFood.asList()
        foodDist = float("inf") 


        #For each food we compute the distance from our New position to the food 
        for f in food:
          dist = util.manhattanDistance(f, newPos)
          if dist < foodDist:
            foodDist = dist
        score -=  3 * foodDist  #given that, as we move we substract points, its better if we are near the food 

        #When pacman eats a Capsule, it get an positive addition to the score 
        capsulePos = currentGameState.getCapsules()
        if newPos in capsulePos:
          score += 210

        #If I have more food on my current state that in my successor state, it means I ate food 
        if currentGameState.getNumFood() > successorGameState.getNumFood():
          score += 200


        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        action, value = self.maximizer(gameState, self.depth)

        return action 

    def maximizer(self,gameState,depth):

      # Either if we have won, lost, then we return the score, or we are in the very beggining
        if gameState.isWin() or gameState.isLose() or depth==0:
          return None, self.evaluationFunction(gameState)

        #Our initial worst  worst maximum value is -infinity or a really small value
        value = -100000000

      # For each action in the legalActions from our gameState 
      # We search for the action that maximizes the score from our pacman
      # For each action we call the minimizer function with its successors and depth correspondent

        for action in gameState.getLegalActions(0):
          a,v = self.minimizer(gameState.generateSuccessor(0,action), depth, 1)
          if v > value:
              baction = action
              value = v
        return baction, value



    def minimizer(self, gameState,depth, ghost):

      # Either if we have won, lost, then we return the score, or we are in the very beggining
        if gameState.isWin() or gameState.isLose() or depth ==0:
            return None,self.evaluationFunction(gameState)

        #Our initial worst  worst minimum value is infinity or a really big value
        value = 100000000

      # For each action available in our list of legal action of our current state
      # We will compare each ghosts and return the minimum of them 
      # When there are NO more ghosts then we maximize the pacman
      
        for action in gameState.getLegalActions(ghost):
          if ghost == gameState.getNumAgents()-1:
            a, v = self.maximizer(gameState.generateSuccessor(ghost, action), depth - 1)
          else:
            a, v = self.minimizer(gameState.generateSuccessor(ghost, action), depth, ghost + 1)
          if v < value:
              baction = action
              value = v
        return baction, value




class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
  

        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        
        action,value = self.maximizer(gameState, self.depth, -100000000, 100000000)

        return action
   
    def maximizer(self,gameState,depth, alpha, betha):

      # Either if we have won, lost, then we return the score, or we are in the very beggining
        if gameState.isWin() or gameState.isLose() or depth==0:
          return None, self.evaluationFunction(gameState)

      #Our initial worst  worst maximum value is -infinity or a really small value
        value = -100000000


        for action in gameState.getLegalActions(0):
          a,v = self.minimizer(gameState.generateSuccessor(0,action), depth, 1, alpha, betha)
          if v > value:
            baction = action
            value = v     
          # If our actual value is greater than betha, then you are winning, so break 
          if value > betha:
            break
          #Then we choose the maximum value between out existent alpha and our value
          alpha = max(alpha, value)
        return baction, value 
      

    def minimizer(self, gameState, depth, ghost, alpha, betha):
      

      # Either if we have won, lost, then we return the score 
        if gameState.isWin() or gameState.isLose() or depth==0:
          return None, self.evaluationFunction(gameState)

      #Our initial worst  worst minimum value is +infinity, or a really big value
        value = 100000000

        for action in gameState.getLegalActions(ghost):
          if ghost == gameState.getNumAgents()-1:
              a,v = self.maximizer(gameState.generateSuccessor(ghost,action), depth - 1, alpha, betha)
          else:
              a,v = self.minimizer(gameState.generateSuccessor(ghost,action), depth, ghost + 1, alpha, betha)
          if v < value:
              baction = action 
              value = v
        #If our actual value is smaller that alpha, then 
          if value < alpha:
              break
        #Then we choose the minimum value from the current betha and our value
          betha = min(betha, value)
        return baction, value
        


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

