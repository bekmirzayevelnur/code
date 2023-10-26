#include <bits/stdc++.h>

using namespace std;

#define all(x) (x).begin(), (x).end()

#define int long long

#define ll long long

#define ff first

#define ss second

#define mp make_pair

#define pb push_back

#define pf push_front

const double eps = 0.000001;

const int MOD = 1e9 + 7;

const int INF = 1000000101;

const long long LLINF = 1223372000000000555;

const int N = 2e6 + 3e2;

const int M = 5222;

const int maxn= 100;

int a[N], result = 0;

int ayirma=0;

void merge_sort(int a[], int l, int r){

    if(l == r - 1) return;

    int m = (l + r) / 2;

    merge_sort(a, l, m);

    merge_sort(a, m, r);

    for(int i = l, j = m; i < m; i ++){

        while(j < r && a[j] < a[i]) j ++;

        result += j - m;

    }

    inplace_merge(a+l, a+m, a+r);

}

void t_main(){

    int n, k; cin >> n;

    k = 1;

    for(int i = 0; i < k; i ++){

        for(int j = 0; j < n; j ++){

            cin >> a[j];

        }

        merge_sort(a, 0, n);

    }

    cout << result-ayirma<<"\n";

    ayirma=result;

}

signed main(){

    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int tt;

    cin>>tt;

    while(tt --) t_main();

    return 0;

}
