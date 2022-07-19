# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.cur_node = None

    def add(self,data = None):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

head = [1,2,3,4,5]
head1 = ListNode()
for i in head:
    head1 = ListNode.add(i)
class Solution01:
    def reverseList(self, head: ListNode) -> ListNode:
        right, left = None, head
        while left is not None:
            next = left.next
            left.next = right
            right = left
            left = next
        return right

if __name__== '__main__':
    print(Solution01().reverseList(head1))