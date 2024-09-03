class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for i in s:
            num+=str(ord(i)-96)
        for _ in range(k):
            sum=0
            for j in num:
                sum+=int(j)
            num=str(sum)
        return int(num)
