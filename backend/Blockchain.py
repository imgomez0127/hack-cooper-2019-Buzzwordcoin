class Node(object):
    
    def __init__(self,transactions,next=None):
        self.transactions = transactions
        self.next = next
