
int parser(char expr[])
{ /*parser for parethesis language
   if left paren, bracket or brace, push
   if right paren, bracket, or brace pop and compare
   if not a match return false. */
  int i;
  char ch;
  stack_ptr top = NULL;
  for (i = 0; i < strlen(expr); i++)
    switch (expr[i])
    {
    case '[':
    case '{':
    case '(':
      push(&top, expr[i]);
      break;
    case ']':
      if (IS_EMPTY(top))
        return FALSE;
      ch = pop(&top);
      if (ch != '[')
        return FALSE;
      break;
    case '}':
      if (IS_EMPTY(top))
        return FALSE;
      ch = pop(&top);
      if (ch != '{')
        return FALSE;
      break;
    case ')':
      if (IS_EMPTY(top))
        return FALSE;
      ch = pop(&top);
      if (ch != '(')
        return FALSE;
    }
  if (IS_EMPTY(top)) /*string is finished, stack contains items */
    return TRUE;
  return FALSE;
}