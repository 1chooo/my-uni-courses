// https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/zui-xiao-sheng-cheng-shu

#include <iostream>
#include <algorithm>

using namespace std;

struct Edge
{
  int x;
  int y;
  int w;
};

Edge edge[500000];
int num[2000], parent[2000];

bool cmp(Edge a, Edge b) {
  return a.w < b.w;
}

int findParent(int a) {
  while (a != parent[a]) {
    a = parent[a];
  }
  return a;
}

int main() {

  int n, m, numEdge, result;

  cin >> n >> m;

  for (int i = 0; i < m; i++) {
    cin >> edge[i].x >> edge[i].y >> edge[i].w;
  }

  for (int i = 0; i < n; i++) {
    parent[i] = i;
    num[i] = 1;
  }

  sort(edge, edge + m, cmp);
  result = 0, numEdge = 0;
  for (int i = 0; i < m && numEdge < n; i++) {
    int a, b;
    a = findParent(edge[i].x);
    b = findParent(edge[i].y);
    if (a != b) {
      if (num[a] > num[b]) {
        parent[b] = a;
        num[a] += num[b];
      } else {
        parent[a] = b;
        num[b] += num[a];
      }
      result += edge[i].w;
      numEdge++;
    }
  }
  cout << result << endl;
  
  return 0;
}