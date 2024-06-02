################## Leetcode Submission ID -- https://leetcode.com/submissions/detail/1275555763/ ##########################

class Stack:
    def __init__(self):  
        self.objects = []  
        self._size = 0  

    def push(self, obj):  
        self.objects.append(obj)
        self._size += 1  

    def size(self):  
        return self._size  

    def is_empty(self):  
        return self._size == 0  

    def pop(self):  
        if self.is_empty():
            raise Exception("Stack is Empty")
        self._size -= 1  
        return self.objects.pop()

    def peek(self):  
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.objects[-1]

class MyQueue:
    def __init__(self):  
        self.s1 = Stack()  
        self.s2 = Stack()  

    def push(self, x: int) -> None:  
        self.s1.push(x)  

    def pop(self) -> int:  
        self.put_elements()  
        return self.s2.pop()  

    def peek(self) -> int:  
        self.put_elements()  
        return self.s2.peek()  

    def empty(self) -> bool:  
        return self.s1.is_empty() and self.s2.is_empty()  

    def put_elements(self):  
        if self.s2.is_empty():  
            while not self.s1.is_empty():  
                self.s2.push(self.s1.pop())
                


        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
