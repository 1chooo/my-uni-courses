#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef struct list {
  char data;
  List *link;
} List;

int main(void) {
  List item1, item2, item3;

  item1.data = 'a';
  item2.data = 'b';
  item3.data = 'c';
  item1.link = item2.link = item3.link = NULL;

  // We attach these structures together by replacing the null link field.
  item1.link = &item2;
  item2.link = &item3;
  return 0;
}