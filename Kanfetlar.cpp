#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
using ll = long long;
#define pi pair<ll, ll>
#define ff first
#define ss second
#define vv vector<ll>
#define vc vector<vv>
#define pb push_back
#define rep(i, a, b) for(ll i = (a); i != (b); i += 2 * ((a) < (b)) - 1)
#define all(x) (x).begin(), (x).end()
#define fast ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define endl '\n'

using namespace std;
const ll mod = 1e9 + 7;

int main(){
int n; scanf("%d", &n); int a[n];
for(int &i : a) scanf("%d", &i);
int left[n], right[n]; 
memset(left, 0, sizeof(left));
memset(right, 0, sizeof(right));
for(int i = n - 2; i >= 0; i--)
 if(a[i] > a[i + 1]) right[i] = right[i + 1] + 1;
for(int i = 1; i < n; i++)
 if(a[i] > a[i - 1]) left[i] = left[i - 1] + 1;
ll sum = 0;
rep(i, 0, n) sum += max(left[i], right[i]) + 1;
cout << sum;
 return 0;
}
