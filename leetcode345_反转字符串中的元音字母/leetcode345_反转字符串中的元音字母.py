class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s or s == "":
            return s
        #一开始没有考虑大小写问题
        y = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        string = list(s)
        head = 0
        tail = len(s) - 1
        #使用头尾指针，将碰到的，非同一位置上的元音字母互换
        while head <= tail:
            #头指针先走，定位到元音字母后，再移动尾指针
            if string[head] in y:
                while tail >= head:
                    if string[tail] in y:
                        break
                    else:
                        tail -= 1
                if head != tail:
                    #有些好奇就去测试了一下，即使下面的赋值语句中的head == tail，也不会出问题报错
                    string[head], string[tail] = string[tail], string[head]
                    #之前没有考虑到交换完了之后将tail指针前移，这样导致如果tail指针碰到元音字母，将不会再移动，导致出错
                    tail -= 1
                #之前在循环外加了head += 1，而第一层if外，即外层while还有一条head += 1，导致head指针多后移一位，如果元音字母连续出现，则第二个元音字母会被跳过导致出错
                #head += 1
            head += 1
        s = "".join(string)
        return s