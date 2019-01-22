#include <cstdio>
int main() {
    int prime[300000];
    int pn=0;
    bool check[300000];
    int n;

    while(1) {
        scanf("%d",&n);
        if (n!=0) {
        pn=0;
            for (int i=2; i<=n*2; i++) {
                if (check[i] == false) {
                    if (i>n) {
                        prime[pn++] = i;
                        }
                    for (int j= i*2; j<=n*2; j+=i) {
                        check[j] = true;
                    }
                }
            }
            printf("%d\n", pn);
        } else {
            return 0;}
    }
}
