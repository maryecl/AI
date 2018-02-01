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
    stack = util.Stack() # we create a Stack, empty
    visited =[] # a list for visited nodes
    stack.push((problem.getStartState(),[]))#here we add first/start node to Stack
    while not stack.isEmpty():#while our stack is not empty
        actualstate,path=stack.pop()#returns us the most upper node of the stack and removes it
        if problem.isGoalState(actualstate):#we check if the state we are is the goal of the problem or not
                return path#if the node is the goal, then we return the path to get to that node
        if actualstate in visited:#if not the goal and is already visited, we continue and
            continue
        visited.append(actualstate)
        for successors in problem.getSuccessors(actualstate):#we are in actual node, which has some adjacent nodes to him
            newstate = successors[0] #the actual node
            newpath = successors[1]#the new path to get to the newnode
            if newstate not in visited:#we check if the current node has been visited or not
            #if not visited, we add the currentnode to the stack
                stack.push( (newstate, path + [newpath]) )

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue= util.Queue()#first we create a empty queue
    visited =[]#empty list
    queue.push((problem.getStartState(),[]))#we add first node to the queue
    while not queue.isEmpty():#while the queue is not empty
        actualstate, path = queue.pop()#we take the last item in the list and after that we remove it
        print(actualstate, path)
        if problem.isGoalState(actualstate):#and if this state is the goal
            print(path)
            return path #we return the path to this node
        if actualstate in visited: #if this node has been visited, then we continue
            continue
        visited.append(actualstate)
        for successor in problem.getSuccessors(actualstate): #we get the successors of the currentnode and iterate them
            newstate = successor[0]#new state
            newpath = successor[1]# the path to this new state
            if newstate not in visited:#if this current node has not been visited, we push it to the queue
                queue.push( (newstate, path + [newpath]) )

def uniformCostSearch(problem):#DIJKSTRA
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    """f(n)=g(n)"""
    queue = util.PriorityQueue()#we create a PriorityQueue because we want to work with compared costs
    visited = []#empty list
    queue.push((problem.getStartState(), [], 0), 0)#we add first/start node
    while not queue.isEmpty():#while the queue in not empty
        actualstate, path, actualcost = queue.pop()#now we are working with three attributes,
        #such as the actual node, the path we take and how much this path costs
        if problem.isGoalState(actualstate):#we compare if the actualstate is our goal
            return path#if it is the goal, return the path to that node
        if actualstate in visited:#if node in visited, we continue
            continue
        visited.append(actualstate)
        for state, newpath, cost in problem.getSuccessors(actualstate):#we have three parametres that we have to take into account
            if state not in visited:#is the state not in visited we have to add it
                queue.push((state, path + [newpath], actualcost + cost), actualcost + cost)#we add the node to the queue
                #here in cost we acummulate the previous cost and the newest one

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    """f(n)=g(n)+h(n)"""

    queue = util.PriorityQueue()#We create a PriorityQueue to compare different costs
    visited = []#then we create an empty list for visited nodes
    queue.push((problem.getStartState(), [], 0), 0)#we add start node to que queue
    while not queue.isEmpty():#while the queue is not empty
        actualstate, path, actualcost = queue.pop()#now we are working with three attributes,
        #such as the actual node, the path what we made and how much this path costs
        if problem.isGoalState(actualstate):#we compare if the actualstate is our goal
            return path#if it is,  we return the path that we used to arrive
        if actualstate in visited:
            continue
        visited.append(actualstate)
        for state, direction, cost in problem.getSuccessors(actualstate):#for loop to iterate the three parametres that we have
            if state not in visited:#if the node we are is no in visited
                heuristicCost = heuristic(state, problem)#we add the heuristic cost
                queue.push((state, path + [direction], actualcost + cost ), actualcost + cost+heuristicCost )#we add the non viisted node to the queue with acumulated cost if it is needed


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
