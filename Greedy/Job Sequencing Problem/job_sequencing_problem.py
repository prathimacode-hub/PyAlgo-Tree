# Problem Name: Job Sequencing Problem
# Approach used: Greedy Method
# Language used: Python

# Problem Statement: Given an array of jobs where every job has a deadline 
#                    and associated profit if the job is finished before the
#                    deadline. It is also given that every job takes a single
#                    unit of time, so the minimum possible deadline for any 
#                    job is 1. Maximize the total profit if only one job can
#                    be scheduled at a time.

# -----------------------------------------------------------------------------

# Constraints:
# arr[] -> Set of datapoints including JobID, Deadline and Profit into a single array.
# t -> No. of jobs to be scheduled.

# -----------------------------------------------------------------------------


def printJobScheduling(arr, t):
# This is the main funtion for determining the final result
# function to schedule the jobs take 2 arguments array and no of jobs to schedule
 
    # length of array
    n = len(arr)
 
    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    # To keep track of free time slots
    result = [False] * t
 
    # To store result (Sequence of jobs)
    job = ['-1'] * t
 
    # Iterate through all given jobs
    for i in range(len(arr)):
 
        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
 
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
 
    # print the sequence
    print(job)
 
 
# Driver's Code
if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print ("-- Job Sequencing Problem using Greedy Approach --")
    print ()
    print ("Job ID    Deadline     Profit")
    for i in range(0, len(arr)):
      for j in range (0, 3):
        print (arr[i][j], end = "           ")
      print()

    print ("\nOutput --")
    print("Following is maximum profit sequence of jobs")
 
    # Function Call
    printJobScheduling(arr, 3)

    
# -------------------------------------------------------------------------
   
# Output  
# -- Job Sequencing Problem using Greedy Approach --

# Job ID    Deadline     Profit
# a           2           100           
# b           1           19           
# c           2           27           
# d           1           25           
# e           3           15           

# Output --
# Following is maximum profit sequence of jobs
# c a e

# -------------------------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2022

# -------------------------------------------------------------------------
