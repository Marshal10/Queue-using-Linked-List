class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
            
class Queue:
    def __init__(self):
        self.linkedList=LinkedList()
        
    def __str__(self):
        values=[str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self,value):
        newNode=Node(value)
        if self.linkedList.head is None:
            self.linkedList.head=self.linkedList.tail=newNode
        else:
            self.linkedList.tail.next=newNode
            self.linkedList.tail=newNode
        return "Succesfully added element to the queue"
    
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False
    
    def dequeue(self):
        popped_node=self.linkedList.head
        if self.linkedList.head==self.linkedList.tail:
            self.linkedList.head=self.linkedList.tail=None
        else:
            self.linkedList.head=self.linkedList.head.next
        return popped_node
        
    
customQueue=Queue()
print(customQueue.enqueue(10))
print(customQueue.enqueue(11))
print(customQueue.enqueue(12))
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.isEmpty())