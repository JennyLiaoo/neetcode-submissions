from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        input: array of words sorted according to alien alphabet
        output: any valid ordering of characters
                "" if impossible

        - build directed graph from first differing character
          between adjacent words
        - then perform BFS topological sort
        '''

        letters = set()

        for word in words:
            for char in word:
                letters.add(char)

        adjlist = defaultdict(set)
        num_parents = {char: 0 for char in letters}

        # build graph
        for i in range(1, len(words)):
            prev_word = words[i-1]
            new_word = words[i]

            # invalid prefix case
            if (len(prev_word) > len(new_word)
                and prev_word.startswith(new_word)):
                return ""

            for j in range(min(len(prev_word), len(new_word))):
                prev_char = prev_word[j]
                new_char = new_word[j]

                if prev_char != new_char:
                    if new_char not in adjlist[prev_char]:
                        adjlist[prev_char].add(new_char)
                        num_parents[new_char] += 1

                    break

        # topological sort
        q = deque()

        for char in letters:
            if num_parents[char] == 0:
                q.append(char)

        res = []

        while q:
            current_char = q.popleft()
            res.append(current_char)

            for neighbor in adjlist[current_char]:
                num_parents[neighbor] -= 1

                if num_parents[neighbor] == 0:
                    q.append(neighbor)

        # cycle
        if len(res) != len(letters):
            return ""

        return ''.join(res)