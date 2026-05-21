class Solution:

    def encode(self, strs: List[str]) -> str:
        ascii_dict = {chr(i): i for i in range(256)}
        encoded_values = []

        if len(strs) == 0:
            return ""

        for word in strs:
            for char in word:
                encoded_values.append(str(ascii_dict[char]))

            encoded_values.append("-1")

        return ",".join(encoded_values)

    def decode(self, s: str) -> List[str]:
        ascii_dict = {i: chr(i) for i in range(256)}
        nums = s.split(",")

        output = []
        word = ""

        if len(s) == 0:
            return []

        for num in nums:
            value = int(num)

            if value == -1:
                output.append(word)
                word = ""
            else:
                word += ascii_dict[value]

        return output