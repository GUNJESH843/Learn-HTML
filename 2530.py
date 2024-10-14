class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums_n = []
        for num in nums:
            nums_n.append(-num)
        heapq.heapify(nums_n)

        score = 0
        while k > 0:
            l = -heapq.heappop(nums_n)
            score += l
            heapq.heappush(nums_n, -ceil(l/3))
            k -= 1
        return score
