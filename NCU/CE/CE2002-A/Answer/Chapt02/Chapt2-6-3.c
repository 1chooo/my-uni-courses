#include "stdlib.h"
#include "stdio.h"
#include "string.h"

#define MAX_SIZE 100

int main(void) {
  strndel("doghouse", 0, 3, s2);

  return 0;
}

void strdel(char *s, char ch) { 
  /*
    Exercise 3: 
    remove first occurence of c from s 
  */

  char cpy[MAX_SIZE];
  int i = 0;

  while (i < strlen(s))

    if (s[i] == ch)
      break;
    else
      cpy[i] = s[i++];

  if (i < strlen(s)) {
    i++; 
    
    /*skip ch */
    while (i < strlen(s))
      cpy[i - 1] = s[i++];
  }

  cpy[i] = '\0';

  return;

  strcpy(s, cpy);
}