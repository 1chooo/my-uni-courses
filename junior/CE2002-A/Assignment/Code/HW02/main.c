/* A Mazing Problem */

#include "stdio.h"
#include "stdlib.h"

#define MAX_ARRAY_COL 500
#define MAX_ARRAY_ROW 500
#define MAX_STACK_SIZE 500

typedef struct offsets {
    int vert;
    int horiz;
} Offsets;

Offsets move[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int maze[MAX_ARRAY_ROW][MAX_ARRAY_COL];
int mark[MAX_ARRAY_ROW][MAX_ARRAY_COL];

typedef struct element {
  short int row;
  short int col;
  short int dir;
} Element;

Element stack[MAX_STACK_SIZE];

int main(void) {
  int row, col;
  int currentRow, currentCol, currentDir;
  int nextRow, nextCol;
  int exitRow, exitCol;
  int found = 0;
  int top;
  Element walk;

  scanf("%d %d", &row, &col);
  exitRow = row, exitCol = col;

  for (int i = 0; i < row + 2; i++) {
    for (int j = 0; j < col + 2; j++) {
      if (i == 0 || i == (row + 1) || j == 0 || j == (col + 1))
        maze[i][j] = 1;
      else
        scanf("%d", &maze[i][j]);
    }
  }

  mark[1][1] = 1;
  top = 0;
  stack[0].row = 1;
  stack[0].col = 1;
  stack[0].dir = 0;

  while (top > -1 && found != 1) {
    
    currentRow = stack[top].row;
    currentCol = stack[top].col;
    currentDir = stack[top].dir;

    while (currentDir < 4 && found != 1) {
      nextRow = currentRow + move[currentDir].vert;
      nextCol = currentCol + move[currentDir].horiz;

      if (nextRow == exitRow && nextCol == exitCol) {
        mark[nextRow][nextCol] = 1;

        stack[top].row = currentRow;
        stack[top].col = currentCol;
        stack[top].dir = currentDir;

        found = 1;

        for (int i = 0; i <= top; i++) {
          printf("(%d,%d) ", stack[i].row - 1, stack[i].col - 1);
        }
        printf("(%d,%d)\n", row - 1, col - 1);
      }   
      
      if (maze[nextRow][nextCol] == 0 && mark[nextRow][nextCol] == 0) {
        mark[nextRow][nextCol] = 1;
        
        stack[top].row = currentRow;
        stack[top].col = currentCol;
        stack[top].dir = currentDir;

        top++;

        currentRow = nextRow;
        currentCol = nextCol;
        currentDir = 0;
      } else 
        currentDir++;
    }

    top--;
  }

  if (top == -1) {
    printf("Can't reach the exit!\n");
  }

  return 0;
}