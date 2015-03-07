from collections import defaultdict
from time import time
from itertools import groupby
import sys
import heapq
import urllib2
import resource

#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

class Solution():
    def readData(self):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt'
        file = urllib2.urlopen(url)
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
        nodes = sorted(list(nodes))
        return (graph, graphR, nodes)
        
    def myDFShelper(self, graphDict, node, leader):
        self.visited.add(node)
        for nextnode in graphDict[node]:
            if not nextnode in self.visited:
                self.myDFShelper(graphDict, nextnode, leader)
        self.count += 1
        self.finishtime[node] = self.count
        self.leader[node] = leader
        
    def myDFS(self, graphDict, nodes):
        for node in nodes:
            if not node in self.visited:
                self.myDFShelper(graphDict, node, node)
                
    def mySCC(self, graph, graphR, nodes):
        # DFS the reverse graph
        self.count = 0
        self.visited = set()
        self.leader = {}
        self.finishtime = {}
        self.myDFS(graphR, nodes)
        # DFS the original graph
        self.count = 0
        nodes = sorted(self.finishtime, key=self.finishtime.get, reverse=True)
        self.count = 0
        self.visited = set()
        self.leader = {}
        self.finishtime = {}
        self.myDFS(graph, nodes)
        # count the SCC
        output = defaultdict(list)
        for nodes, leader in self.leader.items():
            output[leader].append(nodes)
        return output
        
    def main(self):
        start = time()
        (graph, graphR, nodes) = self.readData()
        print time() - start
        output = self.mySCC(graph, graphR, nodes)
        print time() - start
        key5 = heapq.nlargest(5, output, key=lambda x: len(output[x]))
        result = []
        for i in range(5):
            try:
                result.append(len(output[key5[i]]))
            except:
                result.append(0)
        print time() - start
        return result
    
if __name__ == '__main__':
    sol = Solution()
    print sol.main()