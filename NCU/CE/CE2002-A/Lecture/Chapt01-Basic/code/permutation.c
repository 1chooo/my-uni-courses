void permutation(char *list, int i, int n) {
  int j, temp;

  if (i == n) {
    for (j = 0; j <= n; j++)
      printf("%c", list[j]);
    print("     ");
  } else {
    for (j = i; j <= n; j++) {
      SWAP(list[i], list[j], temp);
      permutation(list, i + 1, n);
      SWAP(list[i], list[j], temp);
    }
  }

  return;
}