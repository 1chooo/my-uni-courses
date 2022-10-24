#include <bits/stdc++.h>

#define ll long long
#define print printf
#define pb push_back

using namespace std;

int n, m;

struct Item
{
  int coef;
  int expo;
  Item *next;

  Item() : next(nullptr){};
  Item(int a, int b, int e) : coef(a + b), expo(e), next(nullptr){};
};

Item *a, *b, *d;

int main()
{
  // ios_base::sync_with_stdio(false) ;
  // cin.tie(0) ;

  Item *dummy = new Item();
  Item *dummy2 = new Item();
  Item *dummy3 = new Item();
  a = dummy;
  b = dummy2;
  d = dummy3;

  cin >> n;
  for (int i = 0; i < n; i++)
  {
    Item *item = new Item();
    cin >> item->coef >> item->expo;
    a->next = item;
    a = item;
  }

  cin >> m;
  for (int j = 0; j < m; j++)
  {
    Item *item = new Item();
    cin >> item->coef >> item->expo;
    b->next = item;
    b = item;
  }

  a = dummy->next;
  b = dummy2->next;

  while (a || b)
  {
    // cout << a -> expo << " " << b -> expo << endl ;
    if (!a)
    {
      // cout << "a is null\n" ;
      Item *item = new Item(0, b->coef, b->expo);
      d->next = item;
      d = item;
      b = b->next;
      continue;
    }
    if (!b)
    {
      // cout << "b is null\n" ;
      Item *item = new Item(a->coef, 0, a->expo);
      d->next = item;
      d = item;
      a = a->next;
      continue;
    }

    if (a->expo == b->expo)
    {
      // cout << "equal\n" ;
      Item *item = new Item(a->coef, b->coef, a->expo);
      d->next = item;
      d = item;
      a = a->next;
      b = b->next;
    }
    else if (a->expo < b->expo)
    {
      // cout << "a<b\n" ;
      Item *item = new Item(b->coef, 0, b->expo);
      d->next = item;
      d = item;
      b = b->next;
    }
    else if (a->expo > b->expo)
    {
      // cout << "a>b\n" ;
      Item *item = new Item(a->coef, 0, a->expo);
      d->next = item;
      d = item;
      a = a->next;
    }
  }

  d = dummy3->next;
  while (d)
  {
    if (d->coef != 0)
    {
      cout << d->coef << " " << d->expo << " ";
    }
    d = d->next;
  }
  cout << "\n";

  delete dummy;
  delete dummy2;
  delete dummy3;
}