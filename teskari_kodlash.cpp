#include <bits/stdc++.h>

using namespace std;

int main()
{
  int t,m,n;
  cin >> t;
  for(int i=1; i<=t;i++)
  {
    cin >> n >> m;
    if(n*(n+1)/2==m) cout <<1;
    else cout << 0;
  }
  return 0;
}
