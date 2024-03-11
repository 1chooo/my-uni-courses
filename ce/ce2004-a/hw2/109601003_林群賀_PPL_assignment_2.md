# PPL - HW2

##### Tags: `CS`, `PPL`

> Number of questions: 10  
> Total Score: 100 points  
> Due day: 11:00 PM 25th May 2023 

#### P.S.:
1. You need to type your answers and print them out in papers. And then hand the answer sheets to TAs.
2. Without reasonable reasons, late submission will not be accepted.
3. Copying other student’s answers is strictly prohibited.

---

**(1) (9 points)**  
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

**Ans.**  
(a) If we do not consider whether we can change the value of variable `tuv`, there are other properties associated with its value. tuv is a two-dimensional array of integers, specifically with a size of 10 rows by 10 columns. It is a local variable within the scope of the function `bar()`. The two-dimensional array is defined without initialization, indicating that its elements do not have specific initial values assigned.  
(b) Of course that we can change the value of tuv. Since `tuv` is not decalred as const and it is a non-constant array; therefore we can modify the elements within the scope of the function `bar()`.  
(c) Sure, we can change the value of `tuv[1]`. The reason are the same above the (b) part, the value of `tuv[1]` which refers to the second row of the `tuv` array. We can assign the specific values that we want to its elements or modify the existing values within the scop of the function `bar()`. However, if the array is declared as `const int tuv[10][10]`, it would indicate that the elements of tuv cannot be modified.

**(2) (12 points)**  
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
(c) Could we change the value of tuv[1][1]?  

**Ans.**  
(a) The data type of `tuv` is a two-dimensional array of type `Circle`. It is declared as `Circle[][]`.   
(b) The data type of `tuv[1]` is an array of type `Circle`. It is a row in the two-dimensional array `tuv`, representing the second row.  
(c) Of course we can change the value of `tuv[1][1]`, since it is an element in the two-dimensional array `tuv`. The code `Circle tuv[][]=new Circle[10][10];` initializes `tuv[][]` as a 10x10 two-dimensional array of type `Circle`, where each element is initialized to the default value of `Circle`, which is `null`. In this initialized state, the value of `tuv[1][1]` is `null`, indicating that it does not point to any `Circle` **object** yet. If we want to modify the value of `tuv[1][1]`, we need to create a new Circle object and assign it to tuv[1][1].  
For example:
```java
tuv[1][1] = new Circle(); // Initializing tuv[1][1] with a new Circle object
tuv[1][1].setVariable(5); // Modifying the value of tuv[1][1] using the a method within following java code
```
By initializing `tuv[1][1]` and calling its methods, we can change its value or perform any desired operations.

**(3) (12 points)**  
What follows is a Java program excerpt.
```java
class Circle {
	int setVariable(int s) { 
		int r;
		r=6;
		return s+r; 
	}
}

public class Geometry{
    :
  public static void main(String [] args) {
		String t=new String("Welcome"); 		// location 1 
		String s=new String("Welcome"); 		// location 2 
		Circle shape[][]=new Circle[3][3]; 	// location 3
			: 
	}
}
```
(a) Assume "Welcome" does not appear in any other statement before location 1, how many new String objects will be created by the Java statement at location 1?   
(b) Assume "Welcome" does not appear in any other statement before location 1, how many new String objects will be created by the Java statement at location 2?  
(c) How many objects will be created by the Java statement at location 3?   
(d) How many variables will be created by the Java statement at location 3?   

### Ans.  
(a) The number of new String objects will be created by the Java statement at location 1 is two.
One is at location 1, `String t = new String("Welcome");` will create one new String object stored in the heap memory area, and this object represents the `String "Welcome"`. And the variable `t` will **reference** this String object. The second one is in the String constant pool because we have stored the "Welcome" String object in the memory; therefore we will generate an object in the String constant pool. Above all, there are two new String objects created by the Java statement at location 1.   
(b) Similarly, The number of new String objects will be created by the Java statement at location 2 is one. At location 2 `String s = new String("Welcome");` will create one new String object stored in the heap memory area, and this object represents the `String "Welcome"`. And the variable `s` will **reference** this String object. However, in the location 1, "Welcome" String has existed in the constant pool; therefore, it's only one new String object.   
In sum up of this two questions, we have to talk about the mechanism of `jAVA` Language,
when we use the `new` keyword, we create the new object, it allocates a new memory space 
to store the data of that object. Regardless of whether it is at location 1 or location 2, 
only one new String object is created at Heap memory area. Although the same String literal `"Welcome"` is used in the code, each time a new object is created with the new keyword, it is allocated a **separate** memory space.  
Therefore, in reality, two **independent** `String` Objects are created. 
The variables `t` and `s` respectively reference these two Objects. 
As a result, there are **two String objects** representing `"Welcome"` in heap memory, 
and `t` and `s` point to these two objects respectively.  
Also, if it is the first time to create the String object it will be created in the String constant pool, but if we want to create the new String object, but it have existed in the String constant pool, we won't create the new String object in String constant pool.  
(c) The number of objects will be created by the Java statement at location 3 is thirteen. At location 3, `Circle shape[][] = new Circle[3][3];` will create a two-dimensional array of type `Circle`. The size of the array is three rows by three columns and the total elements of it is nine. And in JAVA, two-dimensional array is combined by one-dimensional array,;therefore, there are three one-dimensional objects. Final, the other is a reference array to point out the formal objects. Above all, there are thirteen objects by the JAVA statement at location 3.  
(d) The number of variables will be created by the Java statement at location 3 is fourteen. Continuely with the (c) answer, we will add `shape[][]` object, and all of them are the variables; therefore, there are fourteen variables by the JAVA statement at location 3.

**(4) (12 points)**  
C, C++, and Fortran do not perform range checking of array subscripts. Assume a C compiler allocates memories for arrays declared in the same declaration statement in adjacent areas and memory allocation stars from the leftmost array to the rightmost array. For example for the following declaration statement, `int t[10], u[10], v[10];`, the compiler allocates memory for array t first. The memory of array u is right after the memory of array t. The memory of array v is right after the memory of array u. Hence, the addresses of array t elements are larger than the addresses of array u elements. And the addresses of array u elements are larger than the addresses of array v elements. Assume the compiler utilizes row major order to store elements in an array. What follows is a C program.
```c
#include<stdio.h>
main() { 
	int a[10][10], b[10][10], c[10][10];
	int i,j;
  	for(i=0;i<10;i++) {
   		for(j=0;j<10;j++) {
			a[i][j] = 1;
			b[i][j] = 2;
			c[i][j] = 3;
		}
		b[17][9]=4;			/*location 1*/
		b[17][16]=5;		/*location 2*/
		b[-3][7]=6;			/*location 3*/
		b[-3][-6]=7;		/*location 4*/
	}
}
```
(a) The value of which array element will be changed by the statement at location 1?  
(b) The value of which array element will be changed by the statement at location 2?  
(c) The value of which array element will be changed by the statement at location 3?  
(d) The value of which array element will be changed by the statement at location 4?  

**Ans.**  
(a) At location 1, the statement `b[17][9] = 4;` will change the value of the element in the `b` array. Specifically, it will modify the element at row index 17 and column index 9 of the array `b`, assigning it the value 4.  
(b) At location 2, the statement `b[17][16] = 5;` will change the value of the element in the `b` array. Specifically, it will modify the element at row index 17 and column index 16 of the array `b`, assigning it the value 5.  
(c) At location 3, the statement `b[-3][7] = 6`; will attempt to change the value of the element in the `b` array. Specifically, it will attempt to modify the element at row index -3 and column index 7 of the array `b`. However this index is outside the declared range of the array, which can lead to undefined behavior 'runtime error', such as a segmentation fault, causing the program to crash.  
Alternatively, it might execute without any apparent issues, but the values of the array elements and the program's behavior cannot be relied upon. 
It is crucial to ensure that array accesses are within the bounds of the array to avoid such undefined behavior.  
(d) The answer of this question is about to the question (3), it also attempt to change the value of the element in the `b` array. Specifically, it will attempt to modify the element at row index -3 and column index -6 of the array `b`. However, this index is outside the declared range of the array, which can lead to undefined behavior 'runtime error', such as a segmentation fault, causing the program to crash.  
Alternatively, it might execute without any apparent issues, but the values of the array elements and the program's behavior cannot be relied upon. It is crucial to ensure that array accesses are within the bounds of the array to avoid such undefined behavior. 

**(5) (8 points)**  
If dynamic scope is used in the following program, at location 10 (a) what is the value of variable a? (b) what is the value of variable b?

```c
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
```
**Ans.**  
(a) The value of variable `a` at location 10 will be 5. This is because at location 3 within the bar() function, the statement `a = 5;` assigns the value 5 to the variable a. Since dynamic scoping uses the value of the nearest dynamically enclosing scope, the value of `a` at location 10 will be the updated value of 5.  
(b) 由於使用了動態範疇（dynamic scope）的特性，我們想要得到變數 b 的值。在位置 9，我們呼叫了 b = bar() + c; 這個語句。然後在位置 2，我們呼叫了 c = car() + b; 這個語句。因此，我們需要回到 car() 這個函數。在位置 1，我們使用了 car() 函數內的變數 e，以及 bar() 函數內的變數 c，還有 main() 函數內的變數 a。所以回傳值是 12。接著，我們回到 bar() 函數的位置 2，c = car() + b; 這裡的 b 是來自 main() 的位置 7，所以 c = 12。因此，在位置 5 回傳值為 14。最後，我們回到 main() 的位置 9，我們使用語句 b = bar() + c;，其中 c 是位置 8 的值。所以最終，變數 b 的值為 14 + 3，即在位置 10，b 的值為 17。  
Due to the use of dynamic scope, to determine the value of variable `b`, we called the statement `b = bar() + c;` at location 9. Then at location 2, we called `c = car() + b;`. So we need to go to the `car()` function. At location 1, the statement `return e + c + a;` in the `car()` function uses the variable `e` from `car()`, the variable `c` from `bar()`, and the variable `a` from `main()`. Therefore, the return value is 12. Next, we go back to location 2 in the `bar()` function, where `c = car() + b;` `b` is the value from location 7 in `main()`, so `c = 12`. Thus, at location 5, the return value is 14. Finally, we return to location 9 in `main()`, where we use the statement `b = bar() + c`;, and `c` is the value from location 8. So, ultimately, the value of variable b is 14 + 3, which means at location 10, the value of `b` is 17.

**(6) (8 points)**  
In the following C program excerpt,
(a) what problem does this program have?  
(b) why does this problem happen?  
```c
#define BufferSize 60

char *poi="The summer break is around the corner.";
char sentence[BufferSize];
int ppp(char *s, char *d, unsigned len) {
	unsigned i;
  for( i=0 ;i<len; ++i ) {
   	*(d+i)=*(s+i);
  }
}

void goo(char *s, char *d, int length) {
   if(length<BufferSize)
    	ppp(poi,sentence,length);
}
```
**Ans.**  
(a) The problem with this program is that the `int ppp(char*, char*, unsigned)` function is declared int an `int` type; however, it does not have a return segment.   
Therefore, it will show the warning message: `non-void function does not return a value`.  
(b) The result that this problem happen because the `ppp()` function is defined to return an `int` type value; however, it does not have   return segment. That will result in when we call the function, it will not return any value, even with the declaration in `ppp()`. This could be an oversight or a mistake in the implementation of the function. As a result, the function doesn't provide a proper return value, which can lead to undefined behavior when the function is called.


**(7) (8 points)**  
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
(a) The reason variables `d` and `e` have different values even though the computation in the 
statements at locations 1 and 3 is mathematically equivalent to the computation in the statement 
at location 2 is due to the order of **operations** and **floating-point precision**.  
In the statement at location 1, the expression `(b*b*b*b*b*b*b*b*b*b)` involves repeated multiplication, which can lead to numerical errors and loss of precision. Similarly, in the statement at location 3, the expression `d=d*c*c` involves multiple multiplications and accumulates numerical errors.  
Floating-point arithmetic has limitations in representing `real` numbers with complete accuracy, and these limitations can lead to **rounding errors** and imprecise results. When multiple floating-point perations are performed, the accumulated errors can cause slight differences in the final results.  
Therefore, even though the computations in the statements at locations 1 and 3 are mathematically equivalent to the computation in the statement at location 2, the presence of numerical errors and the order of operations can result in slightly different values for variables `d` and `e`.  
Here, we can provide additional insights into previous experiences with scientific computations. In our department, we often employ numerical assimilation techniques to address the issue of floating-point errors that can arise during numerical calculations. In scientific endeavors, even the slightest error can lead to undesirable outcomes. Hence, various numerical methods have been developed to mitigate this situation and minimize the impact of such errors on results.  
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

**(8) (12 points)**  
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
After program `test_address.c` is compiled by a C compiler,
then after the program is executed and the execution flow arrives at location 1, the  values of &p, p, and *p would be as follows:  
- `p: The value of `p` is the address of variable `t`, which is 678.
- `&p`: The address of the variable `p` is 123.
- `*p`: The value of `*p` is the value stored at the memory location pointed to by `p`, which is the value of `t`. Since `p` points to `t`, and the value of `t` is 987; therefore, `*p` will be 987.


**(9) (9 points)**  
Consider the following program:  
In the following C program excerpt,  
(a) What is the result printed out by the statement commented as `Location 6`?  
(b) What is the result printed out by the statement commented as `Location 11`?  
(c) What mistake does it make?

```c
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
```

**Ans.**  
(a)  
中文描述：  
在實際使用除錯器逐行執行程式碼時，起初有一段記憶體配置。然而，在位置 2，透過 malloc 函數清除了變數 q，並在位置 3 的語句中將 p 設置為 q 的值。因此此時 p 和 q 的位址相同。接下來，在位置 4 的語句中，*p 和 *q 的值都為 'h'。然後，在位置 5 的語句中，*p 的值被設置為 'e'，這也導致 *q 的值變為 'e'。因此，在位置 6 的語句中，被註解為 "Location 6" 的結果輸出為 'e'。  
English description:  
In the actual execution of the code using a debugger, there is an initial memory allocation. However, at location 2, the variable q is cleared using the malloc function, and the statement at location 3 sets p equal to q. As a result, p and q have the same address. Moving on, at location 4, both *p and *q have the value 'h'. Then, at location 5, the statement sets the value of *p to 'e', which also changes the value of *q to 'e'. Therefore, the result printed out by the statement commented as "Location 6" is 'e'.  
(b)  
中文描述：  
在 (a) 小提示提到的情況中，在位置 7 使用了 malloc 函數來清除變數 q，並在位置 8 的語句中將 p 設置為 q 的值。因此此時 p 和 q 具有相同的位址。接下來，在位置 9 的語句中，*p 和 *q 的值都為 'r'。然後，在位置 10 的語句中，*p 的值被設置為 'o'，這也導致 *q 的值變為 'o'。因此，在位置 11 的語句中，被註解為 "Location 11" 的結果輸出為 'o'。  
English description:  
In the scenario mentioned in part (a) of the hint, at location 7, the malloc function is used to clear the variable q, and at location 8, the statement sets p equal to q. As a result, p and q have the same address. Moving on, at location 9, both *p and *q have the value 'r'. Then, at location 10, the statement sets the value of *p to 'o', which also changes the value of *q to 'o'. Therefore, the result printed out by the statement commented as "Location 11" is 'o'.  
(c) The mistake in this program is the lack of error handling or checking for the return value of the malloc function. In both Location 2 and Location 7, memory is dynamically allocated using `malloc(1)`, but there is no check to ensure that the memory allocation was successful. If malloc fails to allocate memory, it will return a `null` pointer. Attempting to dereference a `null` pointer, as done in Location 4 and Location 9, leads to undefined behavior, which can result in a program crash 
or unexpected behavior.  
To address this issue, it is important to check the return value of malloc to ensure that memory allocation was successful before proceeding with accessing or modifying 
the allocated memory.  
The below is the modified `C` Program:
```c
#include <stdio.h>
#include <stdlib.h>

void bar() { 
    char *p, *q;                    /*Location 1*/
    q = malloc(1);                  /*Location 2*/

    if (q != NULL) {
        p = q;                      /*Location 3*/
        *q = 'h';                   /*Location 4*/
        *p = 'e';                   /*Location 5*/
        printf("%c", *q);           /*Location 6*/

        q = malloc(1);              /*Location 7*/

        if (q != NULL) {
            p = q;                  /*Location 8*/
            *q = 'r';               /*Location 9*/
            *p = 'o';               /*Location 10*/
            printf("%c", *q);       /*Location 11*/
        } else {
            printf("Memory allocation failed at Location 7\n");
        }

        free(q);                    // Free the memory allocated at Location 7
    } else {
        printf("Memory allocation failed at Location 2\n");
    }

    free(q);                        // Free the memory allocated at Location 2
}
```

**(10) (10 points)**  
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

**Ans.**  
(a) Assuming that dunamic scoping is used, Main calls Subl; Subl calls Sub2; Sub2 calls Sub3. Visible variables during execution of the last subprogram activated (Sub3):  
- A (declared in Sub3)
- X (declared in Main)
- W (declared in Sub3)

(b) Assuming that dunamic scoping is used, Main calls Subl; Subl calls Sub3. Visible variables during execution of the last subprogram activated (Sub3):  
- A (declared in Sub3)
- X (declared in Main)
- W (declared in Sub3)
(c) Assuming that dunamic scoping is used, Main calls Sub2; Sub2 calls Sub3; Sub3 calls Subl. Visible variables during execution of the last subprogram activated (Subl):  
- A (declared in Subl)
- Y (declared in Main)
- Z (declared in Main)
  
(d) Assuming that dunamic scoping is used, Main calls Sub3; Sub3 calls Subl. Visible variables during execution of the last subprogram activated (Subl):  
- A (declared in Subl)
- Y (declared in Main)
- Z (declared in Main)
  
(e) Assuming that dunamic scoping is used, Main calls Subl; Subl calls Sub3; Sub3 calls Sub2. Visible variables during execution of the last subprogram activated (Sub2):  
- A (declared in Sub2)
- B (declared in Sub2)
- Z (declared in Main)

Above all, only the variables that are declared within the visible scope of each subprogram will be accessible during the execution. Variables declared in the outer units or subprograms may be shadowed by variables with the same name declared in the inner units or subprograms.