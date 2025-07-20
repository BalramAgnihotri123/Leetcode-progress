# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        middle = fast = head

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        return middle
        