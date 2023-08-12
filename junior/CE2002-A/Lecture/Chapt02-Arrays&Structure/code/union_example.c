#include "stdio.h"
#include "stdlib.h"

typedef struct date{
  int month;
  int day;
  int year;
} Date;


typedef struct sexType {
  enum tagField { female, male } sex;

  union {
    int children;
    int beard;
  } u;
} SexType;

typedef struct humanBeing{
  char name[10];
  int age;
  float salary;
  Date dob;
  SexType sexInfo;
} HumanBeing;

HumanBeing person1, person2;