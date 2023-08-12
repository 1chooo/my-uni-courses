#include <stdio.h>
#include <string.h>

typedef struct
{
  int month;
  int day;
  int year;
} date;

typedef struct
{
  ;
} noMarriage;

typedef struct
{
  date dom, dodivorce;
} divorce;

typedef struct
{
  date dom, dodeath;
} widow;

typedef struct
{
  enum tagField
  {
    single,
    married,
    widowed,
    divorced
  } status;
  
  union
  {
    noMarriage nom;
    date dom;
    divorce divorceStuff;
    widow widowStuff;
  } u;
} maritalStatus;

typedef struct
{
  char name[10];
  int age;
  float salary;
  date dob;
  maritalStatus ms;
} humanBeing;

void printPerson(humanBeing);

int main()
{
  humanBeing p1;
  p1.dob.month = 5;
  p1.dob.day = 16;
  p1.dob.year = 1978;
  strcpy(p1.name, "Fiona");
  p1.salary = 1.00;
  p1.ms.status = married;
  p1.ms.u.dom.month = 10;
  p1.ms.u.dom.day = 31;
  p1.ms.u.dom.year = 1999;
  printPerson(p1);
}

void printPerson(humanBeing p)
{ /*print out the information on a person */
  printf("Name: %s\n", p.name);
  printf("DOB: %d/%d/%d\n", p.dob.month, p.dob.day, p.dob.year);
  printf("Salary: %5.2f\n", p.salary);
  switch (p.ms.status)
  {
  case married:
    printf("Marriage Date: %d/%d/%d\n", p.ms.u.dom.month, p.ms.u.dom.day, p.ms.u.dom.year);
  }
}