# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print "*********************"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    stack = util.Stack() # we create a Stack, empty
    visited =[] # a list for visited nodes, an empty array
    stack.push((problem.getStartState(),[]))#here we add first/start node to Stack
    while not stack.isEmpty():
        state,actions=stack.pop()#returns us the most upper node of the stack and after removes it
        for successors in problem.getSuccessors(state):#we are in some node, which has some adjacent nodes to him
            state = successors[0] #the actual node, where we are now
            direction = successors[1]#the node adjacent to the actual node, the node where we have to go next
            if state not in visited:#we check if the node we are is already visited or not
                if problem.isGoalState(state):#we check if the state we are is the goal of the problem or not
                    return actions + [direction]#if we are in the last node-goal, we have to retrun
                else:#if not we have to add visited nodes to our list,and to the stack
                    stack.push( (state, actions + [direction]) )
                    visited.append( state )
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue= util.Queue()
    close =[]
    queue.push((problem.getStartState(),[]))
    while not queue.isEmpty():
        state, actions = queue.pop()
        for i in problem.getSuccessors(state):
            state = i[0]
            direction = i[1]
            if state not in close:
                if problem.isGoalState(state):
                    return actions + [direction]
                else:
                    queue.push( (state, actions + [direction]) )
                    close.append( state )

    util.raiseNotDefined()

def uniformCostSearch(problem):#DIJKSTRA
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    visited = []
    queue.push((problem.getStartState(), [], 0), 0)
    while not queue.isEmpty():
        currentState, currentPath, currentCost = queue.pop()
        if problem.isGoalState(currentState):
            return currentPath
        for state, direction, cost in problem.getSuccessors(currentState):
            if state not in visited:
                queue.push((state, currentPath + [direction], currentCost + cost), currentCost + cost)
                visited.append(state)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
