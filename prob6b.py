import random
import bisect
import urllib2
random.seed(1708)

class Solution():
    def readData(self):
        url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/Median.txt'
        file = urllib2.urlopen(url)
        data = []
        for line in file:
            data.append(int(line))
        return data
    def median(self, lst):
        if len(lst) % 2 == 0:
            return (lst[len(lst) / 2 - 1] + lst[len(lst) / 2]) / 2.0
        return lst[len(lst) / 2]
        
    def insertSort(self, data):
        sortLst = []
        mediLst = []
        for num in data:
            bisect.insort(sortLst, num)
            mediLst.append(self.median(sortLst))
        print len(mediLst)
        return sum(mediLst) % 10000
    
sol = Solution()
data = sol.readData()
print data[:5]
print sol.insertSort(data)
