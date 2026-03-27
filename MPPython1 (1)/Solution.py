from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        source = self.info['source']
        clients = self.info['clients']
        distance = {source: 0}
        parent = {source: None}
        pq = [(0, source)]

        while len(pq) > 0:
            n = heapq.heappop(pq)
            d = n[0]
            u = n[1]

            if d > distance.get(u, float('inf')):
                continue

            for v in self.graph.neighbors(u):
                weight = self.graph[u][v].get('delay', 1)
                newD = d + weight
                
                if newD < distance.get(v, float('inf')):
                    distance[v] = newD
                    parent[v] = u
                    heapq.heappush(pq, (newD, v))
        paths = {}
        for c in clients:
            path = deque()
            curr = c
            while curr is not None:
                path.appendleft(curr)
                curr = parent.get(curr)
            paths[c] = list(path)

        bandwidths, priorities = {}, {}
        return (paths, bandwidths, priorities)