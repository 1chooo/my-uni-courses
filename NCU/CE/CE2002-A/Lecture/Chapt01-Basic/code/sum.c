float sum(float list[], int n) {
  float tempSum = 0;
  int i;

  for (i = 0; i < n; i++) 
    tempSum += list[i];

  return tempSum;
}