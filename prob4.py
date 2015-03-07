from collections import defaultdict
from time import time
from itertools import groupby
import heapq
import urllib2
import resource

class Tracker(object):
    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()
    
class Solution():
    def readData(self):
        # url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt'
        # file = urllib2.urlopen(url)
        file = open('prob4test1.txt')
        graph = defaultdict(list)
        graphR = defaultdict(list)
        nodes = set()
        for line in file:
            newop = line.split(' ')
            [start, end] = map(int, newop[0:2])
            graph[start].append(end)
            graphR[end].append(start)
            nodes.add(start)
            nodes.add(end)
        print graph[1]
        print graphR[1]
        nodes = sorted(list(nodes), reverse = True)
        return (graph, graphR, nodes)
    
    def dfs(self, graph_dict, node, tracker):
        """Inner loop explores all nodes in a SCC. Graph represented as a dict,
        {tail: [head_list], ...}. Depth first search runs recursively and keeps
        track of the parameters"""
        tracker.explored.add(node)
        tracker.leader[node] = tracker.current_source
        for head in graph_dict[node]:
            if head not in tracker.explored:
                self.dfs(graph_dict, head, tracker)
        tracker.current_time += 1
        tracker.finish_time[node] = tracker.current_time
    
    def dfs_loop(self, graph_dict, nodes, tracker):
        for node in nodes:
            if node not in tracker.explored:
                tracker.current_source = node
                self.dfs(graph_dict, node, tracker)
    
    def scc(self, graph, graphR, nodes):
        """First runs dfs_loop on reversed graph with nodes in decreasing order,
        then runs dfs_loop on original graph with nodes in decreasing finish
        time order(obtained from first run). Return a dict of {leader: SCC}."""
        out = defaultdict(list)
        tracker1 = Tracker()
        tracker2 = Tracker()
        # dfs reverse graph with nodes in decreasing order
        self.dfs_loop(graphR, nodes, tracker1)
        sorted_nodes = sorted(tracker1.finish_time,
                              key=tracker1.finish_time.get, reverse=True)
        # dfs graph with nodes in decreasing finish time order
        self.dfs_loop(graph, sorted_nodes, tracker2)
        for lead, vertex in groupby(sorted(tracker2.leader, key=tracker2.leader.get),
                                    key=tracker2.leader.get):
            out[lead] = list(vertex)
        return out
    
    def main(self):
        start = time()
        (graph, graphR, nodes) = self.readData()
        print time() - start
        print graph
        print graphR
        print nodes
        output = self.scc(graph, graphR, nodes)
        print output
        return output
    
if __name__ == '__main__':
    sol = Solution()
    sol.main()