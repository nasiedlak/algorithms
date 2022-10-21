import sys

instances = int(sys.stdin.readline())

for i in range(instances):

    numTasks = int(sys.stdin.readline()) # number of jobs
    tasks = list() # list of tuples contianing (start, end) elements

    # fills the tasks list with tuples
    tasks = [tuple(sys.stdin.readline().strip().split()) for i in range(numTasks)]

    if(len(tasks) == 1):
        print(1)
        continue

    # sort the list of tuples be end time
    tasks.sort(key = lambda x:int(x[1]))

    # count for all comptaible tasks
    schedule = 0

    # tracks the highest incompatible runtime
    incompatible = 0

    for task in tasks:
        # if the start time of the current task is
        # not in the list of incompatible times
        # then the task will be added to our schedule
        if(int(task[0]) >= incompatible):
            schedule += 1
            incompatible = int(task[1])

    print(schedule)
