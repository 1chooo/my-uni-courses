#include <stdio.h>
#include <stdlib.h>

int car() { 
	int e, f;
	e=7;
	f=8;
	return e+c+a;    //location 1
}

int bar() { 
	int c=4, d=5, e=6;
	c=car()+b;	//location 2
	a=5;				//location 3
	e=9;				//location 4
	return c;		//location 5
}

int main() { 
	int a, b, c;
	a=1;   			//location 6 
	b=2;   			//location 7 
	c=3;   			//location 8 
	b=bar()+c;  //location 9 
	return 1;   //location 10
}