#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e5 + 5, M = 4e6 + 5;
int head[M], nxt[M], to[M], edge[M], tot;
int id[M], cnt, ls[M], rs[M];
int rt1, rt2;
void add(int x, int y, int z) {
    nxt[++tot] = head[x];
    head[x] = tot;
    to[tot] = y;
    edge[tot] = z;
}
void buildin(int &p, int l, int r) {
    if (l == r) {
        p = l;
        return;
    }
    p = ++cnt;
    int mid = l + r >> 1;
    buildin(ls[p], l, mid);
    buildin(rs[p], mid + 1, r);
    add(ls[p], p, 0);
    add(rs[p], p, 0);
}
void buildout(int &p, int l, int r) {
    if (l == r) {
        p = l;
        return;
    }
    p = ++cnt;
    int mid = l + r >> 1;
    buildout(ls[p], l, mid);
    buildout(rs[p], mid + 1, r);
    add(p, ls[p], 0);
    add(p, rs[p], 0);
}
void link(int p, int l, int r, int x, int y, int v, int u, int op) {
    if (x <= l && y >= r) {
        op == 2 ? add(u, p, v) : add(p, u, v);
        return;
    }
    int mid = l + r >> 1;
    if (x <= mid) link(ls[p], l, mid, x, y, v, u, op);
    if (y > mid) link(rs[p], mid + 1, r, x, y, v, u, op);
}
const int INF = 1e18;
priority_queue<pair<int, int> > q;
int d[M];
bool vis[M];
void dijkstra(int s, int n) {
    for (int i = 0; i <= cnt; i++) d[i] = INF;
    d[s] = 0;
    q.push(make_pair(0, s));
    while (q.size()) {
        int u = q.top().second;
        q.pop();
        if (vis[u]) continue;
        vis[u] = true;
        for (int i = head[u]; i; i = nxt[i]) {
            int v = to[i], Val = edge[i];
            if (d[v] > d[u] + Val) {
                d[v] = d[u] + Val;
                q.push(make_pair(-d[v], v));
            }
        }
    }
}
signed main() {
    int n, q, s;
    scanf("%lld%lld%lld", &n, &q, &s);
    cnt = n;
    buildin(rt1, 1, n);
    buildout(rt2, 1, n);
    while (q--) {
        int op, l, r, w, v, u;
        scanf("%lld", &op);
        if (op == 1) {
            scanf("%lld%lld%lld", &u, &v, &w);
            add(u, v, w);
        } else {
            scanf("%lld%lld%lld%lld", &v, &l, &r, &w);
            link(op == 2 ? rt2 : rt1, 1, n, l, r, w, v, op);
        }
    }
    dijkstra(s, n);
    for (int i = 1; i <= n; i++) printf("%lld ", d[i] == INF ? -1 : d[i]);
    puts("");
    return 0;
}
