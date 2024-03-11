#include <bits/stdc++.h>
using namespace std;
pair<string, int> data[1000010];
void pq_sort(int max_val)
{
  for (int j = max_val; j > 1; j--)
  {
    int i = j;
    while ((i > 1))
    {
      if (data[i].second > data[i >> 1].second)
      {
        pair<string, int> tmp = data[i >> 1];
        data[i >> 1] = data[i];
        data[i] = tmp;
      }
      i >>= 1;
    }
  }
}
int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  int Case;
  cin >> Case;

  for (int i = 1; i <= Case; i++)
  {
    cin >> data[i].first >> data[i].second;
  }

  cout << "First three things to do:" << endl;
  for (int i = 0; i < 3; i++)
  {
    pq_sort(Case);
    cout << data[1].first << endl;
    data[1] = data[Case--];
  }

  return 0;
}