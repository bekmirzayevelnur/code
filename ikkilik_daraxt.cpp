#include <iostream>

#include <cmath>

using namespace std;

int const mod = 1e9+7;

long long binpow(long long a, long long b, long long m){

    if(b == 0) return 1;

    

    long long k = binpow(a, b / 2, m) % m;

    k *= k;

    k %= m;

    if(b % 2 == 1) return (a * k) % m;

    return k;

}

long long binpow1(long long a, long long b, long long m) {

    a %= m;

    long long res = 1;

    while (b > 0) {

        if (b & 1)

            res = res * a % m;

        a = a * a % m;

        b >>= 1;

    }

    return res;

}

long long cnr(long long a, long long b, long long m){

    long long t = 1, d = 1;

    

    for(int i = 1; i <= b; i ++){

        t = (t * i) % m;

        d = (d * (a - i + 1)) % m;

    }

    return ((d * binpow(t, (m - 2), m))) % m;

}

int main(){

    long long n; cin >> n;

    long long d = cnr((2 * n), n, mod);  d *= binpow1(n + 1, mod - 2, mod); cout << d % mod << endl;

    return 0;

}
