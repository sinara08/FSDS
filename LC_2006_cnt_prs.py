from collections import defaultdict
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:

        cnt=i=0
        diff=defaultdict(int)
        for num in nums:
            if num-k in diff:
                cnt += diff[num-k]

            if num+k in diff:
                 #diff[num] += 1
                 cnt += diff[num+k]
            diff[num] += 1


        return cnt
nums=[9,3,1,1,4,5,4,9,5,10]


k = 1
s=Solution()
print(s.countKDifference(nums,k))