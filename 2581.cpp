#include <cstdio>
int main() {
    int prime[10000]; // 소수저장
    int pn = 0; // 소수의 개수
    bool check[10001];    // 지워졌으면 true
    int m, n;    //100까지 소수
    int total=0;
    int min=0;


    scanf("%d %d", &m, &n);

    for (int i=2; i<=n; i++) {
        if(check[i]==false) {
            prime[pn++] = i;
            for (int j= i*i; j<=n; j+=i) {
                check[j]=true;
            }
        }
    }
    for (int i=0; i<pn; i++) {
        if (prime[i]>=m && prime[i]<=n) {
            total+=prime[i];
        }
    }
    for (int i=0; i<pn; i++) {
        if (prime[i]>=m && prime[i]<=n) {
            min=prime[i];
            break;
        }
    }
    if(total!=0) {
        printf("%d\n", total);
        printf("%d", min);
    } else {printf("-1");}
    return 0;
}
