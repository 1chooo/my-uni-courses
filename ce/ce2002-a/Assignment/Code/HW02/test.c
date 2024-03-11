#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define MAX_SIZE 500

// give direction
typedef struct
{
  short int vert;
  short int horiz;
} offsets;
typedef struct
{
  short int row;
  short int col;
  short int dir;
} element;

int main()
{
  int i = 0, j = 0;
  int row, col, dir, newrow, newcol, nextrow, nextcol;
  int rowm, colm;

  offsets move[4];
  element stack[MAX_SIZE];
  element position;

  // give direction of mov
  move[0].vert = -1;
  move[0].horiz = 0;
  move[1].vert = 0;
  move[1].horiz = 1;
  move[2].vert = 1;
  move[2].horiz = 0;
  move[3].vert = 0;
  move[3].horiz = -1;

  scanf("%d %d", &row, &col);
  // make a maze
  newrow = row + 2;
  newcol = col + 2;
  int maze[newrow][newcol];
  int mark[newrow][newcol];
  int exitrow = row;
  int exitcol = col;

  // give boundary with 1
  for (i = 0; i <= (row + 1); i++)
  {
    maze[i][0] = 1;
    maze[i][col + 1] = 1;
  }
  for (j = 0; j <= (col + 1); j++)
  {
    maze[0][j] = 1;
    maze[col + 1][0] = 1;
  }

  // give 0,1 in the maze
  for (i = 1; i <= row; i++)
  {
    for (j = 1; j <= col; j++)
    {
      scanf("%d", &maze[i][j]);
    }
  }

  // start walking
  int top = 0;
  top = 0;
  int count = 0;
  int found = false;
  mark[1][1] = 1;
  stack[0].row = 1;
  stack[0].col = 1;
  stack[0].dir = 0;

  while (top > -1 && !found)
  {

    if (top == 0 && count == 0)
    {
      position.row = stack[top].row;
      position.col = stack[top].col;
      position.dir = stack[top].dir;
      count++;
    }
    else
    {
      top--;
      position.row = stack[top].row;
      position.col = stack[top].col;
      position.dir = stack[top].dir;
    }
    // current
    rowm = position.row;
    colm = position.col;
    dir = position.dir;
    while (dir < 4 && !found)
    {

      nextrow = rowm + move[dir].vert;  
      nextcol = colm + move[dir].horiz;

      if (nextrow == exitrow && nextcol == exitcol)
      {
        stack[top].row = rowm;
        stack[top].col = colm;
        stack[top].dir = dir;
        found = true;
      }
      else if (maze[nextrow][nextcol] == 0 && mark[nextrow][nextcol] != 1)
      {

        mark[nextrow][nextcol] = 1;
        position.row = nextrow;
        position.col = nextcol;
        position.dir = ++dir;
        ++top;
        stack[top - 1].row = rowm;
        stack[top - 1].col = colm;
        stack[top - 1].dir = dir;

        rowm = nextrow;
        colm = nextcol;
        dir = 0;
      }
      else
      {
        ++dir;
      }
    }
  }

  // print the result
  if (found)
  {
    for (i = 0; i <= top; i++)
    {
      printf("(%d,%d) ", stack[i].row - 1, stack[i].col - 1);
    }
    printf("(%d,%d)", row - 1, col - 1);
  }
  else
  {
    printf("Can't reach the exit!");
  }
}