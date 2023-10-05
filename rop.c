#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

char flag[64];

int load_flag() {
    FILE* f = fopen("flag.txt", "r");
    if (!f) {
        perror("couldn't read the flag");
        return -1;
    }
    fgets(flag, sizeof(flag), f);
    return 0;
}

void print_flag() {
    puts(flag);
}

void vuln() {
    char buf[8];
    gets(buf);
}

int main() {
    init();
    puts("hello!");
    vuln();
}
