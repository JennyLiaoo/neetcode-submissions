class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        input: int arr (hand, value of ith card), int (groupSize)
        putput: bool (if possible to rearrange cards into groups s.t each has size groupSize and cards are consecutive values)

        - feasibility problem
        Q: are we assuming standard card deck 1-13?/do we need to convert k->13 or can the card values be anything
        Q: possibility of len(hand) < groupSize => return false?
        Q: dupes in hand?
        Q: hand is sorted?
        Q: bound? O(n)/O(nlogn)

        - greedy? can't sliding windows cuz u would skip some values

        - [1,2,2,3,3,4,4,5], size = 4
        - have some sort of dict? remove vals from dict?
        i.e 
        we try to start from index i of hand.
        remove consecutive elems from dict until size = 4
        try next index
        if ever while constructing a group, no next consecutive number exists (i.e not there originally or got removed cuz added in prev group, return false)
        if reach end, return true
        O(n)
        '''
        hand.sort()
        counts = defaultdict(int)
        for val in hand:
            counts[val] += 1

        for val in hand:
            if val in counts:
                # create new group starting here
                for i in range(groupSize):
                    if val + i in counts:
                        counts[val+i] -= 1
                        if counts[val+i] == 0:
                            counts.pop(val+i)
                    else:
                        return False
        return True


        