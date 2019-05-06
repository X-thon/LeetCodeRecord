# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #判断链表是否非空
        if head and head.next:
            pass
        else:
            return None
        #声明两个快慢指针并初始化指向表头
        fast = slow = head
        #边界条件，判断快指针能否行走两步；如果无环时快指针走到最后一个节点，会跳出循环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #如果快指针“追上”了慢指针，说明链表有环，跳出循环
            if fast == slow:
                break
        #链表无环时进入下方if语句
        if (not fast) or (not fast.next):
            return None
        #如果有环，将快指针置向表头节点
        fast = head
        #根据方程可证，当链表有环时，仅在快慢指针第一次相遇时，两者在环内；
        #且此时一指针从表头开始“追赶”慢指针，当两者相遇时，位置为环当入口；
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast