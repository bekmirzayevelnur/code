#include <bits/stdc++.h> 
 
using namespace std; 
 
typedef long long ll; 
 
const int N = 1e6 + 55; 
 
pair<int, int> t[N]; 
int lz[N]; 
inline pair<int, int> combine(pair<int, int> lf, pair<int, int> rg){ 
  if (lf.first < rg.first) return lf; 
  if (lf.first > rg.first) return rg; 
  return make_pair(lf.first, lf.second + rg.second); 
} 
 
inline void build(int v, int tl, int tr){ 
  if (tl == tr){ 
    t[v] = make_pair(0, 1); 
    lz[v] = -1; 
    return; 
  } 
   
  int tm = (tl + tr) >> 1; 
  build(v << 1, tl, tm); 
  build(v << 1 | 1, tm + 1, tr); 
   
  t[v] = combine(t[v << 1], t[v << 1 | 1]); 
} 
 
inline void push(int v, int tl, int tr){ 
  if (lz[v] == -1 || tl == tr) return; 
   
  int val = lz[v]; 
  int tm = (tl + tr) >> 1; 
 
  lz[v << 1] = val; 
  t[v << 1] = make_pair(val, tm - tl + 1); 
 
  lz[v << 1 | 1] = val; 
  t[v << 1 | 1] = make_pair(val, tr - tm); 
 
  lz[v] = -1; 
} 
 
inline void update(int v, int tl, int tr, int l, int r, int val){ 
  push(v, tl, tr); 
 
  if (tl > r || tr < l) return; 
  if (l <= tl && tr <= r){ 
    t[v] = make_pair(val, tr - tl + 1); 
    lz[v] = val; 
    return; 
  } 
   
  int tm = (tl + tr) >> 1; 
 
  update(v << 1, tl, tm, l, r, val); 
  update(v << 1 | 1, tm + 1, tr, l, r, val); 
 
  t[v] = combine(t[v << 1], t[v << 1 | 1]); 
} 
 
int main(){ 
  ios_base::sync_with_stdio(false); 
 
  int n, q; 
  cin >> n >> q; 
     
    build(1, 1, n); 
     
  while (q--){ 
    int type; 
    cin >> type; 
     
    if (type == 1){ 
      int l, r, val; 
      cin >> l >> r >> val; 
      update(1, 1, n, l, r, val); 
    } else { 
      cout << t[1].second << "\n"; 
    } 
  } 
   
  return 0; 
}
