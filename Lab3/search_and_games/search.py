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
import sys
import copy

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

    def goalTest(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """        
        util.raiseNotDefined()

    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """
        util.raiseNotDefined()

    def getCost(self, state, action):
        """
        Given a state and an action, returns step cost, which is the incremental cost 
        of moving to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    """
    Search node object for your convenience.

    This object uses the state of the node to compare equality and for its hash function,
    so you can use it in things like sets and priority queues if you want those structures
    to use the state for comparison.

    Example usage:
    >>> S = Node("Start", None, None, 0)
    >>> A1 = Node("A", S, "Up", 4)
    >>> B1 = Node("B", S, "Down", 3)
    >>> B2 = Node("B", A1, "Left", 6)
    >>> B1 == B2
    True
    >>> A1 == B2
    False
    >>> node_list1 = [B1, B2]
    >>> B1 in node_list1
    True
    >>> A1 in node_list1
    False
    """
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return self.state != other.state


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def getSolutionPath(currentNode, startNode):
    # traverse up from goal node to initial node
    solutionPath = [];
    
    while (currentNode != startNode):
        solutionPath.append(currentNode.action)
        currentNode = currentNode.parent

    print(solutionPath)
    print(list(reversed(solutionPath)))
    return list(reversed(solutionPath))

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"
   
    visitedStates = []
    startState = problem.getStartState()
    startNode = Node(startState, None, None, 0)
    # queue should contain nodes, not state
    frontier = util.Queue()
    frontier.push(startNode)
  
   
    # may enter infinite loop is you do while (not problem.isGoal()):"
    while (not frontier.isEmpty()):
        currentNode = frontier.pop()
       
        "first check is node.state has been visited"
        if (currentNode.state not in visitedStates):
            # add currentNode to visitedStates
            visitedStates.append(currentNode.state)
           
            # first check if at goal node
            if(problem.goalTest(currentNode.state)):
                # traverse from goal node to initial node and reverse
                return getSolutionPath(currentNode, startNode) 
           
            # expand this node, generate successors + enter frontier queue
            actionsList = problem.getActions(currentNode.state)
           
            for action in actionsList:
                nextState = problem.getResult(currentNode.state, action)
                nextCost = problem.getCost(currentNode.state, action) + currentNode.path_cost
                nextNode = Node(nextState, currentNode, action, nextCost)
                frontier.push(nextNode)

    
def depthFirstSearch(problem): 

    "*** YOUR CODE HERE ***"   
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth. Begin with a depth of 1 and increment depth by 1 at every step.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.goalTest(problem.getStartState()))
    print("Actions from start state:", problem.getActions(problem.getStartState()))

    Then try to print the resulting state for one of those actions
    by calling problem.getResult(problem.getStartState(), one_of_the_actions)
    or the resulting cost for one of these actions
    by calling problem.getCost(problem.getStartState(), one_of_the_actions)

    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    
def UniformCostSearch(problem):
    """Search the node that has the lowest path cost first."""
    "*** YOUR CODE HERE ***"  
    util.raiseNotDefined()

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    visitedStates = []
    startState = problem.getStartState()
    startNode = Node(startState, None, None, 0)
    Frontier = util.PriorityQueue()
    Frontier.push(startNode, 0)
    
    while(not Frontier.isEmpty()):
        currentNode = Frontier.pop()
        
        if (problem.goalTest(currentNode.state)):
            return getSolutionPath(currentNode, startNode)
        
        actionsList = problem.getActions(currentNode.state)
        
        for action in actionsList:
            nextState = problem.getResult(currentNode.state, action)
            nextCost = (problem.getCostOfActions(getSolutionPath(currentNode, startNode))
                          + heuristic(nextState, problem))
            nextNode = Node(nextState, currentNode, action, nextCost)
            if (nextState not in visitedStates or problem.getCostOfActions(getSolutionPath(nextNode, startNode)) > nextCost):
                visitedStates.append(nextState)
                Frontier.push(nextNode, nextCost)
            
            
            
    '''node = problem.getStartState()
    Frontier = util.PriorityQueue()
    Frontier.push(node, 0)
    
    Visited = {}
    Visited[node] = 0
    paths = {}
    paths[node] = []
   
    while not Frontier.isEmpty():
        node = Frontier.pop()
        if problem.goalTest(node):
            return paths[node]
        for act in problem.getActions(node):
            child = problem.getResult(node, act)
            cost_child = problem.getCostOfActions(paths[node]+[act]) + heuristic(child, problem)
            if child not in Visited or Visited[child] > cost_child:
                paths[child] = paths[node]+[act]
                Visited[child] = cost_child
                Frontier.push(child, cost_child)'''
                        

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
