#def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):

    seen = {}

    i: int
    for i,num in enumerate(nums):
        if target - nums[i] in seen:
            return [seen[target - num],i]
        else:
            seen[num] = i

nums =[3,2,4]
tgt =7
print(twoSum(nums,tgt))
