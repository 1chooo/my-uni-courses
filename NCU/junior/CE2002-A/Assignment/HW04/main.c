#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_STACK_SIZE 10000
#define MAX_EXPRESSION_SIZE 10000
#define print printf

char infixExpr[MAX_STACK_SIZE];
char result[MAX_STACK_SIZE];

void postfix(void);
void showAns(void);

int main(void) {
  int runTimes = 0;

  scanf("%d", &runTimes);

  while (--runTimes >= 0) {
    scanf(" %[^\n]", infixExpr);     // input until meeting \n
    postfix();
    showAns();    
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

  return;
}

void showAns(void) {
  for (int i = 0; i < strlen(result); i++) {
      print("%c ", result[i]);
    }
  print("\n");

  memset(result, 0, sizeof(result));

  for(size_t i = 0; i < sizeof result; ++i)
    result[i] = 0;

  return;
}