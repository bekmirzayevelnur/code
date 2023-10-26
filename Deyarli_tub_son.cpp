#include<bits/stdc++.h>

using namespace std;

long long hcf(long long a,long long b){

  if(a%b==0)

  return a;

  return a/__gcd(a,b)*b;

}

int main(){

  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  long long n, ans;

  int t, a, b, c, d;

  cin>>t;

  while(t--){

    cin>>n>>a>>b>>c>>d;

    ans=n-(n/a+n/b+n/c+n/d-n/hcf(a,b)-n/hcf(a,c)-n/hcf(a,d)-n/hcf(b,c)-n/hcf(b,d)-n/hcf(c,d)+n/hcf(a,hcf(b,c))+n/hcf(a,hcf(c,d))

    +n/hcf(a,hcf(b,d))+n/hcf(b,hcf(c,d))-n/hcf(hcf(a,b),hcf(c,d)));

    cout<<ans<<"\n";

  }

  return 0;

}
