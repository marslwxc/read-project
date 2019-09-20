class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        dict1, dict2 = {}, {}
        for x in s:
            dict1[x] = dict1.get(x, 0) + 1
        for x in t:
            dict2[x] = dict2.get(x, 0) + 1
        return dict1 == dict2