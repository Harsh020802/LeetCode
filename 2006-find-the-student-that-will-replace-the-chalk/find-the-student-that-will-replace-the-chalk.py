class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        k_new=k%s
        for i in range(0,len(chalk)):
            if(k_new<chalk[i]):
                return i
            k_new-=chalk[i]
        return -1