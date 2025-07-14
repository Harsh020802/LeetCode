class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a,r=set() , set()
        for l in range(len(s)-9):
            curr=s[l:l+10]
            if curr in a:
                r.add(curr)
            a.add(curr)
        return list(r)