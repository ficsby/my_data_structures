#python3
class MyLinkedList(object):

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.head = None
    
    def print_list(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head
        temp_arr = []
        while(temp != None):
            temp_arr.append(temp.val)
            temp = temp.next
        print(temp_arr)
    
    def size(self):
        size, temp = 0, head
        while(temp != None):
            size += 1
        return size
    
    def append(self, val):
        if self.head == None:
            self.head = self.ListNode(val)
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = self.ListNode(val)
    
    def insert(self,val, ind):
        index = 0
        if self.head == None:
            if ind != 0:
                print("Index out of bounds. Appending value to List instead")
            self.head = self.ListNode(val)
        else:
            temp = self.head
            new_val = self.ListNode(val)

            if ind == 0:
                new_val.next = self.head
                self.head = new_val
                return 

            while(temp.next != None):
                if index+1 == ind:
                    index += 1
                    break
                index += 1
                temp = temp.next

            if index != ind:
                print("Index out of bounds. Appending value to List instead")
                temp.next = new_val
            else:
                new_val.next = temp.nex

    def reverse(self):
        prev, curr, next = None, self.head, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev

if __name__== "__main__":
    l1 = MyLinkedList()
    l2 = MyLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.insert(4, 4)
    l1.print_list()
    l1.reverse()
    l1.print_list()