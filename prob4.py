import urllib2

class Solution():
    def readData(self):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt'
        file = urllib2.urlopen(url)
        graph = []
        graphR = []
        for line in file:
            newop = line.split(' ')
            del newop[-1]
            [start, end] = map(int, newop)
            start -= 1
            end -= 1
            if len(graph) < start + 1:
                graph.append([])
            graph[-1].append(end)
        print graph[-5:]
        graphR = [[] * len(graph)]
        for start, lst in enumerate(graph):
            for end in lst:
                graphR[end].append(start)
        return (graph, graphR)
    
        
if __name__ == '__main__':
    sol = Solution()
    (graph, graphR) = sol.readData()
    print graph[:5]
    print graphR[:5]