void prod(int a[][MAX_SIZE], int b[][MAX_SIZE], int c[][MAX_SIZE], int rowsa, int colsb, int colsa) {
  int i, j, k;

  for (i = 0; i < rowsa; i++) 
    for (j = 0; j < colsb; j++) {
      c[i][j] = 0;

      for (k = 0; k < colsa; k++) 
        c[i][j] += a[i][k] * b[k][j];
    }

  return;
}