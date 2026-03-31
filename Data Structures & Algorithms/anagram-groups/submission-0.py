class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]* 26 

            for t in s :
                # asci conversion for this is needed to map it technically 
                count [ord(t) - ord("a")]+=1
                # so this technically gives you the outcome of count[a or b or ...]
                # hnece saying count[0] which is count[80 -80] which is count[a] is practivally 1
            res[tuple(count)].append(s)
        
        return list(res.values())