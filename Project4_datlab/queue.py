from container import Containor
class Queue(Containor):
    def __init__(self):
        super(Queue, self).__init__()

    def pop(self):
        assert not self.is_empty()
        return self.items.pop(0)

    def peek(self):
        assert not self.is_empty()
        return self.items[0]

if __name__ == '__main__':
    queue = Queue()
    queue.items = [1,2,3,4,5]
    while not queue.is_empty():
        print(queue.pop(), " was removed from the list \n")
        print("The remaining elements in the list are ", queue.items, "\n")

    for x in range(5):
        queue.push(x)

    peek = queue.peek()
    print(peek == queue.items[0])

