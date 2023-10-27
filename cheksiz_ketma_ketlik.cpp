#include <iostream>
using namespace std;
int main()
{
     long long n,sum=0,j;
     cin>>n;
     for(int i=0;i<n;i++){
       if(sum>=n) break;
       else sum+=i;
       j=i;
     }
     cout << n-sum+j;
}
