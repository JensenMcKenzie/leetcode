#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        iname = 0
        ityped = 0
        while ityped < len(typed) and iname < len(name):
            if name[iname] != typed[ityped]:
                print(iname, ityped)
                return False
            while ityped < len(typed) and name[iname] == typed[ityped]:
                if iname + 1 < len(name) and name[iname] == name[iname+1]:
                    iname+=1
                ityped += 1
            iname += 1
        print(ityped, iname)
        return ityped == len(typed) and iname == len(name)

# @lc code=end

