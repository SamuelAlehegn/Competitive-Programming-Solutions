class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list_len = len(nums)
        count = [0]*list_len
        for i in range(list_len):
            for j in range(list_len):
                if nums[j] != nums[i] and nums[j] < nums[i]:
                    count[i] += 1
        return count
