"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

from typing import List
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = {} #edge: [[edge, weight], [edge, weight]]
        for time in times:
            u, v, w = time
            if u in d.keys():
                if v != k:
                    d[u][v] = w
            else:
                d[u] = {v:w}

        avail = [[0,k]] # Those we can currently get to
        seen = set() # Those we have seen
        
        while avail != []:
            time, node = heappop(avail)
            
            if node in seen:
                continue
            
            seen.add(node)
            
            if len(seen) == n:
                return time
            
            
            
            if node in d.keys():
                for no,t in d[node].items():
                    if no not in seen:
                        heappush(avail, [time+t, no])
        return -1