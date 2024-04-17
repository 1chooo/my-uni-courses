#include <sys/types.h>
#include <sts/wait.h>
#include <stdio.h>
#include <unistd.h>


int main() {
    int value = 5;
    pid_t pid;
    pid = fork();
    value += 10;
    pid = fork();
    value += 10;

    if (pid == 0) {
        value += 15;
        return 0;
    } else if (pid > 0) {
        wait(NULL);
        printf("%d\n", value);  /* LINE A */
        return 0;
    }
}