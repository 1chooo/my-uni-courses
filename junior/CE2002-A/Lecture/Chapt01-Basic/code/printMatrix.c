void printMatrix(int matrix[][MAX_SIZE], int rows, int cols) {
  int i, j;

  for (i = 0; i < rows; i++) {
    for (j = 0; j < cols; j++) 
      printf("%d", matrix[i][j]);
    
    printf("\n");
  }
}