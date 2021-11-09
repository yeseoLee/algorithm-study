#재귀
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #define graph by defaultdict
        graph=defaultdict(list)
        for a,b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = [] 
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
                    
        dfs("JFK")
        return route[::-1]

#재귀를 반복으로
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #define graph by defaultdict
        graph=defaultdict(list)
        for a,b in sorted(tickets):
            graph[a].append(b)
        
        route,stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]
