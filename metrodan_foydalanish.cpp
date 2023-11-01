#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int> > d(n + 1, vector<int>(n + 1, 1e8));

    for (int i = 1; i <= n; i++){
        d[i][i] = 0;
    }

    for (int i = 1; i <= m; i++){
        int x, y;
        cin >> x >> y;
        d[x][y] = d[y][x] = 1;
    }

    for (int k = 1; k <= n; k++){
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    int q;
    cin >> q;

    while (q--){
        int x, y;
        cin >> x >> y;
        if (d[x][y] == 1e8){
            cout << -1 << endl;
        } else {
            cout << d[x][y] << endl;
        }
    }

    return 0;
}
