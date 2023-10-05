#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void win() {
    asm(
            "andq $-16, %rsp"
    );

    char flag[64];
    FILE* f = fopen("flag.txt", "r");
    if (!f) {
        perror("couldn't read the flag");
        return;
    }
    fgets(flag, sizeof(flag), f);
    puts(flag);
}

int main() {
    init();

    char buf[16];

    puts("hello!");
    fgets(buf, 48, stdin);
}

