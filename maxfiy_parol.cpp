#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class yechim {
private:
    vector<int> p;
    vector<int> r;

public:
    yechim(int s) {
        p.resize(s);
        r.resize(s, 0);
        for (int i = 0; i < s; i++) {
            p[i] = i;
        }
    }

    int f(int x) {
        if (x != p[x]) {
            p[x] = f(p[x]);
        }
        return p[x];
    }

    void u(int x, int y) {
        int rx = f(x);
        int ry = f(y);

        if (rx == ry) {
            return;
        }

        if (r[rx] < r[ry]) {
            p[rx] = ry;
        } else if (r[rx] > r[ry]) {
            p[ry] = rx;
        } else {
            p[ry] = rx;
            r[rx]++;
        }
    }

    int g() {
        int c = 0;
        for (int i = 0; i < p.size(); i++) {
            if (p[i] == i) {
                c++;
            }
        }
        return c;
    }
};

int c(int n, const vector<string>& a) {
    unordered_map<char, int> m;
    yechim d(n);

    for (int i = 0; i < n; i++) {
        const string& s = a[i];
        for (char c : s) {
            if (m.find(c) == m.end()) {
                m[c] = i;
            } else {
                d.u(i, m[c]);
            }
        }
    }

    return d.g();
}

int main() {
    int n;
    cin >> n;

    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int r = c(n, a);
    cout << r << endl;
}
