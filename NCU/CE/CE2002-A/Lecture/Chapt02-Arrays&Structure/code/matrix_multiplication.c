#include "stdio.h"
#include "stdlib.h"

#define MAX_TERMS 101
#define MAX_COL 100

typedef struct term {
  int col;
  int row;
  int value;
} Term;

Term a[MAX_TERMS];
Term b[MAX_TERMS];
Term d[MAX_TERMS];

int COMPARE(int a, int b);

void transposeMatrix(term a[], term b[]) //轉置矩陣.
{
  int i, j, currentb = 1;
  
  b[0].row = a[0].col;
  b[0].col = a[0].row;
  b[0].value = a[0].value;
  
  if(a[0].value > 0) {
    for(i=0; i < a[0].col; i++){
      for (j=1; j <= a[0].value; j++){
        if (a[j].col == i) {
          b[currentb].row = a[j].col;
          b[currentb].col = a[j].row;
          b[currentb].value = a[j].value;
          currentb++;
        }
      }
    }
  }
}

void fastTranspose(Term a[], Term b[]) {
  int row_terms[MAX_COL], starting_pos[MAX_COL];
  int i, j, num_cols = a[0].col, num_terms = a[0].value;

  b[0].row = num_cols;
  b[0].col = a[0].row;
  b[0].value = num_terms;

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

void mmult(Term a[], Term b[], Term d[]) {
  int i, j, column, totalB = b[0].value, totalD = 0;
  int rows_a = a[0].row, cols_a = a[0].col, totalA = a[0].value;
  int cols_b = b[0].col, row_begin = 1, row = a[1].row, sum = 0;
  int new_b[MAX_TERMS][3];

  if (cols_a != b[0].row) {
    fprintf(stderr, "Incompatiable matrices\n");
    exit(1);
  }

  fastTranspose(b, new_b);
  a[totalA + 1].row = rows_a;
  new_b[totalB + 1].row = cols_b;
  new_b[totalB + 1].col = 0;

  for (i = 1; i <= totalA; ) {
    column = new_b[1].row;

    for (j = 1; j <= totalB + 1) {
      if (a[i].row != row) {
        storesum(d, &totalD, row, column, &sum);
        i = row_begin;

        for (; new_b[j].row == column; j++)
          ;
        column = new_b[j].row;
      } else if (new_b[j].row != column) {
        storesum(d, &totalD, row, column, &sum);
        i = row_begin;
        column = new_b[j].row;
      } else switch (COMPARE(a[i].col, new_b[j].col))  {
        case -1 :
          i++;
          break;
        case 0 :
          sum += (a[i++].value * new_b[j++].value);
          break;
        case 1 :
          j++;
      }
    }
    for (; a[i].row == row; i++)
      ;
    row_begin = i;
    row = a[i].row;
  }

  d[0].row = rows_a;
  d[0].col = cols_b;
  d[0].value = totalD;

  return;
}

void storesum(term d[], int *totald, int row, int column, int *sum) //相加儲存.
{
  if (*sum){
    if (*totald < MAX_TERMS) {
      d[++*totald].row = row;
      d[*totald].col = column;
      d[*totald].value = *sum;
      *sum = 0;
    } else {
      fprintf(stderr, "Numbers of terms in product exceed %d\n", MAX_TERMS);
      exit(1);
    }
  }
}

int COMPARE(int a, int b) {
  if(a > b)
    return -1;
  if(a == b)
    return 0;
  if(a < b)
    return 1;
}

void print_matrix(Term matrix[]) {
    int i;
    printf("Row   Col   Value\n");
    for(i = 0; i <= matrix[0].value; i++){
        printf("%-5d %-5d %-5d\n", matrix[i].row, matrix[i].col, matrix[i].value);
    }
}