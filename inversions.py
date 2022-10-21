import sys

instances = int(sys.stdin.readline())

for i in range(instances):

    length = int(sys.stdin.readline())
    nums = sys.stdin.readline().split()

    def count(nums1, nums2):

        c = 0
        for i in range(len(nums1)):
            if(nums1[i] > nums2[i]):
                c += 1
        return c

    def inversion(numbers):
        
        if(len(numbers) == 1):
            return (0)

        c = 0
        c1 = 0
        c2 = 0

        a1 = numbers[:((len(numbers) // 2))]
        a2 = numbers[((len(numbers) // 2)):]

        c1 = inversion(a1)
        c2 = inversion(a2)
        c = count(a1, a2)

        return (c + c1 + c2)

    print(inversion(nums))
