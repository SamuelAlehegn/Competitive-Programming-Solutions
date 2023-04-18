class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        In-Place Sorting Algorithms:
                    Bubble sort, 
                    Selection Sort,
                    Insertion Sort, 
                    Heapsort.
        """
        # Bubble Sort
        list_len = len(nums)
        for i in range(list_len):
            for j in range(list_len - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
