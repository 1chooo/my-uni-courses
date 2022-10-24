void transpose(int a[][MAX_SIZE]) {
  int i, j, temp;

  for (i = 0; i < MAX_SIZE - 1; i++) 
    for (j = i + 1; j < MAX_SIZE; j++)
      SWAP(a[i][j], a[j][i], temp);
}