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