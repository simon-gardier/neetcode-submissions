class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dictionnary = {}

        for current_string in strs:
            sorted_string = str(sorted(current_string))
            # anagrams = anagrams_dictionnary.get(sorted_string, [])
            # anagrams.append(current_string)
            # anagrams_dictionnary[sorted_string] = anagrams
            anagrams_dictionnary.setdefault(sorted_string, []).append(current_string)

        anagrams_lists = []
        for sorted_string, anagrams in anagrams_dictionnary.items():
            anagrams_lists.append(anagrams)

        return anagrams_lists
