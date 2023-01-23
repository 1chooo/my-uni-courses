#include <bits/stdc++.h>
using namespace std;

// u and v is connected
typedef pair<int, int> connected;

struct Graph
{
  // n nodes; m edges
  int n, m;
  vector<pair<int, connected>> edges;

  Graph(int n, int m)
  {
    this->n = n;
    this->m = m;
  }

  void addEdges(int u, int v, int w)
  {
    edges.push_back({w, {u, v}});
  }

  int kruskalMST();
};

// To represent Disjoint Sets
struct Disjoint
{
  int *parent, *ranks;
  int n;

  Disjoint(int n)
  {
    this->n = n;
    parent = new int[n + 1];
    ranks = new int[n + 1];
    // Initial
    for (int i = 0; i <= n; i++)
    {
      parent[i] = i;
    }
  }
  int find(int u)
  {
    if (u != parent[u])
      parent[u] = find(parent[u]);
    return parent[u];
  }
  // Union by rank
  void joint(int x, int y)
  {
    x = find(x);
    y = find(y);

    if (ranks[x] > ranks[y])
      parent[y] = x;
    else
      parent[x] = y;

    if (ranks[x] == ranks[y])
      ranks[y]++;
  }
};

int Graph::kruskalMST()
{
  int weightMST = 0; // Initial
  sort(edges.begin(), edges.end());

  Disjoint dsjoiset(n);

  vector<pair<int, connected>>::iterator it;

  for (it = edges.begin(); it != edges.end(); it++)
  {
    int u = it->second.first;
    int v = it->second.second;

    int uset = dsjoiset.find(u);
    int vset = dsjoiset.find(v);

    // Check if it has cycle
    if (uset != vset)
    {
      // cout << u << " - " << v << endl;
      weightMST += it->first;
      dsjoiset.joint(uset, vset);
    }
  }

  return weightMST;
}

int main()
{
  int n, m;
  int u, v, w;
  while (cin >> n >> m)
  {
    Graph g(n, m);
    while (m--)
    {
      cin >> u >> v >> w;
      g.addEdges(u, v, w);
    }
    int weightMST = g.kruskalMST();
    cout << weightMST << "\n";
  }
  return 0;
}