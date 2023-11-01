#include <bits/stdc++.h>
using namespace std;
int main(){  
  int n;
  cin>>n;
  vector<int> v(n);
  for(int i=0; i<n; i++)cin>>v[i];
  
  vector<vector<int>> g;
  for(int i=0; i<4000; i++){
    vector<int> h(n);
    g.push_back(h);
  }
  bool used[4000] = {0};
  used[0] = 1;
  for(int i=0; i<n; i++){
    for(int j = 1; j<=4000; j++){
      if (j-v[i]>=0){
        if(used[j - v[i]] && !used[j]){
          for(int ind = 0; ind<n; ind++){
            g[j][ind] = g[j - v[i]][ind];
          }
          g[j][i] += 1;
          used[j] = 1;
        }
      }
    }
  }
  int q;
  cin>>q;
  for(int i=0; i<q; i++){
    int a;
    cin>>a;
    for(int j = a; j>=0; j--){
      if(used[j]){
        cout<<j<<endl;
        for(int ind = 0; ind<n; ind ++){
          cout<<g[j][ind]<<" ";
        }
        cout<<endl;
        break;
      }
    }
  }  
  return 0;
}
