#include <stdio.h>
#include <setjmp.h>
#include <stdlib.h>

static jmp_buf buf;

void second(void) {
  printf("second\n");
  longjmp(buf, 1);        // jumps back to where setjmp was called - making setjmp now return 1.
}

void first(void) {
  second();
  printf("first\n");      // does not print
}

int main(void) {
  if (!setjmp(buf))
    first();              // Once executed, setjmp returns 0.
  else                    // Once longjmp jumps back, setjmp return 1
    printf("main\n");     

  return 0;
}