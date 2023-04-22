class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        nums[0::2], nums[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]
        return nums
