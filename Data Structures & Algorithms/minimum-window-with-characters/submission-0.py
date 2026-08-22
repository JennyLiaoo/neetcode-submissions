from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        input: string (s), string (t)
        output: string (shortest substring of s such that every char in t is present in the substring)

        Q: possibility that there's no such substring?
        Q: if t has duplicate values (i.e two a's), do we need to have two a's in our substring of s or just one a (i.e substring of s includes all unique char of t)
        Q: multiple possible correct answers?
        Q: Substring as in contiguous?
        Q: bounds O(n)/O(nlogn)

        Greedy sol: sliding windows + hashmaps
        - Grow window until all char in t are in window + save vlaue
        - shrink while all char in t are in window, then grow again
        - keep hashmap of all char in t + freq
        - keep hashmap of all char in window + freq
        - need a way to quickly check whether two dictionaries are equal or if the number of each elem in a dict is greater than that of another dict
            - or we can have another data struct to store which elems in t have been properly included in the window
        -O(n) solution with O(n) space

        Binary search: 
        - binary search for the minimum possible length (0 to len(s))
        - after finding a length, sliding window across the string s with a window of that size and use a hashmap to determine if all char of t in that substring. if so, then this condition is true and we can change the size of our search space
        - O(logn) * O(n) = O(nlogn)
        - hashmap operations are all O(1) expected or amortized

        
        Edge case: answer is in ending string
        "YVAUSAUAY" "SAAY" (0,5)
        '''
        # going with the sliding windows method
        char_counts_t = defaultdict(int)    # unmodified after
        for c in t:
            char_counts_t[c] += 1
    
        # modify as window changes
        char_counts_window = defaultdict(int)
        chars_in_t = set(list(t))   # don't modify
        
        # characters in t which are fully encompassed by s, including their duplicates (i.e if there are two a's, there are at least two a's in our window)
        chars_in_window = set()     # modify as window changes

        '''
        "ISVAUAYSAUY" "SAAY"
        {S:1, A:2, Y:1}, {S, A, Y}
        d = {S:1, A:1, Y:2}, s = { S, Y}
        left = 6, right = 8
        shortest_len = 4, substr = (5, 8)
        '''
        # window is left and right inclusive. So when right == len(s), that's when we stop
        left = 0
        right = 0
        shortest_substr_len = float('inf')
        shortest_substr = None  # tuple so we don't have to rebuild string

        while right < len(s):   # 3,4,5,6,7,8,9,10
            # increase window, add s[right] to window
            new_char = s[right] #
            if new_char in chars_in_t:
                char_counts_window[new_char] += 1
                if char_counts_window[new_char] == char_counts_t[new_char]:
                    chars_in_window.add(new_char)

            while len(chars_in_window) == len(chars_in_t):  # 3
                # remove elements from the window
                removed_char = s[left]  #S
                if removed_char in chars_in_t:
                    char_counts_window[removed_char] -= 1
                    if char_counts_window[removed_char] < char_counts_t[removed_char]:
                        chars_in_window.remove(removed_char)
                        if shortest_substr_len > right - left + 1:
                            shortest_substr_len = right-left+1
                            shortest_substr = (left, right)
                left += 1
            # increment window size
            right += 1
        if shortest_substr is None:
            return ""
        else:
            return s[shortest_substr[0]:shortest_substr[1]+1]
        


        