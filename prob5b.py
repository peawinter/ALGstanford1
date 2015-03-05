import urllib2

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
    sol2 = Solution2()
    sol2.main()