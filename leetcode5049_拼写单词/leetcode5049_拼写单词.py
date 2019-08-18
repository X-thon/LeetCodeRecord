from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = Counter(chars)
        res = 0
        for word in words:
            word_dict = Counter(word)
            sign = True
            for key, value in word_dict.items():
                if key not in chars_dict:
                    sign = False
                    break
                elif key in chars_dict and value > chars_dict[key]:
                    sign = False
                    break
                elif key in chars_dict and value <= chars_dict[key]:
                    continue
            if sign == True:
                res += len(word)
        return res

