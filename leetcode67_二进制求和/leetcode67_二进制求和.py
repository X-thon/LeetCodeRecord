import itertools
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = list(a[::-1])
        bn = list(b[::-1])
        sign = 0
        n = list()
        for n1, n2 in itertools.zip_longest(an, bn, fillvalue="0"):
            if int(n1) + int(n2) + sign >= 2:
                n.append(str((int(n1) + int(n2) + sign) % 2))
                sign = 1
            else:
                n.append(str((int(n1) + int(n2) + sign) % 2))
                sign = 0
        if sign != 0:
            n.append(str(sign))
        n = n[::-1]
        return "".join(n)

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a,2)+int(b,2))[2:]