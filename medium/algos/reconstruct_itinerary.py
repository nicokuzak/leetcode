"""You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi"""

from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.d = {}
        for it in tickets:
            k, v = it
            if k in self.d.keys():
                self.d[k] = sorted(self.d[k] + [v])
            else:
                self.d[k] = [v]
        res = []
        stack = ['JFK']
        while stack != []:
            cur = stack[-1]
            if cur not in self.d.keys():
                res.append(cur)
                stack.pop()
            else:
                if self.d[cur] != []:
                    stack.append(self.d[cur][0])
                    self.d[cur] = self.d[cur][1:]
                else:
                    res.append(cur)
                    stack.pop()
        return res[::-1]