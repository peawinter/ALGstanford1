import bisect
import urllib2
import heapq


def readData():
    url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/Median.txt'
    file = urllib2.urlopen(url)
    data = []
    for line in file:
        data.append(int(line))
    return data

heap_low = None
heap_high = None

def MedianMaintenance_init():
    global heap_low, heap_high
    heap_low = []
    heap_high = []
    
def MedianMaintenance_insert(x):
    global heap_low, heap_high
    if (len(heap_low) == 0):
        heapq.heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heapq.heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -y)
        else:
            heapq.heappush(heap_low, -x)
            if len(heap_low) - len(heap_high) > 1:
                y = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, y)
    return -heap_low[0]

data = readData()
print data[:5]
medians = []
    
MedianMaintenance_init()

for x in data:
    median = MedianMaintenance_insert(x)
    medians.append(median)
    
print(reduce(lambda x,y: (x+y) % 10000, medians))
