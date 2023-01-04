'''This file is the stack ADT'''
class Stack:
    ''' This class can be used to work with data efficiently'''
    def __init__(self):
        self.items = []

    def push(self,item):
        '''Add and item to the top of the stack'''
        self.items.append(item)

    def pop(self):
        '''Remove and item from the End of the stack'''
        if self.size() > 0:
            result = self.items.pop()
        else:
            raise IndexError
        return result

    def top(self):
        '''View the top of the stack. Similar to peek'''
        if self.size() > 0:
            return self.items[-1]
        raise IndexError

    def size(self):
        '''Return the current size of the stack'''
        return len(self.items)

    def clear(self):
        '''Clear the stack'''
        self.items = []

    def isEmpty(self):
        '''Return a boolean value on whether the stack is empty'''
        if self.items == []:
            return True
        return False
