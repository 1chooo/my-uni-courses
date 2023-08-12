// A C program to demonstrate static scoping.
#include<stdio.h>
int x = 10;

// Called by g()
int f()
{
return x;
}

// g() has its own variable
// named as x and calls f()
int g()
{
int x = 20;
return f();
}

int main()
{
printf("%d", g());
printf("\n");
return 0;
}
