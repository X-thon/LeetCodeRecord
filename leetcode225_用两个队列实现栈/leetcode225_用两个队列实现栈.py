from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.queue1.empty():
            self.queue2.put(x)
        elif self.queue2.empty():
            self.queue1.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue1.empty() and self.queue2.empty():
            return
        if not self.queue1.empty():
            while self.queue1.qsize() != 1:
                self.queue2.put(self.queue1.get())
            return self.queue1.get()
        if not self.queue2.empty():
            while self.queue2.qsize() != 1:
                self.queue1.put(self.queue2.get())
            return self.queue2.get()
        
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue1.empty() and self.queue2.empty():
            return
        if not self.queue1.empty():
            while self.queue1.qsize() != 1:
                self.queue2.put(self.queue1.get())
            top = self.queue1.get()
            self.queue2.put(top)
            return top
        if not self.queue2.empty():
            while self.queue2.qsize() != 1:
                self.queue1.put(self.queue2.get())
            top = self.queue2.get()
            self.queue1.put(top)
            return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.queue1.empty() and self.queue2.empty():
            return True
        else:
            return False
        