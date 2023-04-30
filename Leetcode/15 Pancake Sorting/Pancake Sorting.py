class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = len(arr)
        new_arr = []
        for i in range(k, 0, -1):
            max_index = arr.index(max(arr[:i]))
            if max_index == i-1:
                continue
            if max_index != 0:
                arr[:max_index+1] = arr[:max_index+1][::-1]
                new_arr.append(max_index+1)
            arr[:i] = arr[:i][::-1]
            new_arr.append(i)
        return new_arr
