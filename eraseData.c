/*
    hard-erase data from a file by overwriting it with all zeros,
    the how much need to be erased is determined by the file size
    (overwrite all bytes in the file)

    define a MAX_BUFFER_SIZE to limit the size of the buffer,
    if file size is larger than MAX_BUFFER_SIZE, then the file
    will be erased in multiple passes
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define MAX_BUFFER_SIZE 1024


int main(int argc, char *argv[])
{
    FILE *fp;
    char *filename;
    long int filesize;
    char *buffer;
    int i;

    if (argc != 2)
    {
        printf("Usage: %s filename \r", argv[0]);
        return 1;
    }

    filename = argv[1];

    fp = fopen(filename, "rb");
    if (fp == NULL)
    {
        printf("Error: %s\r", strerror(errno));
        return 1;
    }

    fseek(fp, 0, SEEK_END);
    filesize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    buffer = (char *)malloc(MAX_BUFFER_SIZE);

    if (buffer == NULL)
    {
        printf("Error: %s\r", strerror(errno));
        return 1;
    }

    memset(buffer, 0, MAX_BUFFER_SIZE);

    for (i = 0; i < filesize; i += MAX_BUFFER_SIZE)
    {
        fwrite(buffer, 1, MAX_BUFFER_SIZE, fp);
    }

    fclose(fp);

    return 0;
}

// compile: gcc -o eraseData.exe eraseData.c

