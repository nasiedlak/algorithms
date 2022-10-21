import sys

instances = int(sys.stdin.readline())

for i in range(instances):

    cacheSize = int(sys.stdin.readline()) # maximum size of our cache
    cache = list() # list to represent our cacheSize

    numRequests = int(sys.stdin.readline()) # total number of requests
    requests = sys.stdin.readline().strip().split() # all requests

    # dict with all request at every index at which they appear
    indexes = dict()
    for i in range(len(requests)):
        if(requests[i] not in indexes):
            indexes[requests[i]] = list()
        indexes[requests[i]].append(i)

    # every iteration an index's list with i is removed
    # allows to track the next item to be removed
    # in case the cache is full
    faults = 0
    maxIndexInCache = -1
    itemToDelete = -1
    for i in range(numRequests):

        if(requests[i] in cache):
            indexes[requests[i]].remove(i)
            continue

        faults += 1

        if(len(cache) < cacheSize):

            cache.append(requests[i])
            indexes[requests[i]].remove(i)

            if(indexes[requests[i]][0] > maxIndexInCache):
                maxIndexInCache = indexes[requests[i]][0]
                itemToDelete = requests[i]
            continue

        cache.remove(itemToDelete)

        cache.append(requests[i])
        indexes[requests[i]].remove(i)

        if(len(indexes[requests[i]]) == 0):
            itemToDelete = requests[i]
            maxIndexInCache = cache[0][0]
        elif(indexes[cache[0]][0] > indexes[requests[i]][0]):
            maxIndexInCache = indexes[cache[0]][0]
            itemToDelete = cache[0]
        else:
            maxIndexInCache = indexes[requests[i]][0]
            itemToDelete = cache[1]

    print(faults)
