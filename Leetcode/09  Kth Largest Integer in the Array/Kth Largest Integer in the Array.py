class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new_nums = []
        for i in range(len(nums)):
            new_nums.append(int(nums[i]))
        new_nums.sort()
        return str(new_nums[-k])
