#include <stdio.h>
#define NUM_ROWS 5
#define NUM_COLS 3
#define BOUNDARY_COLS 5
#define MAX_STACK_SIZE 100
#define FALSE 0
#define TRUE 1

typedef struct
{
  short int row;
  short int col;
  short int dir;
} element;

element stack[MAX_STACK_SIZE]; /* global stack declaration */

typedef struct
{
  short int vert;
  short int horiz;
} offsets;

offsets move[9]; /* array of moves for each direction */

static short int maze[][BOUNDARY_COLS] = {{1, 1, 1, 1, 1}, /* top boundary  */
                                          {1, 0, 0, 0, 1},
                                          {1, 1, 1, 0, 1},
                                          {1, 0, 0, 0, 1},
                                          {1, 0, 1, 1, 1},
                                          {1, 0, 0, 0, 1},
                                          {1, 1, 1, 1, 1}}; /* bottom boundary */

short int mark[][BOUNDARY_COLS] = {{0, 0, 0, 0, 0},
                                   {0, 0, 0, 0, 0},
                                   {0, 0, 0, 0, 0},
                                   {0, 0, 0, 0, 0},
                                   {0, 0, 0, 0, 0},
                                   {0, 0, 0, 0, 0},
                                   {0, 0, 0, 0, 0}};

int top;
void init_move();
void add(element);
element delete ();
void stack_full();
void stack_empty();
void path();
void print_record(int, int, int);
void print_maze();

int main()
{ /* stack represented as an array */
  init_move();
  print_maze();
  path();
}

void init_move()
{ /* initial the table for the next row and column moves */
  move[1].vert = -1;
  move[1].horiz = 0; /*  N */
  move[2].vert = -1;
  move[2].horiz = 1; /* NE */
  move[3].vert = 0;
  move[3].horiz = 1; /*  E */
  move[4].vert = 1;
  move[4].horiz = 1; /* SE */
  move[5].vert = 1;
  move[5].horiz = 1; /*  S */
  move[6].vert = 1;
  move[6].horiz = 0; /* SW */
  move[7].vert = 0;
  move[7].horiz = -1; /*  W */
  move[8].vert = -1;
  move[8].horiz = -1; /* NW */
}

void print_maze()
{ /* print out the maze */
  int i, j;
  printf("Your maze, with the boundaries is: \n\n");
  for (i = 0; i <= NUM_ROWS + 1; i++)
  {
    for (j = 0; j <= NUM_COLS + 1; j++)
      printf("%3d", maze[i][j]);
    printf("\n");
  }
  printf("\n");
}

void stack_full()
{
  printf("The stack is full.  No item added \n");
}

void stack_empty()
{
  printf("The stack is empty.  No item deleted \n");
}

void add(element item)
{ /* add an item to the global stack
     top (also global) is the current top of the stack,
     MAX_STACK_SIZE is the maximum size */

  if (top == MAX_STACK_SIZE)
    stack_full();
  else
    stack[++top] = item;
}

element delete ()
{ /* remove top element from the stack and put it in item */
  if (top < 0)
    stack_empty();
  else
    return stack[top--];
}

void print_record(int row, int col, int dir)
{ /* print out the row, column, and the direction, the direction
   is printed out with its numeric equivvalent */
  printf("%2d    %2d%5d", dir, row, col);
  switch (dir - 1)
  {
  case 1:
    printf("    N");
    break;
  case 2:
    printf("    NE");
    break;
  case 3:
    printf("    E ");
    break;
  case 4:
    printf("    SE");
    break;
  case 5:
    printf("    S ");
    break;
  case 6:
    printf("    SW");
    break;
  case 7:
    printf("    W ");
    break;
  case 8:
    printf("    NW");
    break;
  }
  printf("\n");
}

void path()
{ /*  output a path through the maze if such a path exists,
     the maze is found in positions 1 to NUM_ROWS and 1 to NUM_COLS.
     Rows 0 and NUM_ROWS+1 serve as boundaries, as do Columns
     0 and NUM_COLS+1. */

  int i, row, col, next_row, next_col, dir, found = FALSE;
  element position;

  mark[1][1] = 1;
  /* place the starting position, maze[1][1] onto the stack
     starting direction is 2  */
  top = 0;
  stack[0].row = 1;
  stack[0].col = 1;
  stack[0].dir = 2;
  while (top > -1 && !found)
  {
    /* remove position at top of stack, and determine if
  there is a path from this position */
    position = delete ();
    row = position.row;
    col = position.col;
    dir = position.dir;
    while (dir <= 8 && !found)
    {
      /* check all of the remaining directions from the current
      position */
      next_row = row + move[dir].vert;
      next_col = col + move[dir].horiz;
      if (next_row == NUM_ROWS && next_col == NUM_COLS)
        /* path has been found, exit loop and print it out */
        found = TRUE;
      else if (!maze[next_row][next_col] && !mark[next_row][next_col])
      {
        /* current position has not been checked, place it
     on the stack and continue */
        mark[next_row][next_col] = 1;
        position.row = row;
        position.col = col;
        position.dir = ++dir;
        add(position);
        row = next_row;
        col = next_col;
        dir = 1;
      }
      else
        ++dir;
    }
  }
  if (!found)
    printf("The maze does not have a path\n");
  else
  {
    /* print out the path which is found in the stack */
    printf("The maze traversal is: \n\n");
    printf("dir#  row  col  dir\n\n");
    for (i = 0; i <= top; i++)
      print_record(stack[i].row, stack[i].col, stack[i].dir);
    printf("      %2d%5d\n", row, col);
    printf("      %2d%5d\n", NUM_ROWS, NUM_COLS);
  }
}
