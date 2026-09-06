class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        # there exist sol
        total=0
        res = 0
        # invar:all prev total pos, thus when neg, reset to zero cuz removing prev = removing gas => still neg
        for i in range(len(gas)):
            amt = gas[i]-cost[i]
            total += amt
            if total < 0:
                total = 0
                res = i+1
        return res
        