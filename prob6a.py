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
        url = 'https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt'
        file = urllib2.urlopen(url)
        data = []
        for line in file:
            newop = line.split('\t')
            data.append(map(int, newop)[0])
        return data
    
    def findOneNumber(self, data, target):
        dict = {}
        for num in data:
            if target - num in dict:
                print target - num, num
                return 1
            if not num in dict:
                dict[num] = num
        return 0
        
    def findAllNumbers(self, data):
        output = 0
        for target in range(-10000, 10001):
            output += self.findOneNumber(data, target)
        return output
        
sol = Solution()
data = sol.readData()
print data[:5]
output = sol.findAllNumbers(data)
print output
