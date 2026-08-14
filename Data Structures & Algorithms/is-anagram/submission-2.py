class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        occurences_in_s = {}
        occurences_in_t = {}
        for i in range(len(s)):
            occurences_in_s[s[i]] = 1 + occurences_in_s.get(s[i], 0)
            occurences_in_t[t[i]] = 1 + occurences_in_t.get(t[i], 0)

        for key_s in occurences_in_s:
            if occurences_in_s[key_s] != occurences_in_t.get(key_s, 0):
                return False
        return True

        # return sorted(s) == sorted(t)