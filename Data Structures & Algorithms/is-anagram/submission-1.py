class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        d2 = dict()
        for c in t:
            d2[c] = d2.get(c, 0) + 1
        if(len(d) != len(d2)):
            return False
        for v in d:
            if(d.get(v) != d2.get(v, -1)):
                return False
        return True

        