import bisect
import urllib2
import heapq

class Solution():
    def __init__( self ):
        self.heap_low, self.heap_high = [], []
        
    def readData( self ):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/Median.txt'
        file = urllib2.urlopen(url)
        data = []
        for line in file:
            data.append(int(line))
        return data
    
    def MedianMaintenance_insert( self, x ):
        if (len(self.heap_low) == 0):
            heapq.heappush(self.heap_low, -x)
        else:
            m = -self.heap_low[0]
            if x > m:
                heapq.heappush(self.heap_high, x)
                if len(self.heap_high) > len(self.heap_low):
                    y = heapq.heappop(self.heap_high)
                    heapq.heappush(self.heap_low, -y)
            else:
                heapq.heappush(self.heap_low, -x)
                if len(self.heap_low) - len(self.heap_high) > 1:
                    y = -heapq.heappop(self.heap_low)
                    heapq.heappush(self.heap_high, y)
        return -self.heap_low[0]
    
    def MedianTrack( self ):
        data = self.readData()
        print data[:5]
        medians = []
        for x in data:
            medians.append(self.MedianMaintenance_insert(x))
        return reduce(lambda x, y: (x + y) % 10000, medians)
        
if __name__ == '__main__':
    sol = Solution()
    print sol.MedianTrack()