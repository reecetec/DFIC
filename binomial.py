
#DEFINE A CLASS FOR A NODE
###################
#GENERATE THE NUMBER OF TIMESTEPS AS THE NUMBER OF DAYS TO MATURITY
###################

import math

#NODE CLASS REPRESENTS ONE NODE IN BINOMIAL TREE
class Node:
    def __init__(self, price, time):

        #input parameters
        self.price = price
        self.time = time

        #const values (maybe move to global?)
        self.up = 1.1
        self.down = 0.9
        self.rf = 0.12
        self.strike = 21
        self.optionPrice = 0

        #points to next nodes in tree
        self.upNode = None
        self.downNode = None

    #Print root node's stock and option price
    def printTree(self):
        print("Stock Price: " + str(self.price), "Option Price: " + str(self.optionPrice))
#        if self.upNode:
#            self.upNode.printTree()
#        if self.downNode:
#            self.downNode.printTree()

    #Traverse tree to bottom nodes, then generate a new up&down node
    #according to the input parameters 
    def generate(self):
        if self.upNode:
            self.upNode.generate()
        if self.downNode:
            self.downNode.generate()

        else:
            self.upNode = Node(self.price * self.up, self.time - 1)
            self.downNode = Node(self.price * self.down, self.time - 1)
            
    #recursively compute each option price at a given node
    #Method to compute each individual node found on slideshow
    def getCallOptionPrice(self):
        if self.upNode and self.downNode:
            p = (math.e**(self.rf * (self.time / 365)) - self.down) / (self.up - self.down)
            eTerm = math.e**(-1 * self.rf * self.time / 365)
            upTerm = p * (self.upNode.getCallOptionPrice())
            downTerm = (1-p) * (self.downNode.getCallOptionPrice())
            self.optionPrice = eTerm * (upTerm + downTerm)
        else:
            self.optionPrice = self.price - self.strike 

            if self.optionPrice < 0:
                self.optionPrice = 0

        return self.optionPrice

root = Node(20, 20)
for i in range(20):
    root.generate()
root.getCallOptionPrice()
root.printTree()

#ISSUES / IMPROVE:
# -> 30 TIME STEPS TAKE A LONG TIME / DOESNT COMPUTE
#       -> move const values to global variables => less memory taken up
#       -> remove temp variables ? => less memory
#       -> change time from daily time to weekly/monthly time
#           -> allows for less timesteps in model

#TIMES WHICH WORK..
# -> 20 time steps computes within 3-5 seconds


