#include <iostream>
#include <cstdlib>

#define MAX_ARRAY_SIZE 1000009

using namespace std;

string nameArray[MAX_ARRAY_SIZE];
int priorityArray[MAX_ARRAY_SIZE];

int* quickSort(int, int);

int main(void) {
  cout.tie(0);
  cout.sync_with_stdio(false);

  int N;

  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> nameArray[i] >> priorityArray[i];
  }

  quickSort(0, N - 1);

  cout << "First three things to do:\n";

  for (int i = N - 1; i > N - 4; i--) {
    cout << nameArray[i] << endl;
  }

  return 0;
}


int* quickSort(int lb, int rb) {

  if (lb >= rb) {
    return priorityArray;
  }

  int pivot = priorityArray[rb];
  int l = lb;
  int r = rb - 1;
  string tempName;
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

      tempName = nameArray[l];
      nameArray[l] = nameArray[r];
      nameArray[r] = tempName;
    } else {
      break;
    }
  }

  if (priorityArray[rb] != priorityArray[l]) {
    tempPriority = priorityArray[rb];
    priorityArray[rb] = priorityArray[l];
    priorityArray[l] = tempPriority;

    tempName = nameArray[rb];
    nameArray[rb] = nameArray[l];
    nameArray[l] = tempName;
  }

  quickSort(lb, l - 1);
  quickSort(l + 1, rb);

  return priorityArray;
}