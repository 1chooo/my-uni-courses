# 2018

### 1. Please answer the following questions: (12%) 

- (a.) What is the purpose of interrupts?
- (b.) What are the differences between a trap and an interrupt?
- (c.) What is the interrupt service routine? 

### 2. Please explain the following terms: (8%) 
- (a.) Polling I/O
- (b.) System Call
- (c.) DMA
- (d.) Time sharing System 

### 3. What problem do caches solve? What problem do caches cause?

### 4. Please explain how "Context Switch" operates(5%) and describe at least four differences between process and thread.(5%)


### 5. Please draw a diagram showing the life cycle of a process?(5%)

### How may processes including the original process will the following C programs with the unix system call fork() create? Suppose all fork() system calls succeed. (5%)

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    int i; 
    for (i = 0; i < 2; i++) {
        if (fork() == 0) {
            fork();
            fork();
        }
    }

    return 0;
}
```

### 7. 
- a. Please list at least three Multithreading Models.(6%)
- b. What are two differences between user-level threads and kernel level threads?(4%) 

> [!TIP]
> Definition and thread sends blocking system call


### 8. Compared to processes, threads communicate with each other more easily. One of the reasons is that threads share certain memory segments. What's the three segments threads share?(6%) What's the two individual segments threads have?(4%)

### 9. Please explain multilevel feedback queue. (5%)

### 10. Please draw the Gantt charts and calculate the average waiting time for the following processes for the problems shown below.

- (A). Round-Robin, time quantum = 2
- (B). Shortest-remaning-time-first (preemptive SJF)

|  | Arrival Time | Burst Time |
| --- | --- | --- |
| P1 | 0 | 6 |
| P2 | 3 | 4 |
| P3 | 2 | 3 |
| P4 | 5 | 5 |
| P5 | 8 | 2 |

### 11. 

- (a)Please explain the critical-section and race condition problem. (4%)
- (b)Please explain how "Disable Interrupt" and "Critical Section Design" solve race condition problemin kernel space. [假設processor 為沒有 hardware memory protection support 之 8088/8086 cpu] (6%)

### 12. 

- (A) Peterson's solution is a classic software-based solution to the critical-section problem. Please fill in the blanks in the Peterson's solution. (Algorithm for Process Pi)
- (B) Please explain why the following algorithm does not satisfy the requirement for the critical-section design.

```c
do {
    flag[i] = TRUE;
    turn = ___;   // Tip: i or j
    while (___________);   // flag[?] && turn == ?
      // critical section
    flag[i] = ____;   // Tip: True or False
        // remainder section
} while (TRUE);
```

- (B) N process using Test & Set atomic operation