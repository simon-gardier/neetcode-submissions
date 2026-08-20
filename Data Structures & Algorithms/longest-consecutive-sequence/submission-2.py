class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}
        numbers_set = set()
        max_sequence_length = 0

        for num in nums:
            numbers_set.add(num)

        for num in numbers_set:
            if num-1 not in numbers_set:
                sequences[num] = 1

        for start, length in sequences.items():
            next_in_sequence = start + 1
            while next_in_sequence in numbers_set:
                next_in_sequence += 1
                length += 1
            if length > max_sequence_length:
                max_sequence_length = length

        return max_sequence_length

