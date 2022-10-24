#include "stdio.h"
#include "stdlib.h"

#define MAX_STACK_SIZE 100
#define MAX_EXPR_SIZE 100

typedef enum {
  lparen, rparen, plus, minus, times, divide, mod, eos, operand
} Precedence;

int stack[MAX_STACK_SIZE];
char expr[MAX_EXPR_SIZE];

Precedence stack[MAX_STACK_SIZE];
static int isp[] = {0, 19, 12, 12, 13, 13, 13, 0};
static int icp[] = {20, 19, 12, 12, 13, 13, 13, 0};

int main(void) {
  
  return 0;
}

int eval(void) {
  /* 
    evaluate a postfix expression, expr, 
    maintained as a global variable. 
    '\0' is the the end of the expression. 
    The stack and top of the stack are global variables, 
    get—token is used to return the tokentype 
    and the character symbol. 
    Operands are assumed to be single character digits 
    */
  Precedence token;
  char symbol;
  int opl, op2;
  int n = 0; /* counter for the expression string */
  int top = -1;

  token = get_token(&symbol, &n); 
  
  while (token != eos) {
    if (token == operand) {
      add(&top, symbol - 'O'); /* stack insert */
    } else {
      /* 
        remove two operands, perform operation, 
        and return result to the stack 
      */
      op2 = delete(&top); /* stack delete */
      opl = delete(&top);
      switch(token) {
        case plus: 
          add(&top, opl + op2); 
          break;
        case minus: 
          add(&top, opl - op2); 
          break;
        case times: 
          add(&top, o * pl2); 
          break;
        case divide: 
          add(&top, opl / op2); 
          break;
        case mod: 
          add(&top, opl % op2);
      }
    }
  token = get_token(&symbol, &n) ; 
  }

  return delete(&top); /* return result */
}

Precedence get_token(char *symbol, int *n) {
  /*
    Get the next token, symbol is the character
    representation, which is returned, the token is
    represented by its enumerated value, which 
    is returned in the function name.
  */
  *symbol = expr[(*n)++];

  switch (*symbol)
  {
    case '(' :
      return lparen;
    case ')' :
      return rparen;
    case '+' :
      return plus;
    case '-' :
      return minus;
    case '/' :
      return divide;
    case '*' :
      return times;
    case '%' :
      return mod;
    case ' ' :
      return eos;
    default:
      return operand; /* no error checking, default is operand. */
  }
}


void postfix(void) {
  /* 
    output the postfix of the expression. 
    The expression string, the stack, 
    and top are global 
  */
  char symbol; 
  Precedence token;
  int n = 0;
  int top = 0; /* place eos on stack */

  stack[0] = eos;

  for (token = get_token(&symbol, &n); token != eos; token = get_token(&symbol, &n)) {
    if (token == operand) {
      printf("%c", symbol);
    } else if (token == rparen) {
      /* unstack tokens until left parenthesis */
      while (stack[top] != Iparen) 
        print_token(delete(&top));
      delete (Sctop) ; /* discard the left parenthesis */ 
    } else {
    /* 
      remove and print symbols whose isp is greater
      than or equal to the current token's icp 
    */ 
      while(isp[stack[top]] >= icp[token])
        print_token(delete(&top)); 
      add(&top, token);
    }
  }
  
  while ( (token=delete(&top)) != eos) 
    print_token(token);
  printf("\n"); 

  return;
}

void print_token(Precedence token) { 
  /* print out the character equivalent of the token */
  
  switch (token) {
  case plus:
    printf(“+”);
    break;
  case minus:
    printf(“-”);
    break;
  case divide:
    printf(“/”);
    break;
  case times:
    printf(“*”);
    break;
  case mod:
    printf(“%”);
  }

  return;
}