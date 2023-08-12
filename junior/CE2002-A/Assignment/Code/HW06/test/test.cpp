#include<bits/stdc++.h>
#include<iostream>
using namespace std;
string tmp;
vector<string> arr;

long long cal(int i, int n){
    if(arr[i]=="-1")
        return 0;
    if((i*2)>n)
        return int( arr[i][0]-'0');
    if((arr[i*2]=="-1" && arr[i*2+1]=="-1"))
        return int( arr[i][0]-'0');
    
    long long l=cal(i*2, n);
    long long r=cal(i*2+1, n);

    if(arr[i]=="+")
        return l+r;
    if(arr[i]=="-")
        return l-r;
    if(arr[i]=="*")
        return l*r;
    return l/r;
}

int main(){
    cout.tie(0);
    cout.sync_with_stdio(false);
    int h;
    long long k=1;
    cin >> h;
    arr.push_back("-1");
    for(int i=0; i<h; i++){
        for(long long j=1; j<=pow(2,i); j++){
            cin >> tmp;
            arr.push_back(tmp);
        }
    }
    long long ans = cal(1, arr.size()-1);
    cout << ans << "\n";
    return 0;
}