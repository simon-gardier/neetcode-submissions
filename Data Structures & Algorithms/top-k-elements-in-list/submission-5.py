class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_integers = {}
        frequency_lists = [[] for i in range(len(nums))] # [[] , []]

        for num in nums:
            count_integers[num] = 1 + count_integers.get(num, 0)
        # {1: 1, 2: 1}

        for integer, count in count_integers.items():
            frequency_lists[count-1].append(integer)
        # [[1, 2]]

        topk_elements = []
        topk_count = 0
        for i in range(k):
            bucket = frequency_lists.pop()
            while(len(bucket) == 0):
                bucket = frequency_lists.pop()

            for integer in bucket:
                topk_elements.append(integer)
                topk_count += 1

                if topk_count == k:
                    return topk_elements

        return topk_elements
