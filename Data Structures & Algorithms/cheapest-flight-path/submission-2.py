import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        input: 
        - int (n number of airports labelled 0 to n-1)
        - 2d list (flights, flights[i] = [from airport, to airport, price])
        - int (src airport), int (dst airport), int (k maximum number of stops)
        output: cheapest price from src to dest with AT MOST k stops (exclusive of src, dest). return -1 if not possible

        - so essentially, we need to reach dest from src in k+1 "hops" (by the time we make our k+1th hop we need to be at destination)
        - view as a graph with weighted edges

        Can i make the assumption that flights, src, dest are well formed? (i.e that the airport number is within the range of 0 to n-1)
        Q: is it guaranteed that we can make it to dest in k stops?
        Q: can there be more than one flight from one airport to another (multiedges?)
        Q: are there self loops? (edge from airport to self?)
        Q: Can src == dest

        Initial thought: Dijkstra's
        Q: can there be negative prices/edges? No so we good
        dijkstra finds us the shortest path to each node. we can use dijkstra but limit the distance to k+1 edges away. dijkstra guarantees that the first time we reach a node is the smallest cost to reach that node. So essentially: dijkstra + distance limit. if we haven't reached dest, return -1. Otherwise, return the cost the moment we first reach the airport
        - only add new nodes to PQ if their dist <= k+1

        - pq: (cost, airport, dist from source)
        When we pop a node, make sure dist is within bounds k+1. if not then ignore. otherwise if it is, we parse it.
        - visited = set()   # set of airports we've found the min path to
        - greedily pick the shortest path to any node connected to nodes with known shortest paths to "explore" that node (establish its shortest path) and add its neighboring nodes to the heap

        general case: reachable
        4, [[0,1,1], [0,2,2], [1,2,5],[2,3,1]], 0, 3, 1 (2 edges/hops)
        min_cost = [(6, 2, 2), (3, 3, 2)]
        known = {0, 1, 2}
        adjlist = {0: [[1,1], [2,2]], 1: [[2,5]], 2: [[3, 1]]}
        returns 3

        general case: unreachable
        4, [[0,1,1], [0,2,2], [1,2,5],[2,3,1]], 0, 3, 0 (1 edges/hops)
        min_cost = []
        known = {0,1,2}
        adjlist = {0: [[1,1], [2,2]], 1: [[2,5]], 2: [[3, 1]]}
        returns -1

        Time complexity

        min cost with k hops = bellman ford

        min_cost[i][j] = min cost of reaching airport j using at most i edges (i is num edges cuz that is what we trying to build up)
        - build up from smaller num of edges
        min_cost[i][0] = 0
        min_cost[0][j != i] = inf
        min_cost[i][j] = 
        min(for all edges from neighbor k to airport j:
            min_cost[i-1][k] + cost[k to j]
        min_cost[k+1][dst] = answer
        '''
        # build adjlist: to airport -> [from airports]
        adjlist = defaultdict(list)
        for from_airport, to_airport, flight_cost in flights:
            adjlist[to_airport].append([from_airport, flight_cost])

        min_cost = [[float('inf') for _ in range(n)] for _ in range(k+2)] # 0 to k+1
        for max_hops in range(k+2):
            for airport in range(n):
                if airport == src:
                    min_cost[max_hops][airport] = 0
                elif max_hops == 0 and airport != src:
                    min_cost[max_hops][airport] = float('inf')
                else:
                    for neighbor, cost in adjlist[airport]:   # neighbor -> airport, airport -> [list of airports that fly TO it]
                        min_cost[max_hops][airport] = min(min_cost[max_hops][airport], min_cost[max_hops-1][neighbor] + cost)
        if min_cost[k+1][dst] == float('inf'):
            return -1
        return min_cost[k+1][dst]







        