#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;
int main(){
    vector<ll> v;
    set<ll> s;
    ll q;
    for(int i = 0; i < 10; i++){
        v.push_back(i);
        s.insert(i);
    }
    ll d[19] = {1};
    for(int i = 1; i <= 18; i++)
        d[i] = d[i - 1] * 10;
    for(int i = 1; i < v.size(); i++){
        for(int l = 1; l <=18; l++){
           q = v[i] * l;
           if(q >= d[18]) break;
           if(d[l-1] <= q and q < d[l] and s.find(q) == s.end()){
               s.insert(q);
               v.push_back(q);
           }
        }
    }
    sort(v.begin(), v.end());
    ll t, l, r;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> l >> r;
        cout << upper_bound(v.begin(), v.end(), r) - lower_bound(v.begin(), v.end(), l) << '\n';
    }
    return 0;
}
