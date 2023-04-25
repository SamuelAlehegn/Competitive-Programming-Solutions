class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        len_changed = len(changed)
        changed.sort()
        new_list = []
        new_dict = {}
        if len_changed % 2 != 0:
            return []
        for i in changed:
            new_dict[i] = new_dict.get(i, 0) + 1
        for i in changed:
            if new_dict.get(i, 0) == 0:
                continue
            new_dict[i] -=1
            if new_dict.get(2*i, 0) == 0:
                return []
            new_dict[2*i] -= 1
            new_list.append(i)
     
        return new_list
        
       
        

