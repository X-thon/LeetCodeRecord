class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        #使用模拟场景法
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five:
                   five -= 1
                   ten += 1
                else:
                    return False
            else:
                #如果顾客付20块钱，我们如果零钱足够，总是希望先付一张十块加一张五块
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False 
        return True 