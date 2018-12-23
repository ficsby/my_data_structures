class MyQueue(object):
    class QueueNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    
    def __init__(self):
        self.first = None
        self.last = None
    
    def isEmpty(self):
        return self.first == None

    
    def dequeue(self):
        if self.first == None:
            print("Nothing to pop")
            return
        else:
            removed = self.first
            self.first = self.first.next
            return removed

    def enqueue(self):
        new_entry = QueueNode(x)
        if self.first == None:
            self.first = self.last = new_entry
        else:
            self.last.next = new_entry

    def peek(self):
        return self.first.val
    