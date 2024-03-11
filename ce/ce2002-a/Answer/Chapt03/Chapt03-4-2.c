void PrintToken(priority token)
{ /* print out the character equivalent of the token */
  switch (token)
  {
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
}