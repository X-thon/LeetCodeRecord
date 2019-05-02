# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        p = result
        # 进位标志器
        sign = 0
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_num = sign + x + y
            sign = sum_num // 10
            p.next = ListNode(sum_num % 10)
            # 指针后移
            p = p.next
            if(l1 != None): l1 = l1.next
            if(l2 != None): l2 = l2.next
        if sign > 0:
            p.next = ListNode(sign)
        return result.next