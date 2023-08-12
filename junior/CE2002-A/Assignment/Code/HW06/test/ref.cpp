#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
void dbg() { cerr << '\n'; }
template<class T, class ...U> void dbg(T a, U ...b) { cerr << a << ' ', dbg(b...); }
template<class T> void org(T l, T r) { while (l != r) cerr << *l++ << ' '; cerr << '\n'; }
#define debug(args...) (dbg("(" + string(#args) + ") = (", args, ")"))
#define orange(args...) (cerr << "[" + string(#args) + ") = ", org(args))
#else
#define debug(...) ((void)0)
#define orange(...) ((void)0)
#endif
#define all(v) (v).begin(), (v).end()

mt19937 rng((unsigned long long)(new char));

 
void solve() {
	int n;
	cin >> n;

	vector<char> vec(1<<n|1);
	for (int i = 1; i < (1<<n); i++) {
		//cerr << i << '\n';
		string x;
		cin >> x;
		if (x == "-1") vec[i] = -1;
		else if (0 <= x[0] and x[0] <= 9) vec[i] = x[0];
		else vec[i] = x[0];
		
	}

	auto cal = [&](auto cal, int now) -> long long {
		if ('0' <= vec[now] and vec[now] <= '9') return vec[now] - '0'; 	
		else {
			char o = vec[now];
			if (o == '+') return cal(cal, now<<1) + cal(cal, now<<1|1);
			if (o == '-') return cal(cal, now<<1) - cal(cal, now<<1|1);
			if (o == '*') return cal(cal, now<<1) * cal(cal, now<<1|1);
			if (o == '/') return cal(cal, now<<1) / cal(cal, now<<1|1);
		}
	};

	cout << cal(cal, 1) << '\n';
}

signed main() {
	// ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	// freopen("1.in", "w", stdout);
	solve();
	return 0;
}