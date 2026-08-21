class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        input: array of integers nums
        output: int (length of longest strictly incresing subsequence)
        Q: subseq - non contiguous and order maintained
        Q: could we get empty input + is it nums
        Q: bounds on size of nums => O(n^2)

        Brute force:
        - generate all subsequences O(2^n) using backtracking and check if strictly increasing O(n2^n)
        - Not ideal. lots of repeated subproblems
        - DP
        max_length[i] = maximum length subsequence ending at i
        max_length[i] = max(for j < i: if nums[j] < nums[i]: max_length[j] + 1
        max_length[0] = 1
        max(max_length) = answer
        O(n^2)
        '''
        max_length = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_length[i] = max(max_length[i], 1 + max_length[j])

        return max(max_length)
        