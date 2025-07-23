# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        res = ListNode(0)
        dummy = res
        
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        dummy.next = list1 or list2

        return res.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        prev = None
        curr = fast = head
        while fast and fast.next:
            prev = curr
            curr = curr.next
            fast = fast.next.next

        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(curr)

        return self.mergeTwoLists(left, right)