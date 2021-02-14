from container import Containor
class Stack(Containor):
    def __init__(self):
        super(Stack, self).__init__()

    def pop(self):
        assert not self.is_empty()
        return self.items.pop()

    def peek(self):
        assert not self.is_empty()
        return self.items[-1]
if __name__ == '__main__':
    stack = Stack()
    stack.items = [1,2,3,4,5]

    while not stack.is_empty():
        print(stack.pop(), " was removed from the list \n")
        print("The remaining elements in the list are ", stack.items, "\n")

    for x in range(5):
        stack.push(x)

    peek = stack.peek()
    print(peek == stack.items[-1])




