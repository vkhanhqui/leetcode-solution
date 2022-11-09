class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if (
                char_s in s_dict
            ):
                if s_dict[char_s] != char_t:
                    return False
            elif char_t in s_dict.values():
                return False
            s_dict[char_s] = char_t
        return True
