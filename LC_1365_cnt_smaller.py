class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        l1=nums.copy()
        op = []
        l1.sort()
        ord1 = {l1[0]:0}
        for i in range(1, len(l1)):
            if l1[i] != l1[i-1]:
                ord1[l1[i]]=i
        l1=[]
        for num in nums:
            l1.append(ord1[num])

        return l1
l=[7,7,7,7]
sl = Solution()
print(sl.smallerNumbersThanCurrent(l))


