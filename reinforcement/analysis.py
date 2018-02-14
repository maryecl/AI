# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    #the discount factor determines the importance of future rewards 
    #a gamma = 0 will only care of the current reward
    #while a gamma approaching 1 cares about long term reward 

    #We reduce the answerNoise because we want to eliminate the probability of the agent going other way other than the bridge.
    #we leave the gamma high because we are looking toward the long term reward that is 10

    answerDiscount = 0.9
    answerNoise = 0.00

    return answerDiscount, answerNoise

def question3a():
    #not the safest way to a reward, but the fastest
    answerDiscount = 0.1
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    #If not possible:return 'NOT POSSIBLE'

def question3b():
    #In here we still want the closest reward, but going the way that cannot have a negative reward
    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    #We want to prioritize getting to the 10 value reward, so we have to augment the gamma
    #And we dont bother much about the risk of a negative reward 
    answerDiscount = 0.8
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    #We still prefer the 10 value reward, so the gamma stays big
    #But now we want to go the safest way 
    answerDiscount = 0.8
    answerNoise = 0.2
    answerLivingReward = 0.2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    #We want to avoid everything 
    #dont really care of the value of reward
    #half the time the agent will get to somewhere it did not intend to 
    answerDiscount = 0.3
    answerNoise = 0.5
    answerLivingReward = 10
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
