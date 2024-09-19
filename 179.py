class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        result = []
        def Compare(x, y):
            return x + y > y + x  

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if not Compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
 
        result = ''.join(nums) 

        if result[0] == '0':
            return '0'

        return result
