class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)        
        if not self.head:
            self.head = node
        else:
            self.tail.next = node        
            self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))        
        node = node.next        
        if node:
            fptr.write(sep)

def removeNodes(listHead, x):
    deln = listHead    
    if listHead is not None:
        if deln.data > x:
            listHead = listHead.next
            deln = None

    prev = listHead
    while prev is not None:
        deln = deln.next
        
        if deln.data > x:
            prev.next = deln.next
            deln = None
        else:
            prev = deln

if __name__ == '__main__':
        #fptr = open(os.environ['OUTPUT_PATH'], 'w')
        listHead_count = int(input().strip())
        listHead = SinglyLinkedList()
        for _ in range(listHead_count):
                listHead_item = int(input().strip())
                listHead.insert_node(listHead_item)
        x = int(input().strip())
        result = removeNodes(listHead.head, x)
        print_singly_linked_list(result, '\n', fptr)

        #fptr.write('\n')
        #fptr.close()
