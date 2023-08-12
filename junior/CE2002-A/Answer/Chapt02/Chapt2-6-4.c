pos = strpos1(s1, ch);

if (pos >= 0)

  printf("%c found at position %d\n", ch, pos);

else

  printf("%c is not in the string\n", ch);

int strpos1(char *s, char c)

{ /* return the position of c in s

   This version is case sensitive

   Exercise 4 */

  int i;

  for (i = 0; i < strlen(s); i++)

    if (c == s[i])
      return i;

  return -1;
}