# Q - Inserting an element in a Linkedlist , returning its size and checking wheather the list is empty or not !!  

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class FirstSLL:

    def __init__(self):
        self.head=None
        self._size=0

    def insert(self,index,data):
        if index<0 or index > self._size:
            raise IndexError("Index Out of Bound")
        
        inserted_node=Node(data)

        if index == 0:
            inserted_node.next=self.head ## This line links the inserted node(inserted at start) to the initial starting node !!
            self.head=inserted_node      ## This then point the head of the initial node to the inserted node !!

        else:
            current=self.head
            for i in range(index-1):
                current=current.next
            inserted_node.next=current.next
            current.next=inserted_node
            


        self._size+=1

    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size==0
    
    '''def printlinked(self):
        current=self.head
        for i in range(self._size):
            print(current.data,end=" ")
            current=current.next
        print()'''
    def __str__(self):
        elements=[]
        current=self.head
        while current:
            elements.append(current.data)
            current=current.next
        return ",".join(str(s) for s in elements)    
    
fssl=FirstSLL()
fssl.insert(0,1)
fssl.insert(1,2)
fssl.insert(2,3)
fssl.insert(3,4)
fssl.insert(2,2.1)
print(fssl)
'''fssl.printlinked()'''

print(fssl.size())
print(fssl.is_empty())



        




















