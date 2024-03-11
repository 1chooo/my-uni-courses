#include <iostream>
using namespace std;

pair<string, int> arr[1000005];
int num;
int cur = 1;

bool isSame(const pair<string, int> &a, const pair<string, int> &b)
{
  if (a.second != b.second)
    return a.second > b.second;
  else
    return a.first < b.first;
}

void quickSort(int left, int right)
{
  if (left < right)
  {
    pair<string, int> pivot = arr[left];
    int i = left;
    int j = right + 1;

    while (i < j)
    {
      i++;
      j--;
      while (isSame(pivot, arr[i]) and i < num)
        i++;
      while (isSame(arr[j], pivot) and j > 0)
        j--;

      if (i < j)
        swap(arr[i], arr[j]);
    }

    swap(arr[left], arr[j]);
    cout << "The index of the " << cur++ << "-th pivot is " << j << "." << '\n';
    quickSort(left, j - 1);
    quickSort(j + 1, right);
  }
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> num;
  for (int i = 0; i < num; i++)
    cin >> arr[i].first >> arr[i].second;

  quickSort(0, num - 1);

  for (int i = 0; i < num; i++)
    cout << arr[i].first << " " << arr[i].second << '\n';

  return 0;
}