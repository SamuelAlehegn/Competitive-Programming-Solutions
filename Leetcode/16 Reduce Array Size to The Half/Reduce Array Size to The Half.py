class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_arr = {}
        count = 0
        count_sum = 0
        for i in arr:
            count_arr[i] = count_arr.get(i, 0) + 1
        freq_list = list(count_arr.values())
        freq_list.sort(reverse=True)
        for j in freq_list:
            count += 1
            count_sum += j
            if count_sum >= len(arr) // 2:
                return count
