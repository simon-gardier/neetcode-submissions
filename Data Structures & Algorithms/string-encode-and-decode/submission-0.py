class Solution:

    # handles string that are empty

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for current_str in strs:
            encoded += str(len(current_str)) + "#" + current_str

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            current_word_length = int(s[i:j])
            word = s[j+1:j+1+current_word_length]
            decoded.append(word)
            i = j + 1 + current_word_length # "5#hello5#world" i = 0, j = 1, current_word_length = 5, i <- 6, 

        return decoded
