class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        count = []
        for i in range(len(s)) :
            dictt = set()  # we can also use other data types here instead of set but set is fast for lookups
            counting = 0
            for j in s[i:] :
                if j not in dictt :
                    dictt.add(j)  
                    counting += 1
                else :
                    break
            count.append(counting)
        if not count:
            return 0
        return max(count)   
