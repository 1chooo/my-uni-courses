#include <stdio.h>
#include <string.h>

typedef struct
{
  double length, width;
} rectStuff;
typedef struct
{
  double base, height;
} triStuff;

typedef struct
{
  char name[10];
  enum tagField
  {
    rectangle,
    triangle,
    circle
  } shapeType;
  union
  {
    rectStuff rect;
    triStuff tri;
    double radius;
  } stats;
} shape;

void printShape(shape);

int main()
{
  shape s1, s2, s3;
  strcpy(s1.name, "rectangle");
  s1.shapeType = rectangle;
  s1.stats.rect.length = 10;
  s1.stats.rect.width = 20;
  strcpy(s2.name, "triangle");
  s2.shapeType = triangle;
  s2.stats.tri.base = 102;
  s2.stats.tri.height = 450;
  strcpy(s3.name, "circle");
  s3.stats.radius = 2.5;
  /*  printf("%f\n",s3.stats.radius);*/
  printShape(s1);
  printShape(s2);
  printShape(s3);
}

void printShape(shape s)
{ /*print out the information on a shape */
  printf("Name: %s\n", s.name);
  switch (s.shapeType)
  {
  case rectangle:
    printf("\tLength:%f\n", s.stats.rect.length);
    printf("\tWidth:%f\n\n", s.stats.rect.width);
    break;
  case triangle:
    printf("\tBase:%f\n", s.stats.tri.base);
    printf("\tHeight:%f\n\n", s.stats.tri.height);
    break;
  case circle:
    printf("Radius:%f\n", s.stats.radius);
    break;
  }
}