class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        max_sequence_length = 0

        for num in numbers_set:
            if num-1 not in numbers_set:
                length = 1
                next_in_sequence = num + 1
                while next_in_sequence in numbers_set:
                    next_in_sequence += 1
                    length += 1
                if length > max_sequence_length:
                    max_sequence_length = length

        return max_sequence_length

