'''Moduk'''
class Containor:
    '''Container superclass'''
    def __init__(self):
        '''Constructor'''
        self.items = []
    def size(self):
        '''Size of the stack/queue'''
        return len(self.items)
    def is_empty(self):
        '''checks if the container is empty or not'''
        return len(self.items)==0
    def push(self, item):
        '''Pusesh an element to the containor'''
        self.items.append(item)
    def pop(self):
        '''Pushesh an element to the containor'''

    def peek(self):
        '''Retyrns the element on the top of the containor'''
