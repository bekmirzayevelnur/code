#include<iostream>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0); 
  int m,n,r;
  cin>>m>>n>>r;
  int a[300][300];
  for(int i = 0 ; i < m ; ++i)
  {
      for(int j = 0; j < n ; ++j)
      {
        cin>>a[i][j];
    }   
  }
  ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0); 
  int left = 0,right = n-1,top = 0,down = m-1,tleft = 0,tright = n-1,ttop = 0,tdown = m-1,b[300][300],k,size,temp[1200];
  while(true)
  {
      k=0;
      for(int i = left; i <= right ; ++i)
      {
          temp[k] = a[top][i];
          ++k;
      }
      ++top;
      if(top > down  or left > right) 
          break;
      for(int i = top; i <= down ; ++i)
      {
          temp[k]=a[i][right];
          ++k;
      }
      --right;
      if(top > down or left > right) 
          break;
      for(int i = right; i >= left ; --i)
      {
          temp[k] = a[down][i];
          ++k;
      }
      --down;
      if(top > down or left > right) 
          break;
      for(int i = down; i >= top ; --i)
      {   
          temp[k] = a[i][left];
          ++k;
      }
      ++left;
      if(top > down and left > right) 
          break;
      size = k;
      k=0;
      for(int i = tleft; i <= tright ; ++i)
      {
          b[ttop][i] = temp[(k + (r%size))%size];
          ++k;
      }
      ++ttop;
      for(int i = ttop; i <= tdown ; ++i)
      {
          b[i][tright]=temp[(k + (r%size))%size];
          ++k;
      }
      --tright;
      for(int i = tright; i >= tleft ; --i)
      {
          b[tdown][i] = temp[(k + (r%size))%size];
          ++k;
      }
      --tdown;
      for(int i = tdown; i >= ttop ; --i)
      {   
          b[i][tleft] = temp[(k + (r%size))%size];
          ++k;
      }
      ++tleft;
  }
  ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0); 
  size=k;
  k=0;
  if(top != ttop){
      for(int i = tleft; i <= tright ; ++i)
      {
          b[ttop][i] = temp[(k + (r%size))%size];
          ++k;
      }
      ++ttop;
  }
  if(right!=tright){
      for(int i = ttop; i <= tdown ; ++i)
      {
          b[i][tright]=temp[(k + (r%size))%size];
          ++k;
      }
      --tright;
  }
  if(down!=tdown){
      for(int i = tright; i >= tleft ; --i)
      {
          b[tdown][i] = temp[(k + (r%size))%size];
          ++k;
      }
      --tdown;
  }
  if(left!=tleft){
      for(int i = tdown; i >= ttop ; --i)
      {   
          b[i][tleft] = temp[(k + (r%size))%size];
          ++k;
      }
  
      ++tleft;
  }
  for(int i = 0 ; i < m ;++i){
      for(int j = 0 ; j < n ;++j)
      {
        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0); 
        cout<<b[i][j]<<" ";
    } 
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0); 
      cout<<"\n";
  }
  return 0;
}
