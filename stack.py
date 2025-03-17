class FixedSizeStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
    
    def push(self, item):
        if len(self.stack) >= self.max_size:
            print("Stack is overflow")  # Print overflow message
        else:
            self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            print("Stack is underflow")  #Print underflow message
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is underflow")  # Print underflow message
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def get_stack(self):
        return self.stack

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

stack1=FixedSizeStack(6)
stack2=Stack()
stack2.peek()
stack2.is_empty()
stack2.size()