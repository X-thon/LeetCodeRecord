class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #d将存储字符与其对应的索引下标
        d = dict()
        i = 0
        j = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in d:
                #跳过
                i = max(d[s[j]], i)
            #比较最大重复子串的长度
            ans = max(ans, j - i + 1)
            #如果s[j]重复，j索引也从j+1位置开始，不取s[j]
            #d[s[j]]的值表示的是，s[j]上的字符对应的位置是d[s[j]]-1，所以如果后面的遍历中，发现了与s[j]重复的字符，则从d[s[j]]取起
            d[s[j]] = j + 1
            j = j + 1
        return ans