#include <iostream>
using namespace std;
int main(){
    int n, m, r;
    cin >> n >> m >> r;
    cout << (min(n, m)+2*r)/(2*r+1);
    return 0;
}
