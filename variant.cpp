#include<iostream>
#include<cmath>
#define qol 1000000007
using namespace std;
int main()
{
 long long T,n,k,x,a=1;
 cin>>T;
 for(int j=0;j<T;j++)
{
 cin>>n>>k;
 if(n<=0 && k>=0) 
 {
  x=k-n;
 }
 else { x=k-n+1; }
 a=(a*x)%qol;
}
cout<<a%qol; cout<<endl;
}
