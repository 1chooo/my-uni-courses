#include <stdlib.h>
#include <stdio.h>

void init() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	return;
}

int main() {
	init();
	char buf[150];

	puts("Input something in this buffer!!!");
	puts("However,you can't input 'nop' such as '0x90' this time!!!");
	puts("And also,you need to bypass some restrictions in your shellcode!!!");
	puts("This time the restrictions are very strict OAO!??");
	
	read(0, buf, 150);

	for (int i = 0; i < 150; i++) {
		if (buf[i] == '\x90') {
			puts("You can't input '0x90' this time!  :(( ");
			exit(0);
		}
	}

	for (int i = 0; i < 25; i++) {
		if (buf[i*6] != '\x0c' && buf[(i*6)+1] != '\x87' && buf[(i*6)+2] != '\x63') {
			puts("Try to bypass the restriction!!!");
			puts("Try again!!!");
			exit(0);
		}
	}

	void (*func)() = (void (*)())buf;
	(*func)();

	return 0;
}
