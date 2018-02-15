# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0



        #For each iteration, meaning  each exploration 
        #We will iterate thru the possible next states from our current state
        #Anf thru the possible Actions that we can take to get to this possible next states 
        #All this evaluation the Qvalue of each of them taking into account the transition functions
        #Once we compute the Qvalue of each action for a given state -> next state, we evaluate if its the best one 
        #So we will go exploring and choosing the best possible action to make from one state to another

        for i in range(self.iterations):
          action_values = util.Counter()
          for state in self.mdp.getStates():
            finalvalue = None
            for action in self.mdp.getPossibleActions(state):
              actionValue = self.computeQValueFromValues(state, action)
              if finalvalue == None or finalvalue < actionValue:
                finalvalue = actionValue
            if finalvalue == None:
              finalvalue = 0
            action_values[state]=finalvalue

          self.values = action_values 
    


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
       
        #we inicialize the q value  to 0 initially, because we have not explored anything
        #For each episode of exploration, we update the values of the map
        #For our current initial state we evaluate each of the next values and probs, and generate their qvalue
        #we will stop when our currentstate is the goal state

        Qvalue = 0
        transitions = self.mdp.getTransitionStatesAndProbs(state,action)
        for nextState,prob in transitions:
          reward = self.mdp.getReward(state,action,nextState)
          Qvalue+= prob*(reward + (self.discount * self.getValue(nextState)))
        return Qvalue
        util.raiseNotDefined()


    def computeActionFromValues(self, state):
    

        #If my current state and nextState are the same, we are in the terminal, so there are no more actions
        if self.mdp.isTerminal(state):
          return None 

        #We iterate thru all the possible actions of a state, evaluate the Qvalue of each of them
        #Choose the one with better policy, meaning we get the one with the best Qvalue, the one that leads us a reward!
        

        possible_actions = self.mdp.getPossibleActions(state)
        values_actions = util.Counter()
        for action in possible_actions:
          actionValue = self.computeQValueFromValues(state,action)
          values_actions[action] = actionValue

        return values_actions.argMax();



    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
