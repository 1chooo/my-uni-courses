#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;
char data[100000005];

long long slove(int pos){
    if(data[pos]>='0' && data[pos]<='9') return data[pos]-'0';
    long long a = slove((pos<<1));
    long long b = slove((pos<<1)+1);
    if(data[pos]=='+') return a + b;
    if(data[pos]=='-') return a - b;
    if(data[pos]=='*') return a * b;
    if(data[pos]=='/') return a / b;

}

int main(){
    int h;
    string tmp;
    cin >> h;

    h = (1 << h) - 1;

    for(int i=1;i<=h;i++){
        cin >> tmp;
        data[i] = tmp=="-1"?'0':tmp[0];
    }
    cout << slove(1);
    return 0;
}