
char s1[MAX_SIZE] = {"hello, world!"};
char *chPtr;
chPtr = strchr1(s1, ch);
if (chPtr)
  printf("%c found at position %s\n", ch, chPtr);

char *strchr1(char *s, char c)

{ /*return a pointer of c in s

  This version is case sensitive

  Exercise 5 */

  int i;

  for (i = 0; i < strlen(s); i++)

    if (c == s[i])
      return &s[i];

  return NULL;
}

void strnins(char *s, char *t, int i)
{/* revised version of program 2.12 */
   char string[MAX_SIZE];
   if( (i < 0) || (i > strlen(s)))
     printf("Position is out of bounds \n");
   else {
     if (!(strlen(s)))
       strcpy(s,t);
     else if (strlen(t)) {
	    strncpy(string, s,i);
		string[i]='\0';
		printf("After strncpy: %s\n", string);
		strcat(string,t); printf("After strcat: %s\n", string);
		strcat(string, (s+i));
		strcpy(s, string);
	  }
   }
 }