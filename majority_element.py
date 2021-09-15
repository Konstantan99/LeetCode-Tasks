class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = 0
            for elem in nums:
                if elem == num:
                    count += 1
            if count > majority_count:
                return num
