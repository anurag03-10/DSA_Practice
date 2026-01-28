class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating Node
def create_ll_basic():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    return node1

#Printing the linked List

def print_ll(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next

def insert_at_begining(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node

    return head

def delete_node(head,key):
    current=head
    if current and current.data==key:
        head=current.next
        current=None
        return head
    
    prev = None
    while current and current.data !=key:
        prev=current
        current = current.next

        if current is None:
            return head
        
    prev.next=current.next
    current=None    

    return head


head = create_ll_basic()
head = insert_at_begining(head, 5)
head = delete_node(head, 30)
print_ll(head)

