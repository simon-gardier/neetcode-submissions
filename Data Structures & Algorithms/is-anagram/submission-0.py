class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        occurences_in_s = {}
        occurences_in_t = {}
        for i in range(len(s)):
            if occurences_in_s.get(s[i]) is None:
                occurences_in_s[s[i]] = 0
            occurences_in_s[s[i]] += 1

            if occurences_in_t.get(t[i]) is None:
                occurences_in_t[t[i]] = 0
            occurences_in_t[t[i]] += 1

        for key_in_s, value_in_s in occurences_in_s.items():
            value_in_t = occurences_in_t.get(key_in_s)  
            if value_in_t != value_in_s:
                return False
        return True