class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
        
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            self.head.next=None
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
                
    def add_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        
    def add_aftervalue(self,data,x):
        new_node=node(data)
        current=self.head
        while current:
            if current.data==x:
                new_node.next = current.next  # Link new node to the next of the current node
                current.next = new_node  # Link current node to the new node
                return
            current = current.next
        print(f"{x} is not found in linked list !")        

    def deleteby_value(self,x):
        current=self.head
        previous=None
        
        if current is None:
            print('linked list is empty !')                
            return
        while current:
            if current.data == x:  # Node to be deleted found
                if previous is None:  # Node is head
                    self.head = current.next  # Update head
                else:
                    previous.next = current.next  # Bypass the current node
                return  # Exit after deletion
            previous = current  # Move previous to current
            current = current.next  # Move to the next node
        
        print(f"Value {x} not found in the list.")
 

    def printlist(self):
        current=self.head
        if not current:
            print('linked list is empty!')
        else:
            print('linked list have the values !')
            while current:
                print(current.data,end=' - ')
                current=current.next
            print("\n \t successfully executed !")

                 


a=linked_list()

a.add_begin(40)

a.add_end(30)
a.add_end(20)
a.add_end(10)
a.add_aftervalue(5,200)

a.printlist()
a.deleteby_value(10)

a.printlist()
