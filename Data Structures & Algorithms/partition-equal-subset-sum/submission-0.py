class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        input: int array (nums)
        output: True if you can parition the array in a way such that the two subsets are equal

        - prefix sums O(nums)
        - Q: is subset contigous? NO
        for each index in nums: calculate the sums of the two halves using prefix sums in O(1)
        n-1 possible parititons
        Whole algo is O(n)
        Greedy algo does not work

        - Brute force: generate all possible subsets by choosing to either include (subset1) or not include (subset2) each element, and calculate total sum and compare O(2^n) <- exponential
        - at each value, we have a choice: add current elem to subset 1 or subset 2

        - subset_sum = total_sum / 2
        - reduces to finding a subset sum of sum total_sum/2
        total_sum is odd, return False
        - feasibility problem finding if there exists a subset which sums to total_sum // 2
        - 0/1 knapsack problem, target sum = total_sum//2 (left to right pass dp)

        Feasibilty DP question
        can_make_sum[i][j] = True if u can make sum j using the first i values of nums for 0 <= i < len(nums)
        can_make_sum[i][j] = can_make_sum[i-1][j-nums[i-1]] or can_make_sum[i-1][j]
        can_make_sum[i][0] = True
        can_make_sum[len(nums)][total_sum//2] = answer
        '''
        # [1,1,1,1]
        '''
        [T,F,F,F]
        [T,T,F,F]
        [T,T,T,F]
        [T,F,F,T]
        - even but no equal partition exists
        - nums array is empty
        Can optimize space complexiyt: row i only depends on i-1th row (but you'd have to loop through j backwards?)
        '''
        total_sum = sum(nums)   # 4
        if total_sum % 2 == 1:
            return False
        target_sum = total_sum // 2
        can_make_sum = [[False for _ in range(target_sum+1)] for _ in range(len(nums)+1)]
        can_make_sum[0][0] = True
        for i in range(1,len(nums)+1):    #3
            for j in range(target_sum+1):   #3
                if j == 0:
                    can_make_sum[i][j] = True
                else:
                    can_make_sum[i][j] = can_make_sum[i-1][j]
                    if j >= nums[i-1]:
                        can_make_sum[i][j] = can_make_sum[i-1][j-nums[i-1]] or can_make_sum[i][j]
        return can_make_sum[len(nums)][target_sum]
                

        