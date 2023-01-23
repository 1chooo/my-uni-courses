#include <iostream>
#include <cstdlib>

#define MAX_ARRAY_SIZE 1000009

using namespace std;

int priorityArray[MAX_ARRAY_SIZE];

int main(void) {
  int N;

  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> priorityArray[i];
  }

  quickSort(0, N - 1);


  return 0;
}

int* quickSort(int lb, int rb) {

  if (lb >= rb) {
    return priorityArray;
  }

  int pivot = priorityArray[rb];
  int l = lb;
  int r = rb - 1;
  int tempPriority;


  while (1) {

    while (priorityArray[l] < pivot) {
      l++;
    }

    while (priorityArray[r] >= pivot && r > lb) {
      r--;
    }

    if (l < r) {
      tempPriority = priorityArray[l];
      priorityArray[l] = priorityArray[r];
      priorityArray[r] = tempPriority;

      for (int i = 0; i < 5; i++) {
        if (i == 4) {
          cout << priorityArray[i] << endl;
        } else {
          cout << priorityArray[i] << " ";
        }
      }
    } else {
      break;
    }
  }

  if (priorityArray[rb] != priorityArray[l]) {
    tempPriority = priorityArray[l];
    priorityArray[l] = priorityArray[r];
    priorityArray[r] = tempPriority;
  }

  quickSort(lb, l - 1);
  quickSort(l + 1, rb);

  return priorityArray;
}