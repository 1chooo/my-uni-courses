int main(void) {
  int left, right, temp;
  string leftString, rightString;

  for (int i = (N - 1); i > 0; i--) {
    for (int j = 0; j < i; j++) {
      left = priorityArray[j];
      right = priorityArray[j + 1];
      leftString = nameArray[j];
      rightString = nameArray[j + 1];

      if (left > right) {
        priorityArray[j] = right;
        priorityArray[j + 1] = left;
        nameArray[j] = rightString;
        nameArray[j + 1] = leftString;
      }
    }
  }
}