from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        input: 2D int list (points [[x, y],...])
        output: min cost to connect all points s.t no cycles
        (MST?)
        - cost of connecting two points is the manhattan dist (vertical+horizontal diff)

        Points are like nodes, edges are the manhattan dist between two points. 
        So for each pair of points, there exists an edge between them that costs their manhattan distance. we want to find the MST that touches all these points and return their cost.
        Prim's or kruskal's O(n^2) cuz we need to construct the edges lol
        kruskal's uses union find (f no)

        So we use Prim's (finding min edge that crosses the cut) using a heap???
        - connected = set()
        - not connected = set()
        - list of chosen edges?
        - greedily find the edge with min cost that cuts the sets
        - include this edge in our MST
        '''
        first_point = (points[0][0], points[0][1])
        connected = set(first_point)
        adjlist = defaultdict(list)    # map a point -> [(another point, cost), (), ()...]
        for i in range(len(points)):
            point1x, point1y = points[i]
            for j in range(i+1,len(points)):
                point2x, point2y = points[j]
                dist = abs(point1x - point2x)+abs(point1y - point2y)
                adjlist[(point1x, point1y)].append((point2x, point2y, dist))
                adjlist[(point2x, point2y)].append((point1x, point1y, dist))
       
        total_cost = 0
        min_cut = [(0, first_point[0], first_point[1])]    # heap (cost, potentially unconnected point)
        while min_cut:
            cost, pointx, pointy = heapq.heappop(min_cut)
            if (pointx, pointy) in connected:
                continue
            connected.add((pointx, pointy))
            total_cost += cost
            for neighborx, neighbory, cost in adjlist[(pointx,pointy)]:
                if (neighborx, neighbory) not in connected:
                    heapq.heappush(min_cut, (cost, neighborx, neighbory))
        return total_cost



        

        