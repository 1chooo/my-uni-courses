#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(void) {
  long long int c = 246886422468;
  int d = 13579;

  long long int ans;
  long int temp;

  ans = c * c + d;
  cout << ans << endl;
  temp = sqrt(ans);
  // temp -= c;
  cout << ans << endl;
  cout << temp << endl;
  cout << c << endl;

  return 0;
}