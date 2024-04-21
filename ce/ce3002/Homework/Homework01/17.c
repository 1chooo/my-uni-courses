#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *thread_function(void *arg) {
    printf("Thread created\n");
    pthread_exit(NULL);
}

int main() {
    pid_t pid;

    pid = fork();
    if (pid == 0) { /* child process */
        fork();
        pthread_t tid;
        pthread_create(&tid, NULL, thread_function, NULL);
    }
    fork();

    printf("Process with PID %d created\n", getpid());

    return 0;
}
