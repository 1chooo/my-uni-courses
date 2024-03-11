#include <stdio.h>

void foo() {
  char stringInput[100];

  gets(stringInput);
  printf("StringInput: %s\n", stringInput);
}

int main() {
  foo();
  return 0;
}
