作業系統 期中作業
1. Please explain following terms
- a. System call
- b. bootstrap program
- c. Time sharing
- d. Real time
- e. Virtual machine
2. Including the initial parent process, how many processes are created by the
following program? Justify your answer by drawing a tree of processes.
```c
#include <stdio.h>
#include <unistd.h>

int main() {
    fork();
    fork();
    fork();
    return 0;
}
```
3. What is the purpose of interrupts? What are the differences between a trap and
an interrupt? Can traps be generated intentionally by a user program? If so, for
what purpose?

4. Please explain how “Context Switch” operates and describe at least four
differences between process and thread.

5. Please describe Process Control Block with the information of each process.

6. Please draw a diagram showing the life cycle of a process?

7. List the reasons why we use cooperating processes and the way that processes
communicate(Two model of IPC).

8. Please describe the differences between the long-term scheduling and the short-
term scheduling.

9. Describe three general methods for passing parameters to the operating
system.

10.  Please explain how "Disable Interrupt" and C"ritical Section Problem" solve race
condition problem