#include<iostream>
#include<string.h>
#define rep(i,j,k) for(register int i = j; i <= k; ++i)
#define dow(i,j,k) for(register int i = j; i >= k; --i)

using namespace std;
 
inline int read() { 
    int s = 0, t = 1; char c = getchar();
    while( !isdigit(c) ) { if( c == '-' ) t = -1; c = getchar(); }
    while( isdigit(c) ) s = s * 10 + c - 48, c = getchar();
    return s * t;
}

const int N = 4e6+5, inf = 1e9+7;
int n, m, maxl, now, pre, f[2][N], v[N], g[N], h[N], sum[N]; 

int main() {
  n = read(), m = read(), now = 0, pre = 1;
  rep(i,1,n) { 
    swap(now,pre); 
    rep(j,1,m) v[j] = read();
    rep(j,1,m) sum[j] = sum[j-1] + v[j];
    rep(j,1,m) g[j] = max(g[j-1]+v[j],0);
    dow(j,m,1) h[j] = max(h[j+1]+v[j],0);
    maxl = -inf;
    rep(j,1,m) { 
      maxl = max(maxl,f[pre][j]-sum[j-1]+g[j-1]);
      f[now][j] = maxl+sum[j]+h[j+1];
    } 
    maxl = -inf;
    dow(j,m,1) { 
      maxl = max(maxl,f[pre][j]+sum[j]+h[j+1]);
      f[now][j] = max(f[now][j],maxl-sum[j-1]+g[j-1]);
    }
  }
  int ans = 0;
  rep(i,1,m) ans = max(ans,f[now][i]);
  cout<<ans;
  return 0;
}// in code we trust
