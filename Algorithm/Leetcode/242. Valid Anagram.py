class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s, t_s = str(sorted(s)), str(sorted(t))
        return s_s == t_s



    dic, dic2 = {}, {}
    for i in s:
        dic1[item] = dic1.get(item, 0) + 1
    for i in t:
        dic2[item] = dic1.get(item, 0) + 1

    return dic1 == dic2