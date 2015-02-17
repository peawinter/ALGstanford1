# your code goes here
# import the data
import random
import copy
import urllib2
random.seed(1708)

# Tiral data
# data = [
#     [1, 2, 3, 4],
#     [2, 1, 3, 4, 5],
#     [3, 1, 2, 4],
#     [4, 1, 2, 3, 7],
#     [5, 2, 6, 7, 8],
#     [6, 5, 7, 8],
#     [7, 4, 5, 6, 8],
#     [8, 5, 6, 7]
# ]

# print data
# build the function
class Solution():
    def readData(self):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/kargerMinCut.txt'
        file = urllib2.urlopen(url)
        data = []
        for line in file:
            newop = line.split('\t')
            del newop[-1]
            data.append(map(int, newop))
        return data
    
    def readGraph(self):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/kargerMinCut.txt'
        file = urllib2.urlopen(url)
        graph = {}
        for line in file:
            newop = line.split('\t')
            del newop[-1]
            graph[int(newop[0])] = map(int, newop[1:])
        return graph
        
    def minCut(self, data):
        if len(data) < 2:
            return None
        # merge points into two sets
        nameList = [[idx] for idx in range(1, len(data) + 1)]
        # nameList = [[1, 2, 3, 4], [5, 6, 7, 8]]
        while len(nameList) > 2:
            [idx1, idx2] = random.sample(range(len(nameList)), 2)
            nameList[idx1] += nameList[idx2]
            del nameList[idx2]
        count = 0
        for p1 in nameList[0]:
            for p2 in data[p1 - 1]:
                if not p2 in nameList[0]:
                    count += 1
    	return [nameList, count]
    	
    def minCut2(self, graph):
        # random.seed(idx)
        if len(data) < 2:
            return None
        # random pick the merged nodes
        while len(graph) > 2:
            node1 = random.sample(graph.keys(), 1)[0]
            node2 = random.sample(graph[node1], 1)[0]
            for node in graph[node2]:
                if node != node1:
                    graph[node1].append(node)
                    graph[node].append(node1)
                graph[node].remove(node2)
            del graph[node2]
        key = graph.keys()[0]
        return len(graph[key])
        
sol = Solution()
data = sol.readData()
graph = sol.readGraph()
# print data
# print graph
minCount = len(data[0])
for idx in range(1000):
    graphCopy = copy.deepcopy(graph)
    count = sol.minCut2(graphCopy)
    minCount = min(count, minCount)
print minCount
