
#DEFINE A CLASS FOR A NODE
###################
#GENERATE THE NUMBER OF TIMESTEPS AS THE NUMBER OF DAYS TO MATURITY
###################

import math

#NODE CLASS REPRESENTS ONE NODE IN BINOMIAL TREE


#CONST PARAMETERS
UP = 1.1
DOWN = 0.9
RISK_FREE = 0.12
STRIKE = 21
TIME_STEP = 12 #i.e. 12 months in a year 365 days in a year etc.

class Node:
    def __init__(self, price, time):

        #input parameters
        self.price = price
        self.time = time

        self.optionPrice = 0

        #points to next nodes in tree
        self.upNode = None
        self.downNode = None

    #Print root node's stock and option price
    def printTree(self):
        print("Stock Price: " + str(self.price), "Option Price: " + str(self.optionPrice))
        if self.upNode:
            self.upNode.printTree()
        if self.downNode:
            self.downNode.printTree()

    #Traverse tree to bottom nodes, then generate a new up&down node
    #according to the input parameters 
    def generate(self):
        if self.upNode:
            self.upNode.generate()
        if self.downNode:
            self.downNode.generate()

        else:
            self.upNode = Node(self.price * UP, self.time - 1)
            self.downNode = Node(self.price * DOWN, self.time - 1)
            
    #recursively compute each option price at a given node
    #Method to compute each individual node found on slideshow
    def getCallOptionPrice(self):
        if self.upNode and self.downNode:
            p = (math.e**(RISK_FREE* (self.time / TIME_STEP)) - DOWN) / (UP - DOWN)
            print(p)
            eTerm = math.e**(-1 * RISK_FREE * self.time / TIME_STEP)
            upTerm = p * (self.upNode.getCallOptionPrice())
            downTerm = (1-p) * (self.downNode.getCallOptionPrice())
            self.optionPrice = eTerm * (upTerm + downTerm)
        else:
            self.optionPrice = self.price - STRIKE

            if self.optionPrice < 0:
                self.optionPrice = 0

        return self.optionPrice


root = Node(20, 3)
for i in range(1):
    root.generate()
root.getCallOptionPrice()
root.printTree()




