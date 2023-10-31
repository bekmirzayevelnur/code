#include <iostream>
using namespace std;
using ll = long long;
int main()
{
    ll n;
    cin >> n;
    ll ans = 0, k = 1;
    for (ll i = 1; i < n; ++i)
    {
        k = 1;
        while (k * i < n)
        {
            if (k == i)
            {
                ++k;
                continue;
            }
            ll m = n - k * i;
            if (m != i && m != k)
                ++ans;
            ++k;
        }
    }
    cout << ans;
}
