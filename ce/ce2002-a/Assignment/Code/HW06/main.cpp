#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <bitset>

#define MAX_STACK_SIZE 10009

using namespace std;

std::vector<char> arr;

long long calculator(long long, long long, char);
long long turnPostorder(long long);

int main(void) {
  cout.tie(0);
  cout.sync_with_stdio(false);

  int height, nums = 1;
  string temp;

  cin >> height;

  nums = pow(2, height) - 1;
  arr = vector<char>(nums + 1);

  for (int i = 1; i <= nums; i++) {
    cin >> temp;
    if (temp != "-1") {
      arr[i] = temp[0];
    } else {
      arr[i] = 'j';
    }
  }
  cout << turnPostorder(1) << endl;

  return 0;
}

long long calculator(long long left, long long right, char opr) {
  if (opr == '+') {
    return left + right;
  } else if (opr == '-') {
    return left - right;
  } else if (opr == '*') {
    return left * right;
  } else if (opr == '/') {
    return left / right;
  } else;
}

long long turnPostorder(long long index){
  if (arr[index] <= '9' && arr[index] >= '0') 
    return arr[index] - '0';

  long long left, right;
  left = turnPostorder(2 * index);
  right = turnPostorder(2 * index + 1);
  
  return calculator(left, right, arr[index]);
}