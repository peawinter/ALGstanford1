# A faster solution for problem 6 part 1

import urllib2
import sys
from time import time

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

    def two_sum(array):
        WIDTH = 10000
        out = set()
        for i in array:
            lower = bisect.bisect_left(array, -WIDTH - i)
            upper = bisect.bisect_right(array, WIDTH - i)
            out |= set([i + j for j in array[lower:upper]])
        return out

    def main():
        data = self.readData()
        data.sort()
        print data[:10]
        return len(two_sum(data))


if __name__ == '__main__':
    sol = Solution()
    start = time()
    print sol.main()
    print time() - start