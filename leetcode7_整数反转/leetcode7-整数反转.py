class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            str_x = str(x)
            x = ""
            #如果是负数
            if str_x[0] == '-':
                x += '-'
            #将字符串逆序，去掉可能出现在头部的0和尾部的-号
            x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
            x = int(x)
            if pow(-2, 31) < x < pow(2, 31) - 1:
                return x
            else:
                return 0