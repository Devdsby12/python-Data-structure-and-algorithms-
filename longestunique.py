class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        count = []
        for i in range(len(s)) :
            dictt = set()
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
