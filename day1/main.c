#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>    //open
#include <unistd.h>   //read, write, close
#include <errno.h>    //errno
#include <sys/stat.h> //umask, stat
#include <time.h>     //ctime

int fuel_req(int mass)
{
    return mass / 3 - 2;
}

int main()
{
    char file_name[10] = "input.txt";

    struct stat meta_buff;
    stat(file_name, &meta_buff);

    char file_buff[meta_buff.st_size];
    int fd = open(file_name, O_RDONLY);
    read(fd, file_buff, sizeof(file_buff));

    int i;
    for (i = 0; i < meta_buff.st_size; i++)
    {
        printf("%d\n", file_buff[i]);
    }
    return 0;
}
