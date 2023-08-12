#include "stdio.h"
#include "stdlib.h"

#define MAX_SIZE 1000
#define MAX_ROW_SIZE 1000
#define MAX_COL_SIZE 1000

typedef struct offsets {
    short int vert;
    short int horiz;
} Offsets;

Offsets move[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

typedef struct element {
    int row;
    int col;
    int dir;
} Element;

Element stack[MAX_SIZE];

int maze[MAX_ROW_SIZE][MAX_COL_SIZE];
int mark[MAX_ROW_SIZE][MAX_COL_SIZE];

void findPath(int, int);
void showAns(int, int, int, int);

int main(void) {
    int mazeRow, mazeCol;

    scanf("%d %d", &mazeRow, &mazeCol);

    for (int i = 0; i < mazeRow + 2; i++) {
        for (int j = 0; j < mazeCol + 2; j++) {
            if (i == 0 || i == (mazeRow + 1) || j == 0 || j == (mazeCol + 1))
                maze[i][j] = 1;
            else
                scanf("%d", &maze[i][j]);
        }
    }

    findPath(mazeRow, mazeCol);

    return 0;
}

void findPath(int mazeRow, int mazeCol) {
    int exitRow = mazeRow;
    int exitCol = mazeCol;
    int currentRow, currentCol, currentDir;
    int nextRow, nextCol;
    int found = 0;
    int top;

    mark[1][1] = 1;
    stack[0].row = 1;
    stack[0].col = 1;
    stack[0].dir = 0;

    top = 0;

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

            
            break;
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

    showAns(mazeRow, mazeCol, found, top);
    return;
}

void showAns(int mazeRow, int mazeCol, int found, int top) {
    if (found == 0) {
        printf("Can't reach the exit!\n");
    } else {
        for (int i = 0; i <= top; i++) {
            printf("(%d,%d) ", stack[i].row - 1, stack[i].col - 1);
        }
        printf("(%d,%d)\n", mazeRow - 1, mazeCol - 1);
    }

    return;
}