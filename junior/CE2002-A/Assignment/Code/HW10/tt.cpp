#include <bits/stdc++.h>

using namespace std;

int dis[105][105];
int ans[105];

int main()
{
  ios::sync_with_stdio(0), cin.tie(0);

  int n, start, end;
  cin >> n >> start >> end;
  for (int i = 0; i < n; i++)
  {
    for (int t = 0; t < n; t++)
    {
      cin >> dis[i][t];
    }
  }

  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
  set<int> in;

  for (int i = 0; i < n; i++)
  {
    ans[i] = INT_MAX;
  }
  ans[start] = 0;
  pq.emplace(0, start);

  while (in.find(end) == in.end())
  {
    pair<int, int> now = pq.top();
    pq.pop();
    if (in.find(now.second) != in.end())
    {
      continue;
    }

    in.emplace(now.second);

    for (int i = 0; i < n; i++)
      if (dis[now.second][i] != 0)
      {
        if (now.first + dis[now.second][i] < ans[i])
        {
          ans[i] = now.first + dis[now.second][i];
          pq.emplace(ans[i], i);
        }
      }
  }
  cout << ans[end] << endl;
  return 0;
}