#include <iostream>
#include <vector>

int dist(int i,int j) {
    return abs(i/4-j/4)+abs(i%4-j%4);
}

int main(){
    std::vector<char>a(16);
    std::vector<int>b(16);
    for (int i=0;i<16;i++){
        std::cin>>a[i];
        if (a[i]=='.')b[15]=i;
        else b[a[i]-'A']=i;
    }
    int ans=0;
    for (int i=0;i<15;i++){
        if (a[i]=='.'){
            int j=i;
            while (j!=15){
                ans+=dist(j,b[j]);
                std::swap(a[j],a[b[j]]);
                j=b[j];
            }
            break;
        }
    }
    for (int i=0;i<15;i++){
        if (a[i]!=i+'A'){
            int j=i,sum=0,mn=1e9;
            do{
                sum+=dist(j,a[j]-'A');
                mn=std::min(mn,dist(j,15)+dist(15,a[j]-'A')-dist(j,a[j]-'A'));
                a[j]='A'+j;
                j=b[j];
            } while (i!=j);
            ans+=sum+mn;
        }
    }
    std::cout<<ans;
    return 0;
}
