#include <cstdio>
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
typedef long long ll;
int const mod = 1e9+7;
int p[60][3][3];
void copy(int a[][3],int c[][3]){
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            a[i][j]=c[i][j];
}
int c[3][3];
void mult(int a[][3],int b[][3]){
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            c[i][j]=0;
            for(int k=0;k<3;k++)
                c[i][j]=(c[i][j]+a[i][k]*1LL*b[k][j]%mod)%mod;
        }
    }
    copy(a,c);
}
int main(){
 p[0][0][0]=p[0][0][1]=p[0][0][2]=p[0][1][0]=p[0][2][1]=1;
 for(int i=1;i<60;i++){
  copy(p[i],p[i-1]);
  mult(p[i],p[i]);
 }
   freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 int t;
 scanf("%d",&t);
 while(t--){
  ll n;
       scanf("%lld",&n);
  int r[3][3];
    for(int i=0,ok=1;i<60;i ++)
    if((n>>i)&1){
    if(ok){
    copy(r,p[i]);
    ok=0;
    }else
      mult(r,p[i]);
    }
 printf("%d\n",((r[0][0]+r[1][0])%mod+r[2][0])%mod);
}
}
