# A faster solution for problem 6 part 1

import urllib2
import sys

class Solution:
    def readData(self):
        # return sorted data
        url = 'https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt'
        file = urllib2.urlopen(url)
        data = []
        for line in file:
            data.append(int(line))
            # bisect.insort(bisect, int(line))
        return data
    
    def hashData(self, data):
        hashTable = dict()
        for x in data:
            hashTable[x] = True
        print 'Size of hashtable', len(hashTable)
        return hashTable
    
    def count2SumTarget(self, data, hashTable, target):
        for x in data:
            if target - x in hashTable:
                return True
        return False
    
    def count2SumAll(self):
        data = self.readData()
        print data[:10]
        hashTable = self.hashData(data)
        output = []
        for target in range(-10000, 10001):
            if self.count2SumTarget(data, hashTable, target):
                output.append(target)
        print output
        return len(output)
        
if __name__ == '__main__':
    sol = Solution()
    count = sol.count2SumAll()
    print count