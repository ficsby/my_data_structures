class MyStack(object):
    class StackNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None

    
    def pop(self):
        if self.top == None:
            print("Nothing to pop")
            return
        else:
            removed = self.top
            self.top = self.top.next
            return removed

    def push(self, x):
        new_entry = StackNode(x)
        if self.top == None:
            self.top = new_entry
        else:
            new_entry.next = self.top
            self.top = new_entry

    def peek(self):
        return self.top.val
    