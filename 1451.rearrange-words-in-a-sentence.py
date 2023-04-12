#
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = []
        for w in text.split(" "):
            l = 0
            r = len(arr)-1
            m = (r-l)//2
            while l < r:
                if len(arr[m]) < len(w):
                    r = m
                else:
                    l = m
                m = (r-l)//2

            arr.insert(m+1, w.lower())
        return " ".join(arr)
# @lc code=end

