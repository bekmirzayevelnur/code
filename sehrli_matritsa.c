main() {
    int i=0,j,a[3][3];
    for(;i<3;i++)
            for(j=0;j<3;j++)
                scanf("%d", &a[i][j]);
    if(a[0][1]+a[0][2]==a[1][0]+a[2][0]&&a[2][0]+a[2][1]==a[0][2]+a[1][2]){
        a[1][1]=(a[2][0]+a[0][2])/2;
        a[0][0]=a[2][0]+a[1][1]-a[0][1];
        a[2][2]=a[0][2]+a[1][1]-a[2][1];
        for(i=0;i<3;i++){
            for(j=0;j<3;j++)
                printf("%d ",a[i][j]);
            puts("");
        }
    }
    
    else printf("-1");
    return 0;
}