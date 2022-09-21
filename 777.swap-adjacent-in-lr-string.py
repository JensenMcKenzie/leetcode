#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        startPointer = 0
        endPointer = 0
        while startPointer < len(start) and endPointer < len(start):
            while startPointer < len(start) and start[startPointer] == 'X':startPointer += 1
            while endPointer < len(start) and end[endPointer] == "X": endPointer += 1
            if startPointer == len(start) or endPointer == len(start): break
            if start[startPointer] != end[endPointer] or (start[startPointer] == "L" and startPointer < endPointer) or (start[startPointer] == "R" and startPointer > endPointer):
                return False
            startPointer += 1
            endPointer += 1
        if startPointer < len(start) and start[startPointer] != 'X': return False
        if endPointer < len(start) and end[endPointer] != 'X': return False
        return True
            
# @lc code=end

