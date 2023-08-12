#include <bits/stdc++.h>
#define ll long long

using namespace std;

int n, m;
int a[1005];

void preOrder(int i)
{
  if (i > m)
    return;
  cout << a[i] << " ";
  preOrder(i * 2);
  preOrder(i * 2 + 1);
}

void inOrder(int i)
{
  if (i > m)
    return;
  inOrder(i * 2);
  cout << a[i] << " ";
  inOrder(i * 2 + 1);
}

void postOrder(int i)
{
  if (i > m)
    return;
  postOrder(i * 2);
  postOrder(i * 2 + 1);
  cout << a[i] << " ";
}

int main()
{
  // std::ios::sync_with_stdio(false);
  // std::cin.tie(0);

  cin >> n;
  while (n--)
  {
    cin >> m;
    for (int i = 1; i <= m; i++)
    {
      cin >> a[i];
    }
    preOrder(1);
    cout << "\n";
    inOrder(1);
    cout << "\n";
    postOrder(1);
    cout << "\n";
  }
}