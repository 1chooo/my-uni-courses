#include <stdio.h>

void foo()
{
  int i = 50;
  printf("i in function foo is %d\n", i);
  return;
}

void ouo()
{
  int i;
  printf("i in function ouo is %d\n", i);
  return;
}

int main(void)
{

  int i = 10;
  printf("i in function main is %d\n", i);
  foo();
  ouo();
  return 0;
}

// 其實在 C 裡面 ouo 也可以拿到 foo 的 i，有興趣的人可以研究看看為什麼會這樣。