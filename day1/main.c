#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>    //open
#include <unistd.h>   //read, write, close
#include <errno.h>    //errno
#include <sys/stat.h> //umask, stat
#include <time.h>     //ctime

int main()
{
    int SIZE = 100;
    int masses[SIZE];
    FILE *file;

    file = fopen("input.txt", "r");

    int i;
    int total;
    for (i = 0; i < SIZE; i++)
    {
        fscanf(file, "%d", &masses[i]);
        total += masses[i] / 3 - 2;
    }

    fclose(file);

    printf("Answer to part 1: %d\n", total);

    return 0;
}
