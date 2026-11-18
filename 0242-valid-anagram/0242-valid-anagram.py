from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc =Counter(s)
        tc = Counter(t)
        print(sc,tc)
        return True if sc == tc else False