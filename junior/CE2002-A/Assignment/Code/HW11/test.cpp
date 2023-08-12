#include <iostream>
#include <string>
#include <vector>
#pragma GCC optimize("O3,unroll-loops")
using namespace std;

struct score {
    int key;
    string val;
    score(int k, string v) : key(k), val(v) {}
    friend bool operator<(const score& lhs, const score& rhs) {
        return lhs.key == rhs.key ? lhs.val > rhs.val : lhs.key < rhs.key;
    }
    friend bool operator>(const score& lhs, const score& rhs) {
        return lhs.key == rhs.key ? lhs.val < rhs.val : lhs.key > rhs.key;
    }
};

vector<score> v;
int count = 0;

void quicksort(int left, int right) {
    int i = left;
    int j = right;
    if (i < j - 1) {
        auto& pivot = v[i];
        do {
            do {
                i++;
            } while (v[i] < pivot && i < j);
            do {
                j--;
            } while (v[j] > pivot);
            if (i < j) swap(v[i], v[j]);
        } while (i < j);
        swap(pivot, v[j]);
        cout << "The index of the " << ++count << "-th pivot is " << j << ".\n";
        quicksort(left, j);
        quicksort(j + 1, right);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, key;
    string val;
    cin >> n;
    v.reserve(n);
    while (n--) {
        cin >> val >> key;
        v.emplace_back(key, val);
    }
    quicksort(0, v.size());
    for (const auto& it : v)
        cout << it.val << ' ' << it.key << '\n';
    return 0;
}