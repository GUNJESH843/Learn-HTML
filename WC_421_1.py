from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0] * nums[0]
        else:
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
                
            def lcm(a, b):
                return abs(a * b) // gcd(a, b)
            
            def gcdlcm(nums):
                ans_gcd, ans_lcm = nums[0], nums[0]
                for num in nums[1:]:
                    ans_gcd = gcd(ans_gcd, num)  
                    ans_lcm = lcm(ans_lcm, num)  
                return ans_gcd, ans_lcm

            gcd_full, lcm_full = gcdlcm(nums)
            max_score = gcd_full * lcm_full
            
            maxans = max_score

            for i in range(len(nums)):
                sub = nums[:i] + nums[i+1:] 
                if sub:  
                    gcdsub, lcmsub = gcdlcm(sub)
                    maxans = max(maxans, gcdsub * lcmsub)
            
            return maxans
