class Solution:

    delimiter : str = "\\"

    def char2dig(self,text):

        return str([ord(a) for a in text])

    def encode(self, strs: List[str]) -> str:
        
        return self.delimiter.join(self.char2dig(ele) for ele in strs)

    def decode(self, s: str) -> List[str]:
        
        words = s.split(self.delimiter)
        result = []
        for word in words:
            if word : 
                result.append("".join(chr(ele) for ele in eval(word)))
        print(result)
        return result
