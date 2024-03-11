float rsum(float list[], int n) {
  if (n) return rsum(list, n - 1) + list[n - 1];

  return 0;
}