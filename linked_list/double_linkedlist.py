print("----------double linked list----------")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class double_linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        current=self.head
        if current is None:
            print("linked list is empty!")
        else:
            while current:
                print(current.data,end=" - ")
                current=current.next

    def addbegin(self,data):
        new_node=node(data)
        current=self.head
        if current is None:
            current=new_node
            current.prev=None
            current.next=None
        else:
            new_node=current.prev
            
a=double_linkedlist()
a.addbegin(10)
a.printlist()