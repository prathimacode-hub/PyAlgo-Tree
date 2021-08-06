# Round Robin Scheduling
## Aim
To implement Round Robin Scheduling

## Purpose
Round robin scheduling (RRS) is a preemptive algorithm that is considered to be very fair, as it uses time slices that are assigned to each process in the queue.

## Short description
- Round Robin is a CPU scheduling algorithm where each process is alloted in a given time slot in a cyclic manner.
- It is simple and easy to implement.
- It is one of the most commonly used technique in CPU scheduling.
- Round Robin Scheduling gives all processes equal access to the processors (this is called starvation-free job scheduling).
- A round-robin scheduler generally employs time-sharing, giving each job a time slot or quantum.
- Each process get a chance to reschedule after a particular quantum time in this scheduling.

## Workflow
- Completion Time: Time at which process completes its execution.
- Turn Around Time: Time Difference between completion time and arrival time. 
    - `Turn Around Time = Completion Time – Arrival Time`
- Waiting Time(W.T): Time Difference between turn around time and burst time.
    - `Waiting Time = Turn Around Time – Burst Time`

- Create an array rem_bt[] to keep track of remaining burst time of processes. 
- This array is initially a copy of bt[] 
- Create another array wt[] to store waiting times of processes. 
- Initialize this array as 0.
- Initialize time : t = 0
- Traversing all processes while all processes are not completed. 
- Do following for i'th process if it is not completed yet.
    - If rem_bt[i] > quantum
       - t = t + quantum
       - bt_rem[i] -= quantum;
    - Else 
       - t = t + bt_rem[i];
       - wt[i] = t - bt[i]
       - bt_rem[i] = 0; 
       
## Compilation Steps
- Download the file [Round_Robin_Scheduling](https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Scheduling/Round%20Robin%20Scheduling/Round_Robin_Scheduling.py)
- Run the file [Round_Robin_Scheduling](https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Scheduling/Round%20Robin%20Scheduling/Round_Robin_Scheduling.py)
- Initialize required number of processes as the list in the program.
- Specify Burst Time as a list in the program itself.
- Waiting time, Turn around time, Average waiting time, Average turn around time are our required outputs.
       
## Output
![image](https://user-images.githubusercontent.com/71583695/128535125-661ecd04-237e-4996-8e39-62ef1da420d8.png)
Image Pathlink : https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Scheduling/Round%20Robin%20Scheduling/images/Round_Robin_Scheduling_output1.jpeg

![image](https://user-images.githubusercontent.com/71583695/128535299-7696bae2-6b09-424a-831c-1eefdeb71cb6.png)
Image Pathlink : https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Scheduling/Round%20Robin%20Scheduling/images/Round_Robin_Scheduling_output2.jpeg

![image](https://user-images.githubusercontent.com/71583695/128535385-45761369-bb16-44b0-ae50-37e4f568ffb8.png)
Image Pathlink : https://github.com/manvitha3579/PyAlgo-Tree/blob/main/Scheduling/Round%20Robin%20Scheduling/images/Round_Robin_Scheduling_output3.jpeg


## Author:
[Manvitha Chowdary](https://github.com/manvitha3579)
