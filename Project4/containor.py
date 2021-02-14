class Containor:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items)==0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        pass
    def peek(self):
        pass