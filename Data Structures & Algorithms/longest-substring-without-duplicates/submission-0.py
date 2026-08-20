class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # longuest_sequence_length = 0
        # i = 0
        # while i < len(s):
        #     curr_sequence_dict = {}
        #     start = i
        #     while i < len(s) and s[i] not in curr_sequence_dict:
        #         curr_sequence_dict[s[i]] = i
        #         i += 1

        #     longuest_sequence_length = max(i - start, longuest_sequence_length)
        #     if i < len(s):
        #         i = curr_sequence_dict[s[i]] + 1

        # return longuest_sequence_length

        curr_sequence = set()
        longuest_sequence_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in curr_sequence:
                curr_sequence.remove(s[left])
                left += 1
            curr_sequence.add(s[right])
            longuest_sequence_length = max(longuest_sequence_length, right - left + 1)
        
        return longuest_sequence_length
