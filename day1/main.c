#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>    //open
#include <unistd.h>   //read, write, close
#include <errno.h>    //errno
#include <sys/stat.h> //umask, stat

int sub(int fuel) { return (fuel < 0) ? 0 : sub(fuel / 3 - 2) + fuel; }

int solve(int part) {
    int SIZE = 100;
    int masses[SIZE];
    FILE * file = fopen("input.txt", "r");

    int i;
    int total = 0;
    for (i = 0; i < SIZE; i++) {
        fscanf(file, "%d", &masses[i]);
        int fuel = masses[i] / 3 - 2;
        total += (part == 1) ? fuel : sub(fuel);
    }

    fclose(file);

    return total;
}

int main() {
    printf("Answer to part 1: %d\n", solve(1));
    printf("Answer to part 2: %d\n", solve(2));
    return 0;
}
