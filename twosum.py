class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, numbs in enumerate(nums):
            number = target - numbs
            if number in hashmap :
                return [hashmap[number],i]
            hashmap[numbs] = i
