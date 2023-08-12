#include <stdio.h>
#include <stdlib.h>

void bar() { 
    char *p, *q;                    /*Location 1*/
    q = malloc(1);                  /*Location 2*/

    if (q != NULL) {
        p = q;                      /*Location 3*/
        *q = 'h';                   /*Location 4*/
        *p = 'e';                   /*Location 5*/
        printf("%c", *q);           /*Location 6*/

        q = malloc(1);              /*Location 7*/

        if (q != NULL) {
            p = q;                  /*Location 8*/
            *q = 'r';               /*Location 9*/
            *p = 'o';               /*Location 10*/
            printf("%c", *q);       /*Location 11*/
        } else {
            printf("Memory allocation failed at Location 7\n");
        }

        free(q);                    // Free the memory allocated at Location 7
    } else {
        printf("Memory allocation failed at Location 2\n");
    }

    free(q);                        // Free the memory allocated at Location 2
}
