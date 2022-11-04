#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start


class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        if t == None:
            return None
        self.arr.append(t)
        end = len(self.arr)-1
        count = 0
        while end >= 0 and self.arr[end] > t-3000:
            count += 1
            end -= 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

