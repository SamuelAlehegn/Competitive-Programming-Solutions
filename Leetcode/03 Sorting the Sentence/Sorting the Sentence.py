class Solution:
    def sortSentence(self, s: str) -> str:

        s_list = s.split()
        s_len = len(s_list)
        new_list = ['s']*s_len
        for i in range(s_len):
            new_s = s_list[i]
            last_chx = int(new_s[-1])
            remove_last = new_s[:-1]
            new_list[last_chx - 1] = remove_last
        new_s = ' '.join(new_list)
        return new_s
