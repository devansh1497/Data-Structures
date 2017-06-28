class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head1 = None
        self.head2 = None


    def check_intersection(self,head1,head2):

        temp1 = head1
        temp2 = head2
        size1= 1
        size2 = 1

        while temp1.next is not None:
            size1 = size1+1
            temp1 = temp1.next

        while temp2.next is not None:
            size2 = size2+1
            temp2 = temp2.next

        if temp1 is not temp2:
            print "The given lists don't intserset at all"

        else:
            jumps = abs(size1-size2)

            if size1>size2:
                while(jumps>0):
                    head1 = head1.next
                    jumps = jumps - 1

            if size2>size1:
                while(jumps>0):
                    head2 = head2.next
                    jumps = jumps - 1

            while head1 is not None and head2 is not None:
                if head1 is head2:
                    print "The lists intersect at the node with value ", head1.data, " and address ", head1
                    break
                head1 = head1.next
                head2 = head2.next

ll = LinkedList()
new_node = Node(5)
ll.head1 = Node(3)
ll.head1.next = Node(2)
ll.head1.next.next = Node(1)
ll.head1.next.next.next = new_node

ll.head2 = Node(1)
ll.head2.next = Node(2)
ll.head2.next.next = Node(2)
ll.head2.next.next.next = new_node

ll.check_intersection(ll.head1, ll.head2)


