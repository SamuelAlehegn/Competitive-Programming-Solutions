class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        new_list = []
        for i in range(len(l)):
            new_nums = nums[l[i]:r[i]+1]
            new_nums.sort()
            difference = new_nums[1] - new_nums[0]
            for j in range(2, len(new_nums)):
                if new_nums[j] - new_nums[j-1] != difference:
                    new_list.append(False)
                    break
            else:
                new_list.append(True)
        return new_list
