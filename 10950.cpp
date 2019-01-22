#include <cstdio>
int main() {
    int a,b;
    int t;
    scanf("%d", &t);

    for (int i=0; i<t; i++) {
        scanf("%d %d", &a, &b);
        if (a>0 && b<10) {

            printf("%d\n", a+b);
        }
    }
    return 0;
}
