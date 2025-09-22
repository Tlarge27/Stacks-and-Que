# Implement your Node class here
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

#Line 4 is to store the customer name, line 5 is to point towards the next name in the queue 

# In this project I build two different custom lists, one being a stack and the other being a customer queue. 
# For the undo/redo system I used a stack because it's whats called a LIFO. Since the last thing entered in would be the thing I want to remove, 
# Last in first out works best for this. Each time a user performs an action, it is added to the top of the undo stack. 
# If the user chooses to undo, the action is removed from the undo stack and placed on a redo stack. 
# Redoing an action moves it back from the redo stack to the undo stack. 
# Doing is this way makes sure than everything is done in the correct order, like in actual applications 
#
# For the Help Desk system, a queue was the best choice because it works on a First-In, First-Out (FIFO) principle. 
# Customers are added to the back of the queue when they arrive, and the next customer to be helped is always taken from the front. 
# This makes sure that everyone is served in the order they arrived, which is fair and practical. At my office this priciple is used for ticketing and inventory management purposes.
# 
# my stack and queue use nodes and pointers. 
# Each element points to the next one, which makes adding or removing items fast and easy.
# Using nodes also shows how these data structures work under the hood, which helps to understand the principles of stacks and queues and how they are used in real programs.
#
#
#
#
#
