#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n, m, l, r;
    cin >> n >> m;
    vector<int> a(n), b(n);
    vector<pair<int, int>> c(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i] >> b[i];
        c[i] = {a[i], b[i]};
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for (int i = 0; i < n; ++i)
    {
        int l = lower_bound(b.begin(), b.end(), c[i].first) - b.begin();
        int r = upper_bound(a.begin(), a.end(), c[i].second) - a.begin();
        cout << r - l - 1 << endl;
    }
}
