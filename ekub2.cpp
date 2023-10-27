#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    int n; long long s = 0; cin >> n;
    vector <int> a(2 * n);
    for(int &x: a){
        cin >> x; s += x;
    }
    
    int inf = s / n;
    vector <int> divs;
    
    for(int i = 1, j; 1LL * i * i <= s; i ++){
        if(s % i == 0){
            divs.push_back(i);
            j = s / i;
            if(i != j && j <= inf) divs.push_back(j); 
        }
    }
    
    sort(divs.rbegin(), divs.rend());
    int i = -1, mod, l, r;
    vector <int> b(2 * n);
    
    while(true){
        mod = divs[++ i];
        for(int i = 0; i < 2 * n; i ++) b[i] = a[i] % mod;
        
        sort(b.begin(), b.end());
        l = 0; r = 2 * n - 1;
        
        while(l <= r && b[l] == 0) l ++;
        
        if(l % 2 != 0) continue;
        
        while(l < r && b[l]+b[r] == mod) l ++, r --;
        if(l < r) continue;
        break;
    }
    
    cout << divs[i] << endl;
    return 0;//
}
