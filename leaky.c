#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {
    init();

    char flag[64];
    char name[16];

    memset(name, 0, sizeof(name));

    FILE* f = fopen("flag.txt", "r");
    if (!f) {
        perror("couldn't read the flag");
        return 0;
    }
    fgets(flag, sizeof(flag), f);

    puts("what's your name?");
    read(STDIN_FILENO, name, sizeof(name));

    printf("hi %s\n", name);
}
