#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_STACK_SIZE 10000
#define MAX_EXPRESSION_SIZE 10000
#define print printf

char infixExpr[MAX_STACK_SIZE];
char result[MAX_STACK_SIZE];

typedef enum {
  // + - * / ()
  leftParen, rightParen, plus, minus, times, divide, eos, operand
} Precedence;

int priorityWeight(char);
Precedence getToken(char);
void postfix(void);
void showAns(void);

int main(void) {
  int runTimes = 0;

  scanf("%d", &runTimes);

  while (--runTimes >= 0) {
    scanf(" %[^\n]", infixExpr);     // input until meeting \n
    postfix();

    for (int i = 0; i < strlen(result); i++) {
      print("%c ", result[i]);
    }
    memset(result, 0, sizeof(result));
    print("\n");
  }

  return 0;
}

void postfix(void) {

  char stack[MAX_STACK_SIZE];
  char symbol;
  int stackTop = -1;
  int resultTop = 0;

  for (int i = 0; i < strlen(infixExpr); i++) {
    symbol = infixExpr[i];

    if (symbol == '(') {
      stack[++stackTop] = symbol;
    } else if (symbol == ')') {
      while (stack[stackTop] != '(') {
        result[resultTop++] = stack[stackTop--];
      }

      stackTop--;
    } else if ((symbol == '*') || (symbol == '/')) {
      while ((stack[stackTop] == '*' || stack[stackTop] == '/') && stackTop != -1) {
        result[resultTop++] = stack[stackTop--];
      }
      stack[++stackTop] = symbol;
    } else if (symbol == '+' || symbol == '-') {
      while (stack[stackTop] != '(' && stackTop != -1) {
        result[resultTop++] = stack[stackTop--];
      }
      stack[++stackTop] = symbol;
    } else if ('0' <= symbol && symbol <= '9') {
      result[resultTop++] = symbol;
    } else;
  }

  while (stackTop != -1) {
    result[resultTop++] = stack[stackTop--];
  }
}

int priorityWeight(char token) {
  switch (token) {
    case '(' :  return 3;
    case ')' :  return 3;
    case '*' :  return 2;
    case '/' :  return 2;
    case '+' :  return 1;
    case '-' :  return 1;
    case ' ' :  return -1;
    default :   return 0;
  }
}

Precedence getToken(char token) {

  switch (token) {
    case '(' :  return leftParen;
    case ')' :  return rightParen;
    case '*' :  return times;
    case '/' :  return divide;
    case '+' :  return plus;
    case '-' :  return minus;
    case ' ' :  return eos;
    default :   return operand;
  }
}