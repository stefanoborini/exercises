#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int child(int i) {
    int *foo = 0x0;
    printf("Child %d\n", getpid());
    sleep(5);
    if (i == 5) {
        *foo = 42; /* if the process is the fifth of the bunch, do a segfault */
    }
    sleep(5);
    
}

int main() {
    int i;
    int report;
    pid_t pid[8];

    for (i=0; i < 8; i++) {
        pid[i] = fork();
        if (pid[i] == 0) { child(i); exit(0); }
    }

    for (i=0; i < 8; i++) {
        printf("parent waiting child %d\n", (int)pid[i]);
        waitpid(pid[i], &report, 0);
        printf("%d : %d : %d\n", pid[i], WIFEXITED(report), WTERMSIG(report));
    }
    
}

