#include <stdio.h>
#include <math.h>
#include <ctype.h>

float prefixCalculator(char[]);

int main()
{
  char expression[40];
  float ans;
  printf("Enter the expression :: ");
  scanf("%s", expression);

  ans = roundf(prefixCalculator(expression) * 100) / 100;
  printf("%f", ans);
  return 0;
}

float prefixCalculator(char expression[40])
{
  float stack[40];
  int top = -1;
  char *e;
  float operand1, operand2;
  int asciiToInt;
  float value;

  e = expression;
  while (*e != '\0')
  {
    if (isdigit(*e))
    {
      asciiToInt = *e - 48;
      stack[++top] = asciiToInt;
    }
    else
    {
      operand1 = stack[top--];
      operand2 = stack[top--];
      switch (*e)
      {
      case '+':
      {
        value = operand1 + operand2;
        break;
      }
      case '-':
      {
        value = operand2 - operand1;
        break;
      }
      case '*':
      {
        value = operand1 * operand2;
        break;
      }
      case '/':
      {
        value = operand2 / operand1;
        break;
      }
      }
      stack[++top] = value;
    }
    e++;
  }
  return stack[top--];
}
