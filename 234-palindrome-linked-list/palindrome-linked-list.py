# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head

        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        right = None
        temp = slow
        while temp:
            front = temp.next
            temp.next = right
            right = temp
            temp = front

        while right:
            if right.val != head.val:
                return False
            else:
                right = right.next
                head = head.next
        return True

        