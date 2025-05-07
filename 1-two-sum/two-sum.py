class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}
        for i,num in enumerate(nums):
            if target-num in val:
                return [i,val[target-num]]
            val[num]=i
        