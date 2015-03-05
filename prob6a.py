import urllib2

class Solution():
    def readData(self):
        url = 'https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt'
        file = urllib2.urlopen(url)
        data = []
        for line in file:
            data.append(int(line))
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
        dict = {}
        targets = {}
        for num in range(-10000, 10000):
            targets[num] = 0
        for idx, num in enumerate(data):
            print idx
            for target in targets.keys():
                if target - num in dict:
                    print target
                    targets[target] += 1
            if not num in dict:
                dict[num] = num
        for target in targets.keys():
            if targets[target] >= 1:
                output += 1
        return output
        
sol = Solution()
data = sol.readData()
print data[:5]
output = sol.findAllNumbers(data)
print output
