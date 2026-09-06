class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        - count and compare
        - O(n) expected
        '''
        base = len(nums)//3
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        appear = set()
        for num in nums:
            if counts[num] > base:
                appear.add(num) #O(1) expected
        return list(appear)
        