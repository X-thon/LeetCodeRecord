class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        self.ans = 0
        #特殊情况
        if not g:
            return None
        if not s:
            return 0        
        #由于思路即：从胃口值g最小的孩子开始，尝试着找到s值能够满足小孩胃口值g的其中最小的s值
        #所以先将两个数组排序，然后逆序（方便使用pop弹出值，也方便实现“已分发”这个概念）
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        #在任意一个数组为空时跳出循环
        while g != [] and s != []:
            temp_g = g.pop()
            while s != []:
                if temp_g <= s.pop():
                    self.ans += 1
                    break
        return self.ans
    