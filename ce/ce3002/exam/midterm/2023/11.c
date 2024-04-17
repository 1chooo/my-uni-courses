#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/wait.h>

static void *runner(void *param) {
    (*(int*)param)--;
    pthread_exit(0);
}

int main(int argc, char **argv) {
    int value = 11;
    pid_t pid = fork();
    if (pid > 0) {
        int status;
        waitpid(-1, &status, 0);
        printf("A=%d\n", value--);
    } else if (pid == 0) {
        pid_t pid = fork();
        if (pid > 0) {
        
        }
    }









            else {
                printf("D=%d\n", ++value);
            }
        } else {
            return 1;
        }
    } else {
        return 1;
    }
    return 0;
}