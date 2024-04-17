# 2019

### 1. Please answer the following questions: (12%) 

- (a.) What is the purpose of interrupts?
- (b.) What are the differences between a trap and an interrupt?
- (c.) What is the interrupt service routine? 

### 2. Please explain the following terms: (8%) 
- (a.) Polling I/O
- (b.) System Call
- (c.) DMA
- (d.) Time sharing System 


### 3. What is the main advantage of the microkernel approach to system design? How do user programs and system services interact in a microkernel architecture? What are the disadvantages of using the microkernel approach? (10%) 


### 4. Describe the differences among short-term, medium-term, and long-term scheduling. (10%) 


### 5. Please draw a diagram showing the life cycle of a process? (10%) 


### 6. Using the following C programs, identify the values of pid at lines A, B, C, and D. (Assume that the actual pids of the parent and child are 2600 and 2603, respectively.) (10%) 

```c
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid, pidi;
    
    pid = fork(); 
    if (pid < 0) { /* error occurred */
        fprintf(stderr, "Fork Failed");
        return 1;
    } else if (pid == 0) { /* child process */
        pidi = getpid();
        printf("child: pid - %d\n", pid); /* A */
        printf("child: pidi - %d\n", pidi); /* B */
    } else { /* parent process */
        pidi = getpid();
        printf("parent: pid - %d\n", pid); /* C */
        printf("parent: pidi - %d\n", pidi);
        // wait(NULL); // uncomment if you want the parent to wait for child
    }
    return 0;
}
```
