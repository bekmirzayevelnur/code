#include <stdio.h>
#include <stdlib.h>
int main() 
{
    long n;
    scanf("%li", &n);
    long m;
    scanf("%lli", &m);
    m -= 1;
    int i;
    long *a = (long *)malloc(n * sizeof(long));
    long *b = (long *)malloc(n * sizeof(long));
    long *t;
    for(i=0; i<n; i++) 
  {
        scanf("%li", a+i);
    }
    long ans = 1;
    while (m > 0) 
  {
        if (m & 1) 
    {
            for(i=0; i<n; i++) 
      {
                if (i+ans < n) 
        {
                    b[i] = a[i] ^ a[i+ans];
                } 
        else 
        {
                    b[i] = a[i] ^ a[i+ans-n];
                }
            }
            t = a;
            a = b;
            b = t;
        }
        ans <<= 1;
        if (ans >= n) 
    {
            ans-= n;
        }
        m >>= 1;
    }
    printf("%li", a[0]);
    for(i=1; i<n; i++) 
  {
        printf(" %li", a[i]);
    }
    printf("\n");
  
}
