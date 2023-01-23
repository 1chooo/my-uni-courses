#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main(void) {
  int N, M, index;
  int first[100000], second[100000], ans[200000];
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> first[i];
  }

  cin >> M;

  for (int i = 0; i < M; i++) {
    cin >> second[i];
  }

  cin >> index;

    int count = 0;
    int temp;
    for (int i = 0; i <= index; i++) {
        ans[i] = first[i];
        count++;
    }
    // count++;
    temp = count;

    for (int i = 0; i < M; i++) {
        ans[count + i] = second[i];
    }




	for (int i = (N - 1); i > index; i--) {
        cout << first[i] << "-->";
    }



    for (int i = (index + M); i >= 0; i--) {
        cout << ans[i] << "-->";
    }
	cout << "null";

 return 0;
}
