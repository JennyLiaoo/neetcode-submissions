class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        input: string (s)
        output: int (number of palindromes in s)
        Q: empty string?
        Q: can the string contain whitespace?
            - '    ' can look like '\t' '    a\t'
        Q: Bound of s? 20 < n < 3000 => O(n^2)

        - greedy + sliding windows, two pointers
        - Brute force: generating all palindromes O(n^3)
        - DP
        is_pal[i][j] = 1 if s[i:j+1] is a palindrome, 0 otherwise
        Sum up is_pal => number of palindrome within s
        is_pal[i][i] = 1
        is_pal[i][i+1] = 1 if s[i] == s[i+1]
        is_pal[i][j] = 1 if s[i] == s[j] and s[i+1:j-1] is palindrome
        solution: sum(is_pal)

        is_pal = [[1,1,1],
                  [0,1,1],
                  [0,0,1]

        Cases to test:
        - general case "abcdcxy", "ababa", "aaaaa", "abcde", ""
        '''
        is_pal = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):   
            for j in range(i, len(s)):      
                if i == j:
                    is_pal[i][j] = 1
                elif i+1 == j:
                    if s[i] == s[j]:
                        is_pal[i][j] = 1
                else:
                    if is_pal[i+1][j-1] == 1 and s[i] == s[j]:
                        is_pal[i][j] = 1
        num_pal = 0
        for row in is_pal:
            num_pal += sum(row)
        return num_pal