#include <iostream>
using namespace std;
int main(){
    long long n, m;
    cin >> n >> m;
    if(n < m || n > m*5)
        cout << "-1 -1";
    else
        cout << max((long long)0, n-m*4) << ' ' << (n-m)/4;
    return 0;
}
