# Round Robin scheduling

#----To calculate waiting time----
def findWaitingTime(processes, n, bt, wt, quantum):
	rem_bt = [0] * n

	for i in range(n):
		rem_bt[i] = bt[i] # Copy the burst time into rt[]
	t = 0 # present time

	#---traversing processes continues in robin manner until all of them are not done---
	while(1):
		done = True

		#---Traverse all processes one by one repeatedly---
		for i in range(n):
			
			if (rem_bt[i] > 0) : # If burst time of a process is greater than 0 then only need to process further
				done = False # There is a pending process
				
				if (rem_bt[i] > quantum) :
				
					t += quantum # Increase the value of t i.e. shows how much time a process has been processed

					rem_bt[i] -= quantum # Decrease the burst_time of current process by quantum
#---If burst time is smaller than or equal to quantum. Last cycle for this process---
				else:
					t = t + rem_bt[i] # Increase the value of t i.e. shows how much time a process has been processed

					wt[i] = t - bt[i] # Waiting time is current time minus time used by this process

					rem_bt[i] = 0 # As the process gets fully executed make its remaining burst time = 0
				
		#---If all processes are accomplished---
		if (done == True):
			break
			
#---calculation of turn around time---
def findTurnAroundTime(processes, n, bt, wt, tat):
	
	for i in range(n):
		tat[i] = bt[i] + wt[i] # Calculating turnaround time


#---calculating average waiting and turn-around times---
def findavgTime(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n

	#---Calculating waiting time for all processes---
	findWaitingTime(processes, n, bt, wt, quantum)

	#---Calculating turn around time for all processes---
	findTurnAroundTime(processes, n, bt, wt, tat)

	#---Display processes along with all details---
	print("Processes Burst Time	 Waiting", "Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	

if __name__ =="__main__":
	proc = [1, 2, 3]
	n = 3
	burst_time = [7, 3, 11]
	quantum = 2;
	findavgTime(proc, n, burst_time, quantum)
