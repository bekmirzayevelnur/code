#include <iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
using namespace std;
#define ll long long

bool dfsgreedy(pair<int,int> a, pair<int,int> b){
  int mn = min(min(a.first, a.second), min(b.first, b.second));
  return (mn == a.first || mn == b.second);
}

void  greedy(){
  int n; cin >> n;
   vector<pair<int,int>> v(n);
   for(int i = 0; i < n; i ++) cin >> v[i].first;
     for(int i = 0; i < n; i ++) cin >> v[i].second;

     sort(v.begin(), v.end(), dfsgreedy);

    ll ans = 0, a = 0;
    for (ll i = 0; i < n; i++)
        a += v[i].first, ans = max(a, ans) + v[i].second;
    cout << ans;
}

int main()
{
    greedy();  
}
