#include <stdio.h>
#include <stdlib.h>

void bar() { 
	char *p,*q;					/*Location 1*/
	q=malloc(1);				/*Location 2*/
	p=q;								/*Location 3*/
	*q='h';							/*Location 4*/
	*p='e';							/*Location 5*/
	printf("%c",*q);		/*Location 6*/
	q=malloc(1);				/*Location 7*/
  p=q;								/*Location 8*/
  *q='r';							/*Location 9*/
  *p='o';							/*Location 10*/
  printf("%c",*q);		/*Location 11*/
}

int main(void) {

	bar();

	return 0;
}