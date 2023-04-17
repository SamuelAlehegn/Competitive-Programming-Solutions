class Solution:
    def is_number(self, i):
        try:
            int(i)
            return True
        except ValueError:
            return False

    def areNumbersAscending(self, s: str) -> bool:
        s_list = s.split()
        # s_len = len(s_list)
        new_list = []
        for i in s_list:
            if self.is_number(i):
                new_list.append(int(i))
        s_len = len(new_list)
        for i in range(1, s_len):
            if new_list[i] <= new_list[i-1]:
                return False

        return True
