#include <iostream>
using namespace std;
int main() {
    int m, b;
    cin >> m >> b;
    long long mx = 0;
    for (int y = 0; y <= b; y++) {
        int x = m * (b - y);
        long long mn = (x + 1LL) * (y + 1LL) * (x + y) / 2;
        mx = max(mx, mn);
    }
    cout << mx;
}
