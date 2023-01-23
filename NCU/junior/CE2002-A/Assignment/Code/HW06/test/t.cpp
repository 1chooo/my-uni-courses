#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int H;
int N;

std::vector<char> v;

long long cal(long long l, long long r, char op){
    if (op == '+'){
        return l + r;
    }
    else if (op == '-'){
        return l - r;
    }
    else if (op == '*'){
        return l * r;
    }
    else if (op == '/'){
        return l / r;
    }
}

long long post_order(long long x){
    //cout << x << " " << v[x] << "\n";
    if (v[x] <= '9' && v[x] >= '0') return v[x] - '0';
    long long l, r;
    l = post_order(2 * x);
    r = post_order(2 * x + 1);
    return cal(l, r, v[x]);
}

int main(){
    cin >> H;
    N = pow(2, H);
    v = vector<char>(N+1);
    string t;
    for (int i = 1; i < N; i++){
        cin >> t;
        if (t == "-1") v[i] = '!';
        else v[i] = t[0];
    }

    cout << post_order(1);
}