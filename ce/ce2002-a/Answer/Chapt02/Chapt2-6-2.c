#include "stdlib.h"
#include "stdio.h"
#include "string.h"

#define MAX_SIZE 100

int main(void) {
  char s1[MAX_SIZE] = {"hello, world!"};
  char s2[MAX_SIZE] = {};

  strndel(s1, 5, 7, s2);
  countChars(s1);
}

void strndel(char *s, int start, int length, char *cpy) { 
  /*
    Exercise 2: 
    create a string with start to length -1 characters removed from s 
  */

  int i, n;

  for (i = 0; i < start; i++)

    cpy[i] = s[i];

  n = start;

  printf("start + length: %d\n", start + length);

  for (i = start + length; i < strlen(s); i++)

    cpy[n++] = s[i];

  cpy[n] = '\0';

  return;
}

void countChars(char *s) { 
  /*Exercise 1*/

  int counts[26];
  int i;
  char ch;

  for (i = 0; i < 26; i++) 
    /* set counts to 0 */
    counts[i] =0;

	  

  for (i = 0; i < strlen(s); i++)
    if ( (isupper(s[i])) || (islower(s[i]))) {
      ch = toupper(s[i]); /* make case insensitive */
      counts[(int)ch-65]++; /*Subtract ASCII value for A */
  }
   
  for (i = 0; i < 26; i++)
    printf("[%c: %d]  ", (char)(65+i), counts[i]);
   
  printf("\n");

  return;
}