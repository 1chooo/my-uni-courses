#include "stdio.h"
#include "stdlib.h"
#include "string.h"

# define FALSE 0
# define TRUE 1

typedef struct sex_type {
  enum tag_filed {female, male} sex;2

  union {
    int children;
    int beard;
  } u;
} Sex_type;

typedef struct date {
  int month;
  int day;
  int year;
} Date;

typedef struct human_being {
  char name[10];
  int age;
  float salary;
  Date dob;
  Sex_type sex_info;
} Human_being;


int human_equal(Human_being person1, Human_being person2) {
  if (strcmp(person1.name, person2.name))
    return FALSE;
  if (person1.age != person2.age)
    return FALSE;
  if (person1.salary != person2.salary)
    return FALSE;

  return TRUE;
}

int main(void) {
  Human_being person1, person2;

  /* ------------------------ 
   Don't do in this way!!!
   Cause can't assign to array 
   only the copy way.

   person1.name = "Hugo";
   person2.name = "1chooo";
  --------------------------- */ 

  strcpy(person1.name, "Hugo");
  strcpy(person2.name, "1chooo");

  person1.age = 10;
  person1.salary = 10000;
  person2.age = person1.age;
  person2.salary = person1.salary;

  person1.dob.month = 2;
  person1.dob.day = 11;
  person1.dob.year = 1944;

  person1.sex_info.sex = male;
  person1.sex_info.u.beard = FALSE;

  person2.sex_info.sex = female;
  person2.sex_info.u.children = 4;

  if (strcmp(person1.name, person2.name))
    printf("The two people do jave the same name.\n");
  else 
    printf("The two people have the same name.\n");

  if (human_equal(person1, person2))
    printf("The two human beings are the same.\n");
  else 
    printf("The two human beings are not the same.\n");

  return 0;
}