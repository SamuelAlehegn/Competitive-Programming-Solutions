class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted(nums)
        new_list = []
        for i in range(len(new_nums)):
            if new_nums[i] == target:
                new_list.append(i)
        return sorted(new_list)
