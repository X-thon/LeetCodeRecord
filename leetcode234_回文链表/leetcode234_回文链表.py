class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if head == [] or head == None:
#             return False
#         l_list = list()
#         while head.next != None:
#             l_list.append(head.val)
#             head = head.next
#         l_list.append(head.val)
#         reverse_list = l_list[::-1]
#         if reverse_list == l_list:
#             return True
#         else:
#             return False

class Solution:
    def isPalindrome(self, head:ListNode)->bool:
        #定义快慢指针并赋值指向表头
        fast = slow = head
        #边界条件，判断快指针能否行走两步
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #链表长为奇数时，快指针走到尾节点停下，慢指针指向中点；
        #链表长为偶数时，快指针走到尾节点的下一个节点，此时慢指针指向链表后半段的第一个节点；
        #利用python元组赋值的特性进行链表后半部分的转化
        #比较绕，可以结合画图理解
        node = None
        while slow:
            slow.next, node, slow = node, slow, slow.next
        #将反转后的链表的节点的值与前半段对比，如果都相同则证明是回文链表
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
