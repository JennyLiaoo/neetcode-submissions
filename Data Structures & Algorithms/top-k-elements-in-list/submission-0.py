import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        input: list of integers, int k
        output: list of integers (the k most frequent of nums)
        Q: unique?
        Q: order?
        Q: k > num of unique elem
        Q: 3000 < n < 10^6 => O(n)/O(nlogn)

        dict: num -> freq   O(n), look up in dict -> O(1) expected. O(1) expected/amortized.
        PQs, max heap: (freq, num) O(klogn) < O(nlogn) cuz k < n heappop is O(logn) worst case, cuz u need to put bottom to top and sift down.
        {1:1, 2:2, 3:3}
        (1,1), (2,2), (3,3) => (3,3) (2,2) (1,1)
        '''
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        largest_freq = []   # (freq, number)
        for num, count in freq.items():
            largest_freq.append((count, num))
        heapq.heapify_max(largest_freq)

        top_k_most_freq = []
        for _ in range(k):
            frequency, number = heapq.heappop_max(largest_freq)
            top_k_most_freq.append(number)
        return top_k_most_freq

        



        