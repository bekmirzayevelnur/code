#include<bits/stdc++.h>
#define ll long long
using namespace std;

const ll MOD = 1e9+7;
ll n,m,p=1;

// base^p
ll bin_pow(ll base, ll p) {
    if (p<2) return base;
    if (p%2) return bin_pow(base, p-1)*base%MOD;
    
    ll t = bin_pow(base, p/2);
    return t*t%MOD; 
}

// (a/b) mod m
ll divide(ll a, ll b) {
    return a*bin_pow(b, MOD - 2)%MOD;
}

int main(){
  cin>>n>>m;
  n--,m--;
  for(;n;n--) p=p*divide(n+m,n)%MOD;
  for(;m;m--) p=p*divide(m,  m)%MOD;
  cout<<p;
}
