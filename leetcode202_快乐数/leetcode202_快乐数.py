class Solution:
    def square(self, n: int) -> int:
        # 输入一个整型数，返回该数各个位置上数的平方和
        s = str(n)
        n_sum = 0
        for i in s:
            n_sum += int(i)*int(i)
        return n_sum
    
    def isHappy(self, n: int) -> bool:
        #此处n1、n2分别为快慢指针，若n为快乐数，则
        n1 = n2 = n
        n1 = self.square(n1)
        n1 = self.square(n1)
        n2 = self.square(n2)
        #当出现重复时判断是否是1，如果是1则为快乐数，反之为非快乐数
        while n1 != n2:
            n1 = self.square(n1)
            n1 = self.square(n1)
            n2 = self.square(n2)
        if n1 == 1:
            return True
        else:
            return False