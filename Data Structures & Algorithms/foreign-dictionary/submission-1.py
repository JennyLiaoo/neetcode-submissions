class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        input: list of strings (words)
        output: sorted order of alien language. "" if impossible
        - strings sorted lexicographically
        Q: words may or may not be lexicographically ordered, this is something we need to check
        Q: are all characters in words english alphabet?
        Q: duplicate words?
        Q: empty strings?
        Q: "longer", "long" impossible cuz we can't have e < ""
        - view this as a graph (directed)
        - i.e "bcdf", "egks" => b < e
        - 'ldfg', 'ldfe' => g < e
        - a < b => a->b
        - in some other string, if b < a => b->a, there is a cycle => no possible alphabet

        - n -> f
        - h -> e
        - r -> n
        - e -> r
        - "hernf"

        This is equivalent of creating these edges and finding if there exists a topological ordering (No cycles)
        '''
        # creating an adjlist 
        adjlist = defaultdict(list)    # maps char -> [neighbors]
        num_parents = defaultdict(int)
        for i in range(1,len(words)):
            prev_word = words[i-1]
            curr_word = words[i]
            foundDiff = False
            for j in range(min(len(prev_word), len(curr_word))):
                if prev_word[j] != curr_word[j]:
                    adjlist[prev_word[j]].append(curr_word[j])
                    num_parents[curr_word[j]] += 1
                    foundDiff = True
                    break
            if not foundDiff and len(prev_word) > len(curr_word):
                return ""
        # see if possible to topologically sort
        # Kahn's algorithm BFS + counting number of parents remaining
        all_chars = set()
        for word in words:
            for c in word:
                all_chars.add(c)
        q = deque()  # start with all chars that have no parent (i.e these are smallest chars in dictionary). contains all chars that can be added to res
        res = []
        seen = set()
        
        for c in all_chars:
            if num_parents[c] == 0:
                q.append(c)
        while q:    # adds things from q to seen
            new_elem = q.popleft()
            if new_elem in seen:
                continue
            seen.add(new_elem)
            res.append(new_elem)
            # go through all the chars this iis a parent of
            for child in adjlist[new_elem]:
                num_parents[child] -= 1
                if num_parents[child] == 0:
                    q.append(child)

        if len(res) == len(all_chars):
            return ''.join(res)
        else:
            return ""

        

            



        