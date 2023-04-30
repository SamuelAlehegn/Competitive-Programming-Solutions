class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        new_nums = []
        for i in range(len(nums) // 1):
            new_nums.append(nums[i] + nums[len(nums) - i - 1])
        return max(new_nums)
