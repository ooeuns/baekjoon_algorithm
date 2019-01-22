#include <cstdio>
int main() {
    bool check[1000001];
    int m, n;

    scanf("%d %d", &m, &n);

    for (int i=2; i<=n; i++) {
        if (check[i] == false) {
            if (i>=m && i<=n) {
            printf("%d\n", i);
            }
            for (int j= i*2; j<=n; j+=i) {
                check[j] = true;
            }
        }
    }
    return 0;
}
