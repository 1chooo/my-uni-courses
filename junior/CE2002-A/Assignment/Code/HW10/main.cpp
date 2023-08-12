#include <functional>
#include <iostream>
#include <queue>
// #include <sstream>
#include <vector>
#pragma GCC optimize("O3")

using namespace std;
typedef pair<int, int> pii;

const int inf = 1e9;
int n, s, d;
int graph[100][100];
int cost[100];
bool visited[100] = {false};
priority_queue<pii, vector<pii>, greater<pii>> heap;

int dijkstra() {
    for (int i = 0; i < n; ++i)
        cost[i] = inf;
    cost[s] = 0;
    heap.emplace(0, s);
    while (!heap.empty()) {
        auto top = heap.top();
        auto& w = top.first;
        auto& u = top.second;
        heap.pop();
        if (visited[u])
            continue;
        visited[u] = true;
        for (int v = 0; v < n; ++v) {
            if (!visited[v] && cost[v] > graph[u][v] + w) {
                cost[v] = graph[u][v] + w;
                heap.emplace(cost[v], v);
            }
        }
    }
    return cost[d];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    // stringstream cin(
    //     "7 1 0\n"
    //     "0 2 0 1 0 0 0\n"
    //     "0 0 0 3 10 0 0\n"
    //     "4 0 0 0 0 5 0\n"
    //     "0 0 2 0 2 8 4\n"
    //     "0 0 0 0 0 0 6\n"
    //     "0 0 0 0 0 0 0\n"
    //     "0 0 0 0 0 1 0");
    cin >> n >> s >> d;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
            if (i != j && graph[i][j] == 0)
                graph[i][j] = inf;
        }
    }
    cout << dijkstra() << '\n';
    return 0;
}