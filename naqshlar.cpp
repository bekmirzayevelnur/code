#include <iostream>
#include <vector>

using namespace std;

using ll = long long;
using ld = long double;

const ld PI = 3.141592653589793;
const int MOD = 1e9+7;
const int INF = 1e9;
const ll INFLL = 4e18;
const double EPS = 1e-9;
const int MAXN = 1000*1007;

class BigInt{
    string digits;
public:
 
    BigInt(unsigned long long n = 0);
    BigInt(BigInt &);

    friend bool Null(const BigInt &);
    friend int Length(const BigInt &);
 
    BigInt &operator=(const BigInt &);
 
    friend BigInt &operator+=(BigInt &, const BigInt &);
    friend BigInt operator+(const BigInt &, const BigInt &);
 
    friend BigInt &operator*=(BigInt &, const BigInt &);
    friend BigInt operator*(const BigInt &, const BigInt &);
 
    friend ostream &operator<<(ostream &,const BigInt &);
};

BigInt::BigInt(unsigned long long nr){
    do{
        digits.push_back(nr % 10);
        nr /= 10;
    } while (nr);
}
//Big int by geeksforgeeks
BigInt::BigInt(BigInt & a){
    digits = a.digits;
}

bool Null(const BigInt& a){
    if(a.digits.size() == 1 && a.digits[0] == 0) return true;
    return false;
}

int Length(const BigInt & a){
    return a.digits.size();
}
 
BigInt &BigInt::operator=(const BigInt &a){
    digits = a.digits;
    return *this;
}

BigInt &operator+=(BigInt &a,const BigInt& b){
    int t = 0, s, i;
    int n = Length(a), m = Length(b);
    if(m > n)
        a.digits.append(m - n, 0);
    n = Length(a);
    for (i = 0; i < n;i++){
        if(i < m)
            s = (a.digits[i] + b.digits[i]) + t;
        else
            s = a.digits[i] + t;
        t = s / 10;
        a.digits[i] = (s % 10);
    }
    if(t)
        a.digits.push_back(t);
    return a;
}

BigInt operator+(const BigInt &a, const BigInt &b){
    BigInt temp;
    temp = a;
    temp += b;
    return temp;
}

 
BigInt &operator*=(BigInt &a, const BigInt &b)
{
    if(Null(a) || Null(b)){
        a = BigInt();
        return a;
    }
    int n = a.digits.size(), m = b.digits.size();
    vector<int> v(n + m, 0);
    for (int i = 0; i < n;i++)
        for (int j = 0; j < m;j++){
            v[i + j] += (a.digits[i] ) * (b.digits[j]);
        }
    n += m;
    a.digits.resize(v.size());
    for (int s, i = 0, t = 0; i < n; i++)
    {
        s = t + v[i];
        v[i] = s % 10;
        t = s / 10;
        a.digits[i] = v[i] ;
    }
    for (int i = n - 1; i >= 1 && !v[i];i--)
            a.digits.pop_back();
    return a;
}
BigInt operator*(const BigInt&a,const BigInt&b){
    BigInt temp;
    temp = a;
    temp *= b;
    return temp;
}

ostream &operator<<(ostream &out,const BigInt &a){
    for (int i = a.digits.size() - 1; i >= 0;i--)
        cout << (short)a.digits[i];
    return cout;
}

using ull = BigInt;

int n,m;
int a[41][8];
bool vis[1<<8][1<<8];
ull dp1[1<<8][1<<8];

ull calc(int p1, int p2){

    if(vis[p1][p2]) return dp1[p1][p2];
    vis[p1][p2] = 1;

    if(p1 == p2 && p1+1 == (1<<m)) return dp1[p1][p2] = BigInt(1ULL);
    int x1 = -1,x2 = -1;
    for(int i = 0; i < m; ++i){
        if((p1>>i&1) == 0) {
            x1 = i;
            break;
        }
    }

    for(int i = 0; i < m; ++i){
        if((p2>>i&1) == 0) {
            x2 = i;
            break;
        }
    }

    if(x1 == -1){
        if(x2+1 < m && (p2>>(x2+1)&1) == 0) {
            dp1[p1][p2] += calc( p1 , (p2|(1<<x2)|(1<<(x2+1))) );
        }
    } else if(x2 == -1){
        if(x1+1 < m && (p1>>(x1+1)&1) == 0) {
        }
    } else {
        if(abs(x1-x2) > 1){
            if(x1 < x2){
                if(x1+1 < m && (p1>>(x1+1)&1) == 0) {
                }
            } else {
                if(x2+1 < m && (p2>>(x2+1)&1) == 0) {
                    dp1[p1][p2] += calc( p1 , (p2|(1<<x2)|(1<<(x2+1))) ); 
                }
            }
        } else {
            if(x1 == x2){
                if(x1+1 < m && (p1>>(x1+1)&1) == 0) {
                } else if(x2+1 < m && (p2>>(x2+1)&1) == 0) {
                    dp1[p1][p2] += calc( p1 , (p2|(1<<x2)|(1<<(x2+1))) );
                }
                dp1[p1][p2] += calc( (p1|(1<<x1)) , (p2|(1<<x2)) );

                if(x1+1 < m && (p1>>(x1+1)&1) == 0 && x2+1 < m && (p2>>(x2+1)&1) == 0) {
           
                    dp1[p1][p2] += calc( (p1|(1<<x1)) , (p2|(1<<(x2+1))) );

                    dp1[p1][p2] += calc( (p1|(1<<x1)|(1<<(x1+1))) , (p2|(1<<x2)|(1<<(x2+1))) );
                }


                if(x1+1 < m && (p1>>(x1+1)&1) == 0) {
                    dp1[p1][p2] += calc( (p1|(1<<x1)|(1<<(x1+1))) , (p2|(1<<x2)) );
                }

                if(x2+1 < m && (p2>>(x2+1)&1) == 0) {
                    dp1[p1][p2] += calc( (p1|(1<<x1)) , (p2|(1<<x2)|(1<<(x2+1))) );
                }

            } if (x1+1 == x2){
                if(x1+1 < m && (p1>>(x1+1)&1) == 0) {
                }

                dp1[p1][p2] += calc( (p1|(1<<x1)) , (p2|(1<<x2)) );

                
                if(x1+1 < m && (p1>>(x1+1)&1) == 0) {
                    dp1[p1][p2] += calc( (p1|(1<<x1)|(1<<(x1+1))) , (p2|(1<<x2)) );
                }

            } else if(x2+1 == x1){

                if(x2+1 < m && (p2>>(x2+1)&1) == 0) {
                    dp1[p1][p2] += calc( p1 , (p2|(1<<x2)|(1<<(x2+1))) );
                }

                dp1[p1][p2] += calc( (p1|(1<<x1)) , (p2|(1<<x2)) );


                if(x2+1 < m && (p2>>(x2+1)&1) == 0) {
                    dp1[p1][p2] += calc( (p1|(1<<x1)) , (p2|(1<<x2)|(1<<(x2+1))) );
                }
            }
        }
    }

    return dp1[p1][p2];
}

ull ways(int p1, int p2, int idx){
    if(idx > 0){
        for(int i = 0; i < m; ++i){
            if(a[idx-1][i] == 1 && (p1>>i&1) == 0) return BigInt(0ULL);
        }
    }

    int new_mask = 0;
    for(int i = 0; i < m; ++i){
        if(a[idx][i] == 1){
            if((p2>>i&1) == 0) return BigInt(0ULL);
            new_mask |= (1<<i);
        } else {
            if((p2>>i&1) == 0) new_mask |= (1<<i);
        }
    }

    return calc(p1,new_mask);
}

ull dp[41][1<<8];
void solve(int NT){
    cin >> n >> m;
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    for(int i = 0; i < (1<<m); ++i){
        for(int j = 0; j < (1<<m); ++j){
            calc(i,j);
        }
    }

    dp[0][(1<<m)-1] = 1;
    for(int i = 1; i <= n; ++i){
        for(int k = 0; k < (1<<m); ++k){
            for(int j = 0; j < (1<<m); ++j){
                dp[i][j] += ways(k,j,i-1)*dp[i-1][k];
            }
        }
    }

    cout << dp[n][(1<<m)-1];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t = 1;
    #ifdef TESTCASES
        cin >> t;
    #endif
    for(int i = 1; i <= t; ++i){
        solve(i);
        cout << "\n";
    }
}
