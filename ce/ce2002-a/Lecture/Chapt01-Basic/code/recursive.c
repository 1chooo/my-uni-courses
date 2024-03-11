int binarySearch(int list[], int searchNum, int left, int right) {
  int middle;

  if (left <= right) {
    middle = (left + right) / 2;
    switch (COMPARE(list[middle], searchNum)) {
      case -1 : 
        return binarySearch(list, searchNum, middle + 1, right);
      case 0 :
        return middle;
      case 1 :
        return binarySearch(list, searchNum, left, middle - 1);
    }
  }

  return -1;
}