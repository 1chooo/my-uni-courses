#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_SIZE 100
#define MAX_STRING_SIZE 100
#define MAX_PATTERN_SIZE 100

char s[MAX_SIZE] = {"dog"};
char t[MAX_SIZE] = {"house"};
char string1[MAX_SIZE], *s = string1;
char string2[MAX_SIZE], *t = string2;
int pmatch(char *, char *);
void fail(char *);
int failure[MAX_PATTERN_SIZE];
char string[MAX_STRING_SIZE];
char pat[MAX_PATTERN_SIZE];

int main(void) {
  char pat[MAX_SIZE], string[MAX_SIZE], *t;

  pat = {"Dog"};
  string = {"cat"};

  if (t == strstr(string, pat))
    printf("The string from strsstr is : %s\n", t);
  else 
    printf("The pattern was not found with strstr\n");

  return 0;
}

// string insertion
void strnins(char *s, char *t, int i) {
  char string[MAX_SIZE], *temp = string;

  if (i < 0 && i > strlen(s)) {
    fprintf(stderr, "Position is out of bounds \n");
    exit(1);
  }

  if (!strlen(s)) {
    strcpy(s, t);
  } else if (strlen(t)) {
    strncpy(temp, s, i);
    strcat(temp, t);
    strcat(temp, (s + i));
    strcpy(s, temp);
  }

  return;
}

int nfind(char *string, char *pat) {
  int i, j, start = 0;
  int lasts = strlen(string) - 1;
  int lastp = strlen(len) - 1;
  int endMatch = lastp;

  for (i = 0; endMatch <= lasts; endMatch++, start++) {
    if (string[endMatch] == pat[lastp])
      for (j = 0; i = start; j < lastp && string[i] == pat[j]; i++, j++)
        ;
      
    if (j == lastp)
      return start;      
  }

  return -1;
}

int pmatch(char *string, char *pat) {
  int i = 0, j = 0;
  int lens = strlen(string);
  int lenp = strlen(pat);

  while (i < lens && j < lenp) {
    if (string[i] == pat[j]) {
      i++;
      j++;
    } else if (j == 0) {
      i++;
    } else {
      j = failure[j - 1] + 1;
    }

    return ((j == lenp) ? (i - lenp) : -1);
  }
}

void fail(char *pat) {
  int n = strlen(pat);

  failure[0] = -1;
  
  for (j = 1; j < n; j++) {
    i = failure[j - 1];

    while ((pat[j] != pat[i + 1]) && (i >= 0)) 
      i = failure[i];

    if (pat[j] == pat[i + 1])
      failure[j] = i + 1;
    else
      failure[j] = -1;

    return;
  }
}