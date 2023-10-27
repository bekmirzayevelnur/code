#include <iostream>
#include <vector>
using namespace std;
int main() {
  int a,n=0;
  cin>>a;
  vector<int>A,w(a);
  for(int i=0; i<a; i++)A.emplace_back(i);
  for(int i=1; i<=a; i++) {
    n+=i;
    n%=A.size();
    w[A[n]]=i;
    A.erase(A.begin()+(n));
  }
  for(int i=0; i<a; i++)cout<<w[i]<<" ";
}
