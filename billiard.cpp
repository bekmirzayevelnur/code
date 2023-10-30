#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll top(ll a, ll b){
    if(b%2==0 and a%2!=0)
                return 4;
    else if(b%2!=0 and a%2!=0)
                return 3;
    else if(b%2!=0 and a%2==0)
                return 2;
                else return 1;
    
    
}
void reduceFraction(ll x, ll y)
{
  ll d;
  d = __gcd(x, y);

  x = x / d;
  y = y / d;
    
  cout <<  x + y - 2 <<  " " << top(x, y);
}
int main()
{
    ll a, b;
    cin >> a >> b;
    reduceFraction(a,b);
}
