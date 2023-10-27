#include <bits/stdc++.h>
using namespace std;
#define mx 100005
vector<int>adj[mx];
bool vis[mx];
long long d;
void dfs(int u, int s) {
    vis[u] = true;
    for (auto x : adj[u]) {
        if (vis[x] == false) {
            d += s+1;
            dfs(x, s+1);
        }
    }}
void add(int u, int v)
{    adj[u].push_back(v);
    adj[v].push_back(u);}
int main()
{    int n, m;
    cin >> n ;
    int a[n+1];
    for (int i = 1; i <= n; i++) {
        cin  >> a[i];
       // add(i-1, v-1);
    }
   for(int i=1; i<=n; i++)
   {
       if (a[i] == -1) add(i, 0);
       else add(i, a[i]);
   }
    dfs(0,0);
    cout << d;
}
