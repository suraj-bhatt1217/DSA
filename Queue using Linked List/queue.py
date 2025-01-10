class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
      
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None and self.rear is None

    def enqueue(self, new_data):
      
        new_node = Node(new_data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
      
        if self.is_empty():
            print("Queue Underflow")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def get_front(self):
      
        if self.is_empty():
            print("Queue is empty")
            return float('-inf')
        return self.front.data

    def get_rear(self):
      
        if self.is_empty():
            print("Queue is empty")
            return float('-inf')
        return self.rear.data

if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)

    print("Queue Front:", q.get_front())
    print("Queue Rear:", q.get_rear())

    q.dequeue()
    q.dequeue()

    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    q.dequeue()

    print("Queue Front:", q.get_front())
    print("Queue Rear:", q.get_rear())