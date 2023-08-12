#include <stdio.h>
#include <stdlib.h>
#define MAX_TERMS 101
#define MAX_COL 100

typedef struct term {
	int col;
	int row;
	int value;
} Term;

Term a[MAX_TERMS] = {{6, 6, 8}, {0, 0, 15}, {0, 3, 22}, {0, 5, -15}, {1, 1, 11}, {1, 2, 3}, {2, 3, -6}, {4, 0, 91}, {5, 2, 28}};
Term b[MAX_TERMS];

void fastTranspose(Term a[], Term b[]);

int main() {
	fastTranspose(a, b);

	printf("Sparse matrix: A\n");
	for (int i = 0; i < 8; i++) {
		printf("%d %d %d\n", a[i].col, a[i].row, a[i].value);
	}


	printf("Sparse matrix: B\n");

	for (int i = 0; i < 8; i++) {
		printf("%d %d %d\n", b[i].col, b[i].row, b[i].value);
	}
	return 0;
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
      row_terms[a[i].row]++;

		for (i = 0; i < num_cols; i++)
			printf("%d ", row_terms[i]);

		printf("\n");

    starting_pos[0] = 1;

    // carries out the computation of starting_pos
    for (i = 1; i < num_cols; i++)
      starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1];

		for (i = 0; i < num_cols; i++)
			printf("%d ", starting_pos[i]);

		printf("\n");

    // places the triples into the tran­spose matrix
    for (i = 1; i <= num_terms; i++) {
      j = starting_pos[a[i].row]++;
      b[j].row = a[i].col;
      b[j].col = a[i].row;
      b[j].value = a[i].value;
    }

		for (i = 0; i < num_cols; i++)
			printf("%d ", starting_pos[i]);

		printf("\n");
  }

  return;
}