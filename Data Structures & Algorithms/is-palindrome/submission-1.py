class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        str_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(str_cleaned)-1

        for _ in range((len(str_cleaned)+1)//2):
            if str_cleaned[left] != str_cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
    