#include <cstdio>
int main() {
    int t;  // 테스트 값
    scanf("%d", &t);

    int prime[10000];
    int pn=0;
    bool check[10001];

    int n;  // 소수의 합
    int ans[1][2]= {0, 10000};


    // 소수를 배열에 저장
    while (t--) {   //테스트의 수 만큼
        scanf ("%d", &n);
        if (n>=4 && n<=10000) { // n의 범위
            pn=0;
            for (int i=2; i<=n; i++) {
                if (check[i]==false) {
                    prime[pn++]=i;
                    for (int j=i*2; j<=n; j+=i) {
                        check[j]=true;
                    }
                }
            }

            ans[0][0]=0;
            ans[0][1]=10000;
            for (int x=0, y=0; x<pn; x++) {
                y = n - prime[x];
                if(check[y]==false) {
                    if ((y-prime[x]<ans[0][1]-ans[0][0]) && (y-prime[x] >=0)) {
                        ans[0][0] = prime[x];
                        ans[0][1] = y;
                    }
                }

            }
        }
        printf("%d %d\n", ans[0][0], ans[0][1]);

    }
    return 0;
}
