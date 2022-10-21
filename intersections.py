import sys

instances = int(sys.stdin.readline())

for i in range(instances):

    # total number of pairs
    n = int(sys.stdin.readline())

    # will be a list of tuples containing every pairs
    pairs = list()

    # insert every q point
    for q in range(n):
        pairs.append((int(sys.stdin.readline()),))

    # insert every p point
    for p in range(n):
        pairs[p] += (int(sys.stdin.readline()),)


    # sort by q values
    pairs = sorted(pairs, key = lambda x: x[0])

    def merge(a1, a2):

        pairs_merged = list()
        c = 0

        while(True):

            if(len(a1) == 0):
                pairs_merged += a2
                break

            if(len(a2) == 0):
                pairs_merged += a1
                break

            if(a1[0][1] < a2[0][1]):
                pairs_merged.append(a1[0])
                a1.pop(0)
            else:
                pairs_merged.append(a2[0])
                a2.pop(0)
                c += len(a1)

        return pairs_merged, c

    def count(a):

        l = len(a)

        if(l == 1):
            return a, 0

        a1, c1 = count(a[:(l // 2)])
        a2, c2 = count(a[(l // 2):])

        a3, c3 = merge(a1, a2)

        return a3, (c1 + c2 + c3)

    print(count(pairs)[1])
