class Solution:
    def isPalindrome(self, s: str) -> bool:
        # import re
        # str_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # left = 0
        # right = len(str_cleaned)-1

        # for _ in range((len(str_cleaned)+1)//2):
        #     if str_cleaned[left] != str_cleaned[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        def alpha_num(c: str):
            return  (ord('a') <= ord(c) <= ord('z')) or \
                    (ord('A') <= ord(c) <= ord('Z')) or \
                    (ord('0') <= ord(c) <= ord('9'))

        left = 0
        right = len(s)-1

        while left < right:
            while(left < right and not alpha_num(s[left])):
                left += 1
            while(right > left and not alpha_num(s[right])):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
