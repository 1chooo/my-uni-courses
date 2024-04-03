# CPU Scheduling



## Basic Concepts

- Maximum CPU utilization obtained with multiprogramming
- CPU–I/O Burst Cycle – Process execution consists of a cycle of CPU execution and I/O wait
- CPU burst followed by I/O burst
- CPU burst distribution is of main concern

![alt text](image.png)

### Histogram of CPU-burst Times

- Large number of short bursts
- Small number of longer bursts


![alt text](image-1.png)

### CPU Scheduler

- The CPU scheduler selects from among the processes in ready queue, and allocates a CPU core to one of them
  - Queue may be ordered in various ways
- CPU scheduling decisions may take place when a process:
    1.	Switches from running to waiting state
    2.	Switches from running to ready state
    3.	Switches from waiting to ready
- Terminates
- For situations 1 and 4, there is no choice in terms of scheduling. A new process (if one exists in the ready queue) must be selected for execution. 
- For situations 2 and 3, however, there is  a choice.

### Preemptive and Nonpreemptive Scheduling

- When scheduling takes place only under circumstances 1 and 4, the scheduling scheme is nonpreemptive.
- Otherwise, it is preemptive. 
- Under Nonpreemptive scheduling, once the CPU has been allocated to a process, the process keeps the CPU until it releases it either by terminating or by switching to the waiting state. 
- Virtually all modern operating systems including Windows, MacOS, Linux, and UNIX use preemptive scheduling algorithms.


## Scheduling Criteria 


## Scheduling Algorithms


## Thread Scheduling


## Multi-Processor Scheduling


## Real-Time CPU Scheduling


## Operating Systems Examples


## Algorithm Evaluation
