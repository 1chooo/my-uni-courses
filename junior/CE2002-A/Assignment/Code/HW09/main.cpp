#include <iostream>
#include <cstdlib>
#include <vector>
#include <climits>

using namespace std;

typedef pair<int, int> connected;

struct Graph {
  int from, to;

  vector<pair<int, connected>> edges;

  Graph(int from, int to) :
    from(from), to(to) {}
  
  void addEdges(int from, int to, int weight) {
    edges.push_back({weight, {from, to}});
  }

  int kruskalMST();
};

struct Disjoint {
  int *parent, *ranks;
  int n;

  Disjoint(int n) {
    this->n = n;
    parent = new int[n + 1];
    ranks = new int[n + 1];

    for (int i = 0; i <= n; i++) 
      parent[i] = i;
  }

  int find(int u) {
    if (u != parent[u])
      parent[u] = find(parent[u]);
    return parent[u];
  }

  void joint(int x, int y) {
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

int Graph::kruskalMST() {
  int weightMST = 0;
  sort(edges.begin(), edges.end());

  Disjoint dsjointSet(from);

  vector<pair<int, connected>>::iterator it;

  for (it = edges.begin(); it != edges.end(); it++) {
    int u = it->second.first;
    int v = it->second.second;

    int uset = dsjointSet.find(u);
    int vset = dsjointSet.find(v);

    if (uset != vset) {
      weightMST += it->first;
      dsjointSet.joint(uset, vset);
    }
  }

  return weightMST;
}

class Edge {
public:
  int from, to, weight;

  Edge(int f, int t, int w) : 
    from(f), to(t), weight(w) {}
};

int main(void) {
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
    return 0;
  }
  return 0;
}