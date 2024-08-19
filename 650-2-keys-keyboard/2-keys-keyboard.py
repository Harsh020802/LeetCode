class Solution:
    def minSteps(self, n: int) -> int:
        i=2
        ans=0
        while(i*i<=n):
            if(n%i==0):
                ans+=i
                n=n/i
            else:
                i+=1
        if(n!=1):
            ans+=n
        return int(ans)