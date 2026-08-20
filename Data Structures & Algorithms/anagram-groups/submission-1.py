class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        input: list of strings
        output: 2d list where each list contains a group of anagrams

        Q: are the same words considered anagrams? will we have duplicates in our input?
        Q: strings of only alphabetical nature
        - hashmap, sort each string and see if it matches anything in our hashmap
        - O(n) 
        - O(slogs) (python uses optimized version of mergesort -> timsort = mergesort + insertion sort)
        - checking if in hashmap is O(1) expected (assuming with good hash function)
        - inserting new elem is O(1) expected and amortized
        - O(nslogs)
        Q: constraint? 
        3000 < n < 10^6 => O(n)/O(nlogn)
        20 < s < 3000 => O(s^2)
        '''
        anagram_groups = dict()     # sorted anagram name -> [anagrams]
        for word in strs:
            sorted_letters = sorted(word)
            sorted_word = ''.join(sorted_letters)
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
        resulting_groups = []
        for anagram, group in anagram_groups.items():
            resulting_groups.append(group)
        return resulting_groups


        


        