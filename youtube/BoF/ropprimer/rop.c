#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv, char **argp)
{
    char name[32];
    printf("[+] ROP tutorial level0\n");
    printf("[+] What's your name? ");
    gets(name);
    printf("[+] Bet you can't ROP me, %s!\n", name);
    return 0;
}
