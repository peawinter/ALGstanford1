import urllib2

class Solution1():
    def readData(self):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/dijkstraData.txt'
        file = urllib2.urlopen(url)
        dist = []
        for line in file:
            strLst = line.split('\t')
            del strLst[0]
            del strLst[-1]
            dist.append([])
            for str in strLst:
                dist[-1].append(map(int, str.split(',')))
                dist[-1][-1][0] -= 1
        return dist
    
    def initDist(self, dist):
        weight = [1000000] * 200
        weight[0] = 0
        for [idx, d] in dist[0]:
            weight[idx] = d
        return weight
    
    def updateDist(self, visited, weight, dist):
        nextd = 1000000
        nextptr = None
        for ptr, d in enumerate(weight):
            if not visited[ptr]:
                if d < nextd:
                    nextd = d
                    nextptr = ptr
        visited[nextptr] = True
        for [ptr, d] in dist[nextptr]:
            if not visited[ptr]:
                weight[ptr] = min(weight[ptr], nextd + d)
        return weight
    
    def Dist(self):
        dist = self.readData()
        weight = self.initDist(dist)
        visited = [False] * 200
        visited[0] = True
        while not all(visited):
            weight = self.updateDist(visited, weight, dist)
        return weight
    
    def main(self):
        weight = self.Dist()
        key = [7,37,59,82,99,115,133,165,188,197]
        rst = []
        for k in key:
            rst.append(str(weight[k - 1]))
        print (','.join(rst))
        
class Solution2:
    def readUndirectedGraph(self):
        adjlist = []
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/dijkstraData.txt'
        lines = urllib2.urlopen(url).read().splitlines()
        for line in lines:
            adjlist.append([])
            data = line.split()
            v = int(data[0])-1
            for tpl in data[1:]:
                ts, ws = tpl.split(',')
                t = int(ts)-1
                w = int(ws)
                adjlist[v].append((t, w))
        return adjlist
    
    def extract_min(self, pq, weights):
        i = 0
        j = 1
        m = weights[pq[0]]
        while j < len(pq):
            if weights[pq[j]] < m:
                i = j
                m = weights[pq[j]]
            j += 1
        res = pq[i]
        pq[i] = pq[-1]
        pq.pop()
        return res

    def dijkstraShortestPaths(self, graph, s):
        weights = [1000000]*len(graph)
        weights[s] = 0
        pqueue = [i for i in range(len(graph))]
        visited = [False]*len(graph)
        while len(pqueue) > 0:
            v = self.extract_min(pqueue, weights)
            visited[v] = True
            for inc, w in graph[v]:
                if not visited[inc]:
                    weights[inc] = min(weights[inc], weights[v]+w)
            if len(pqueue) == 199:
                print weight
        return weights
    
    def main(self):
        desired = [7,37,59,82,99,115,133,165,188,197]
        graph = self.readUndirectedGraph()
        weights = self.dijkstraShortestPaths(graph, 0)
        res = []
        for i in desired:
            res.append(str(weights[i-1]))
        print(','.join(res))

if __name__ == '__main__':
    print 'my method'
    sol1 = Solution1()
    dist = sol1.readData()
    weight = sol1.initDist(dist)
    sol1.main()
    print weight
    print 'others method'
    sol2 = Solution2()
    sol2.main()
