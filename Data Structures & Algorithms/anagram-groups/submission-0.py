class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            a="".join(sorted(i))
            if a in d:
                d[a]=d[a]+[i]
            else:
                d[a]=[i]
        return list(d.values())
