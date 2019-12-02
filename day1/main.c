#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>    //open
#include <unistd.h>   //read, write, close
#include <errno.h>    //errno
#include <sys/stat.h> //umask, stat
#include <time.h>     //ctime

int sub(int fuel) {
    if (fuel < 0)
        return 0;
    else
        return sub(fuel / 3 - 2) + fuel;
}

int solve(int part) {
    int SIZE = 100;
    int masses[SIZE];
    FILE *file = fopen("input.txt", "r");

    int i;
    int total = 0;
    for (i = 0; i < SIZE; i++) {
        fscanf(file, "%d", &masses[i]);
        int fuel = masses[i] / 3 - 2;
        if (part == 1)
            total += fuel;
        else
            total += sub(fuel);
    }

    fclose(file);

    return total;
}

int main() {
    printf("Answer to part 1: %d\n", solve(1));
    printf("Answer to part 2: %d\n", solve(2));
    return 0;
}
