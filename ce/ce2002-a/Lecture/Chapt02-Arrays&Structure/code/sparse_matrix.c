#include "stdio.h"
#include "stdlib.h"

#define MAX_TERMS 101
#define MAX_COL 50

typedef struct term {
  int col;
  int row;
  int value;
} Term;

Term a[MAX_TERMS];
Term b[MAX_TERMS];



/*
  for (j = 0; j < col; j++) 
    for (i = 0; i < rows; i++)
      b[j][i] = a[i][j];
*/

void transpose(Term a[], b[]) {
  int n, i, j, currentB;

  n = a[0].value;
  b[0].row = a[0].col;
  b[0].col = b[0].row;
  b[0].value = n;

  if (n > 0) {
    currentB = 1;


    for (i = 0; i < a[0].col; i++) {
      for (j = 1; j <= n; j++) {
        if (a[j].col == i) {
          b[currentB].row = a[j].col;
          b[currentB].col = a[j].row;
          b[currentB].value = a[j].value;

          currentB++;
        }
      }
    }
  }

  return;
}


/* 
  O(col + elements)
  But the time becomes O(columns • rows) 
  when the number of elements is 
  of the order columns • rows.
*/
void fastTranspose(Term a[], Term b[]) {
  int row_terms[MAX_COL], starting_pos[MAX_COL];
  int i, j, num_cols = a[0].col, num_terms = a[0].value;

  b[0].row = num_cols;
  b[0].col = num_terms;

  if (num_terms > 0) {

    // Compute the value for row_terms.
    for (i = 0; i < num_cols; i++)
      row_terms[i] = 0;

    // Compute the value for row_terms.
    for (i = 1; i <= num_terms; i++)
      row_terms[a[i].col]++;

    starting_pos[0] = 1;

    // carries out the computation of starting_pos
    for (i = 1; i < num_cols; i++)
      starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1];

    // places the triples into the tran­spose matrix
    for (i = 1; i <= num_terms; i++) {
      j = starting_pos[a[i].col]++;
      b[j].row = a[i].col;
      b[j].col = a[i].row;
      b[j].value = a[i].value;
    }
  }

  return;
}