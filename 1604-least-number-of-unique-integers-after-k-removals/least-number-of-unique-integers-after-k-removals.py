class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mp = collections.Counter(arr)
        v = list(mp.values())
        cnt = 0
        v.sort()
        for i in range(len(v)):
            if k > v[i]:
                k -= v[i]
                v[i] = 0
            else:
                v[i] -= k
                k = 0
            if v[i] != 0:
                cnt += 1
        return cnt