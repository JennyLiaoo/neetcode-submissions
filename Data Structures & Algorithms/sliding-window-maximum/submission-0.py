import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        input: list of int (nums), int (k)
        output: the max element of the window at each step (list of ints)
        Q: can nums contain negatives or duplicate values? yes
        Q: k < len(nums)
        Q: 3000 < n < 10^6 => O(n)/O(nlogn)
        - sliding window of size k
        - size of output: n - k + 1

        - heap -> easily find max value -> remove elem of heap is hard
        - brute force: go through and max all elements of current window    
            - O(NK)
        - heap + lazy deletion nlogn
        - dict: counts of nums inside the window n
        Instead of keeping a dict, we can store the index that a value appears at in the heap

        '''
        largest_num = []
        for i in range(k):
            largest_num.append((nums[i], i))
        heapq.heapify_max(largest_num)

        max_in_each_window = []

        for i in range(len(nums)-k+1):  # i is the starting index of our window
            while largest_num:
                potential_max, index = largest_num[0]
                if index < i:
                    heapq.heappop_max(largest_num)
                    continue
                max_in_each_window.append(potential_max)
                break
            new_elem_index = i+k
            if i + k < len(nums):
                new_elem = nums[i+k]
                heapq.heappush_max(largest_num, (new_elem, new_elem_index))
        return max_in_each_window

            

        
        