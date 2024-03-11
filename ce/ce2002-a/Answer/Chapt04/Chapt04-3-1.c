#include "stdio.h"
#include "stdlib.h"

// convert string
void convert_string(char *expr, char cleaned[MAX_STRING_SIZE])
{ /* change to all lower case
      remove spaces and punctuation */
  int i = 0, count = 0;
  char ch;
  while (i < strlen(expr))
  {
    if (isspace(expr[i]))
      i++;
    else if (ispunct(expr[i]))
      i++;
    else
    {
      ch = expr[i++];
      cleaned[count++] = tolower(ch);
    }
  }
  cleaned[count] = '\0';
}

// The palindrome parser() function
int parser(char expr[])
{
  int i = 0, half, odd;
  char ch;
  stack_ptr top = NULL;
  half = (int)strlen(expr) / 2;
  odd = strlen(expr) % 2;
  while (i < half) /* push half the letters onto the stack */
    push(&top, expr[i++]);
  if (odd)
    i++;
  while (i < strlen(expr))
  { /* pop character from stack and compare with next character in the string */
    ch = pop(&top);
    if (expr[i] != ch)
    { /* not a palindrome, empty out stack and return false */
      while (!IS_EMPTY(top))
      {
        ch = pop(&top);
      }
      return FALSE;
    }
    i++;
    return TRUE;
  }
}

int main()
{
  char expr[MAX_STRING_SIZE];
  char parse_string[MAX_STRING_SIZE];
  int i, half, odd, ok_pal;
  stack_ptr top = NULL;
  do
  {
    printf("Expression: ");
    /* use fgets to read in strings with spaces,
       strip off the new line character to get the correct count */
    fgets(expr, MAX_STRING_SIZE, stdin);
    if (expr[strlen(expr) - 1] == '\n')
      expr[strlen(expr) - 1] = '\0';
    if (strlen(expr))
    {
      convert_string(expr, parse_string);
      printf("cleaned %s\n", parse_string);
      if (ok_pal = parser(parse_string))
        printf("%s IS a palindrome.\n\n", expr);
      else
        printf("%s IS NOT a palindrome.\n\n", expr);
    }
  } while (strlen(expr));
}