# A faster solution for problem 6 part 1

import urllib2
import sys
import threading

def readData(self):
    # return sorted data
    url = 'https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt'
    file = urllib2.urlopen(url)
    data = []
    for line in file:
        data.append(int(line))
        # bisect.insort(bisect, int(line))
    return data

def TwoSum_HashTable(hashTable, lst, target):
    for x in lst:
        y = target-x
        if y in hashTable and x != y:
            return (x, y)
        return None

def main():
    data = readData()
    print data[:5]
    
    hashTable = dict()
    for x in data:
        hashTable[x] = True
    print('size:' + str(len(hashTable)))
        
    count = 0
    for t in range(-10000, 10000+1):
        if(TwoSum_HashTable(hashTable, data, t)):
            count += 1
    print('Via hash table: ' + str(count))
    

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target