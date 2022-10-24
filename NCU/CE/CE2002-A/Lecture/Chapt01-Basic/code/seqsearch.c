int seqsearch(int list[], int searchNum, int n) {
  int i;
  list[n] = searchNum;

  for (i = 0; list[i] != searchNum; i++);

  return ((i < n) ? i : -1);
}