class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        has greedy solution
        sliding window is not viable since there are negatives.
        you could greedily choose whether or not to extend the current subarray based on the sum of previous elements of current window with current element. 
        i.e [2, -3, 4, -2, 2, 1, -1, 4]
        2
        2 + -3 = -1, so the total contribution of the previous part of the array is negative. it would be better to not include it at all. 
        choose larger of current number + prev sum, and current number alone
        -3+4 = 1
        1 + -2 
        '''
        best = nums[0]
        prev = nums[0]
        for i in range(1,len(nums)):
            # asking whether or not it would be better to start new here or to continue with previous subarray
            prev = max(nums[i], prev + nums[i])
            best = max(best, prev)

        return best
        

        