class Solution:

    str_sep = "#"
    chr_sep = "*"


    def encode(self, strs: List[str]) -> str:
        
        result = self.str_sep.join(self.chr_sep.join(str(ord(ch)) for ch in st) for st in strs)
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        for enc_st in s.split(self.str_sep):
            if not enc_st:
                ans.append("")
            else:
                ans.append(
                    "".join(chr(int(ele)) for ele in enc_st.split(self.chr_sep))
                )
        return ans