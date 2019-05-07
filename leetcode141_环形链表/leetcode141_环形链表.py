# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head:ListNode)->bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        #定义快慢指针
        fast = slow = head
        #边界条件
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #如果快指针先走却能“遇到”慢指针，证明链表有环
            if fast == slow:
                return True
        #反之无环
        return False