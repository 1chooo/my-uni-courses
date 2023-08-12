#include <stdio.h>

void foo() {
  int a, b, i;
  char inputString[1000];

  i = 1;
  a = 2;
  b = 3;

  gets(inputString);
  printf(inputString, i);
}

int main() {
  int x = 100;
  int y = 200;

  foo();

  return 0;
}

/*
 * Input: %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d
 * Output: 1 0 154855084 1414400760 0 42 3 622879781 543434016 1680154724 622879781 543434016 -1105940568
 */