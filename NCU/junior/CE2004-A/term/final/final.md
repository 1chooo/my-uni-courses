# Final

What follows is a C program excerpt.
```c
void bar() { 
    int tuv[10][10];
        :
        : 
}
```
(a) If we do not consider whether we can change the value of variable tuv, what other properties does the value of tuv have?  
(b) Could we change the value of tuv?  
(c) Could we change the value of tuv[1]?  
(d) Could we change the value of tuv[1][1]?

**Ans.**  
(a)   
(b) No. Since array name is a constant. ISO C prohibit array assignment.   
(c) No. tuv[1] is single dimension array name, which is a constant.  
(d)	Yes. tuv[1][1] is the element of array tuv.  


What follows is a Java program excerpt.
```java
class Circle {
  int setVariable(int s) { 
    int r;
    r=6;
    return s+r; 
  }
}

public class xyz{
    :
	public static void main(String [] args) { 
		Circle tuv[][]=new Circle[10][10];
				: 
	}
}
```
(a) What data type does tuv have?  
(b) What data type does tuv[1] have?  
(c)	Could we change the value of tuv?  
(d)	Could we change the value of tuv[1]?  
(e)	Could we change the value of tuv[1][1]?  


**Ans.**  
(a)  
(b)   
(c)	Yes. tuv is a reference to an int[10][10] object.  
(d)	Yes. tuv[1] is a reference to an int[] object.  
(e)	Yes. tuv[1][1] is a reference to an integer.  


The following C program can be compiled successfully. But what error does the following program have?
```C
#include<stdio.h>
main() { 
  int *p;
  *p=100;
}
```

**Ans.**  
The pointer p didn't initialize correctly. Hence, it will point to somewhere in memory we don't know. But OS won't let it change the value in that memory which not belongs to the program.


C, C++, and Fortran do not specify range checking of array subscripts. Assume a C compiler allocates memories for arrays declared in the same declaration statement in adjacent areas. For example for the following declaration statement, int t[10], u[10], v[10];, the compiler allocates memory for array t first. The memory of array u’is right after the memory of array t. The memory of array v’is right after the memory of array u. Assume the compiler utilizes row major order to store elements in an array. What follows is a C program.
```c
#include<stdio.h>
main() { 
    int a[10][10], b[10][10], c[10][10];
    int i,j;
    for(i=0;i<10;i++)
        for(j=0;j<10;j++) { 
            a[i][j] = 1;
            b[i][j] = 2;
            c[i][j] = 3;
        }
        b[17][9]=4;     /*location 1*/
        b[17][16]=5;    /*location 2*/
        b[-3][7]=6;     /*location 3*/
        b[-3][-6]=7;    /*location 4*/
    }
}
```
(a)	The value of which array element will be changed by the statement at location 1?  
(b)	The value of which array element will be changed by the statement at location 2?  
(c)	The value of which array element will be changed by the statement at location 3?  
(d)	The value of which array element will be changed by the statement at location 4?  


**Ans.**
(a)	a[7][9].  
(b)	a[8][6].  
(c)	c[7][7].  
(d)	c[6][4].  


In the following C program excerpt,   
(a)	what problem does this program have?  
(b)	why does this problem happen?  
(c) what security problem does it have?  
(d)	why does this problem happen?  
```c
#define BufferSize 60

char *poi = "The summer break is around the corner.";
char sentence[BufferSize];

int ppp(char *s, char *d, unsigned len) { 
    unsigned i;
    for( i=0 ;i<len; ++i ) {
        *(d+i)=*(s+i);
    }
}
void goo(char *s, char *d, int length) {
   if(length < BufferSize)
        ppp(poi,sentence,length); 
}
```

**Ans.**  
(a)	If the parameter length of goo() function is a negative signed integer, ppp() function will give back  some very long memory value in character pointer d, which will cause serious security hazard by reading illegal memory.  
(b)	The parameter length of goo() function is int data type. However, the parameter len of ppp() function is unsigned data type. If we give a negative signed integer to length of goo(), ppp(poi,sentence,length); will implicitly convert signed length variable into unsigned len variable which will be super large value in unsigned integer binary format.  
(c) If the value of length is a negative number, then function ppp() will copy a long character sequence into the limited array sentence, then all data adjacent to array sentence will be overwritten.  
(d) Type checking is not enforced upon a formal parameter and its corresponding actual parameter.


(a) 
```java
String s=new String("Welcome");
```
Assume the above statement is contained in a Java program and "Welcome" does not appear in any other statement in the program, how many String objects are created by this Java statement?
(b)  
```java
String t=new String("Welcome"); // statement 1
String s=new String("Welcome"); // statement 2
```
Assume the above two Java statements are contained in a Java program and statement 1 is right before statement 2, how many String objects are created by statement 2?

**Ans.**  
(a)	2. One is a string object in normal heap, and another is “Welcome” literal in string constant pool.  
兩個，一個在 heap 記憶體區塊，另一個則是在 String constant pool 區塊。  
(b)	1. Only one new string object in normal heap. The “Welcome” literal in string constant has already existed.  
一個，只有一個在 heap 區塊，因為 String constant pool 區塊已經建立一個名為 "Welcome" 的記憶體  


In the following C program,   
(a)	Right after the execution of the statement commented as "Location 1" is finished, do variable f and i have the same value?  
(b) Right after the execution of the statement commented as "Location 2" is finished, do variable f and i have the same value?  
(c) Explain the results of (a) and (b).(P.S.: You can execute this program and observe the results to get your answers.)  
```c
#include<stdio.h>
main() {
  float f;
  int   i;
  
  i=0.07;
  f=i;                          /*Location 1*/
  f=3.57;
  i=f;                          /*Location 2*/
}
```

**Ans.**  
(a)	Yes. Both i and f will be 0.  
他們會相同，因為 i 的型別是 int type，如果 assign 0.07 的話，數值會變 0，如果把 0 assign 給 f，值同樣也是 0。  
(b)	No. f is 3.57 and i is 3.  
他們不會一樣，因為 f 是 float type，如果 assign 3.57，那數值會變 3.57 ，但如果把 3.57 assign 給 int type 的 i ，數值會變成 3 ，所以他們不會相同。
(c)	The assignment between different data type (e.g. integer and floating point number) will lead to the precision of value loss.  
(c_v2) When assignment a value (e.g. an integer value) to a varialbe with a different type (e.g. a floating point type), the precision of the value will lose.  
如果 assign 不同型別，會有數值丟失的問題（這便就拿上述兩題做舉例）


What follows is a C program named `test_address.c`.
```c
#include <stdio.h>
int t;
int *p;
main() { 
	int q ;
	t=987 ;
	p=&t;
	printf("Hello \n"); 		/* location 1 */
}
```
Assume after program `test_address.c` is compiled by a C compiler, the addresses of variables t and p are 678 and 123 respectively. Then after the program is executed and the execution flow arrives at **location 1**, what are the values of `&p, p, and*p` respectively?

**Ans.**  
The value of &p, p and *p is 123, 678 and 987 repectively.

| &p            | p                 | *p                      |
| ------------- | ----------------- | ----------------------- |
| 123           | 678               | 987                     |
| adderess 不變 | p 是 t 的 address | p 指向 t address 的數值 |


Consider the following program:

```pascal
procedure Main is
	X, Y, Z : Integer; 
	procedure Subl is
    A, Y, Z : Integer;
  begin -- of Subl
		...
	end; -- of Subl 
	procedure Sub2 is
    A, B, Z : Integer;
  begin -- of Sub2
		...
	end; -- of Sub2 
	procedure Sub3 is
    A, X, W : Integer;
  begin -- of Sub3
		...
	end; -- of Sub3
begin -- of Main 
	...
end; -- of Main
```

List all the variables, along with the program units where they are declared, that are visible in the bodies of Subl, Sub2, and Sub3, assuming static scoping is used.

**Ans.**  
Sub1: A -> Sub1, X -> Main, Y -> Sub1, Z -> Sub1  
Sub2: A -> Sub2, B -> Sub2, X -> Main, Y -> Main, Z -> Sub2  
Sub3: A -> Sub3, X -> Sub3, Y -> Main, Z -> Main, W -> Sub3  


Consider the following program:

```pascal
procedure Main is
	X, Y, Z : Integer; 
	procedure Subl is
    A, Y, Z : Integer;
  begin -- of Subl
		...
	end; -- of Subl 
	procedure Sub2 is
    A, B, Z : Integer;
  begin -- of Sub2
		...
	end; -- of Sub2 
	procedure Sub3 is
    A, X, W : Integer;
  begin -- of Sub3
		...
	end; -- of Sub3
begin -- of Main 
	...
end; -- of Main
```
Given the following calling sequences and assuming that dynamic scoping is used, what variables are visible during execution of the last subprogram activated? Include with each visible variable the name of the unit where it is declared.  
(a) `Main` calls `Subl`; `Subl` calls `Sub2`; `Sub2` calls `Sub3`.  
(b) `Main` calls `Subl`; `Subl` calls `Sub3`.  
(c) `Main` calls `Sub2`; `Sub2` calls `Sub3`; `Sub3` calls `Subl`.  
(d) `Main` calls `Sub3`; `Sub3` calls `Subl`.  
(e) `Main` calls `Subl`; `Subl` calls `Sub3`; `Sub3` calls `Sub2`.
(f) `Main` calls `Sub3`; `Sub3` calls `Sub2`; `Sub2` calls `Subl`.

**Ans.**  
把程式流程寫出來，最後 call 的 function 變數就是他的  
(a)	A -> Sub3, B -> Sub2, X -> Sub3, Y -> Sub1, Z -> Sub2, W -> Sub3  
(b)	A -> Sub3, X -> Sub3, Y -> Sub1, Z -> Sub1, W -> Sub3  
(c)	A -> Sub1, B -> Sub2, X -> Sub3, Y -> Sub1, Z -> Sub1, W -> Sub3  
(d)	A -> Sub1, X -> Sub3, Y -> Sub1, Z -> Sub1, W -> Sub3  
(e)	A -> Sub2, B -> Sub2, X -> Sub3, Y -> Sub1, Z -> Sub2, W -> Sub3  
(f)	A -> Sub1, B -> Sub2, X -> Sub3, Y -> Sub1, Z -> Sub1, W -> Sub3  


In the C following C program,  
(a) Right after the execution of the statement commented as "Location 1" is finished, do variable j, h, and g  have the same value?  
(b) Right after the execution of the statement commented as "Location 2" is finished, do variable j, h, and g have the same value?  

```c
#include <stdio.h>
main() {
    float c, d, e, f, g, h;
    int i, j, k;
        :
        :
}
```

**Ans.**  
(a) h and j have the same value, but g has a different value.  
(b) Yes.  


What follows is a C program.
```c
#include<stdio.h>
#define SMALL_NUMBER_1 0.000007 
#define SMALL_NUMBER_2 0.000009

main() {
	float a, b, c, d, e; 
	a=SMALL_NUMBER_1;
	b=c=SMALL_NUMBER_2;
	printf("a=%f\n",a);
	d=(a/(b*b*b*b*b*b*b*b*b*b)); 							/*location 1*/
	e=(a/(b*b*b*b))*(c/(b*b*b*b))*(c/(b*b)); 	/*location 2*/
	d=d*c*c;																	/*location 3*/
	printf("(1)d = %f\n",d);									/*location 4*/
	printf("(2)e =%f\n",e);										/*location 5*/
}
```
(a) From the point of view of mathematics, the computation executed by the statement at location 1 and the statement at location 3 together is equivalent to the computation executed by the statement at location 2. In other words, the expression consisted of the statements at locations 1 and 3 is equivalent to the expression consisted of the statement at location 2. Hence, when the statement at location 3 is completed, variable d and variable e are supposed to have the same value. But statements at location 4 and location 5 show that variables d and e have different values? Explain the reason.  
(b) Write a C program as the above one to find two equivalent expressions with different evaluation orders that have different values. (P.S.: You must paste your program and its execution result on your answer sheet.)  

**Ans.**  
(a) Usually a computer can only store the approximate value of a real number, not a accurate value. The inaccuracy increases when operations are performed on the real variables.  
通常電腦只能存取近似值，而沒有辦法存取精確值，所以存取實數時準確性會下降。  
(b)  
```c
/**
 * @file q7_b.c
 * @author Hugo ChunHo Lin
 * @brief 
 * Write a C program as the above one 
 * to find two equivalent expressions 
 * with different evaluation orders 
 * that have different values. 
 * (P.S.: You must paste your program 
 * and its execution result on your answer sheet.)  
 * @version 0.1
 * @date 2023-05-24
 * 
 * @copyright Copyright (c) 2023
 */

/*
 * The expression:
 * 1. expression1 = (a + b) * c: Addition followed by multiplication
 * 2. expression2 = a * c + b * c: Multiplication followed by addition
 * 3. a / a * a / a * a / b
 * The output:
 * a = 3.000000, b = 2.000000, c = 4.000000
 * Expression 1: (a + b) * c = 20.000000
 * Expression 2: a * c + b * c = 20.000000
 */

#include <stdio.h>
#include <stdlib.h>

#define SMALL_NUMBER_1 0.000007 
#define SMALL_NUMBER_2 0.000009

int main() {
  float a = 3.0, b = 2.0, c = 4.0;
  float expression1, expression2;

  printf("a = %f, b = %f, c = %f\n", a, b, c);

  expression1 = (a + b) * c;    
  expression2 = a * c + b * c;  
  printf("Expression 1: (a + b) * c = %f\n", expression1);
  printf("Expression 2: a * c + b * c = %f\n", expression2);

  return 0;
}
```


What are the advantages of named constants?  

**Ans.**  
(a) Named constants are useful as aids to readability and program reliability.  
變數的命名在幫助程式的可讀性、維護性都有非常重要地幫助。  
(b) Named constants can aid modifiability.


Consider the following skeletal C program:  
```c
void funl(void);    /* prototype */
void fun2(void);    /* prototype */
void fun3(void);    /* prototype */
void main() { 
    int a, b, c;
        :
}
void funl(void) { 
    int b, c, d;
        :
}
void fun2(void) { 
    int c, d, e;
        :
}
void fun3(void) { 
    int d, e, f;
        :
}
```
Given the following calling sequences and assuming that dynamic scoping is used, what variables are visible during execution of the last function called? Include with each, visible variable the name of the function in which it was defined.  
(a) main calls funl; funl calls fun2; fun2 calls fun3.  
(b) main calls funl; funl calls fun3.  
(c) main calls fun2; fun2 calls fun3; fun3 calls funl.   
(d) main calls fun3; fun3 calls funl.
(e) main calls funl; funl calls fun3; fun3 calls fun2.   
(f) main calls fun3; fun3 calls fun2; fun2 calls funl. Ans.  

**Ans.**  
dynamically scope 的填答模式：接續從最後呼叫的開始寫，一路往回朔到前一個呼叫的程式，如果有還沒填上的變數，就是該 scope 的結果  
| Question | Variable | Where Declared |
| -------- | -------- | -------------- |
| a        | d, e, f  | fun3           |
|          | c        | fun2           |
|          | b        | fun1           |
|          | a        | main           |
| b        | d, e, f  | fun3           |
|          | b, c     | fun1           |
|          | a        | main           |
| c        | b, c, d  | fun1           |
|          | e, f     | fun3           |
|          | a        | main           |
| d        | b, c, d  | fun1           |
|          | e, f     | fun3           |
|          | a        | main           |
| e        | c, d, e  | fun2           |
|          | f        | fun3           |
|          | b        | fun1           |
|          | a        | main           |
| f        | b, c, d  | fun1           |
|          | e        | fun2           |
|          | f        | fun3           |
|          | a        | main           |
