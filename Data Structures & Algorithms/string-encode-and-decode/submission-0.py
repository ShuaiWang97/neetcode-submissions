class Solution:

    def encode(self, strs: List[str]) -> str:
        # we use a example of num + # + str

        chars=""
        for str_ in strs:
            chars += str(len(str_))+"#"+str_
        return chars

    def decode(self, s: str) -> List[str]:

        # decode from num + # + str
        result = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])
            i = word_end


        return result

