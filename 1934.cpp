#include <cstdio>
int gcd (int a, int b) {
    if(b==0) {
        return a;
    } else {
        return gcd (b, a%b);
    }
}

int main() {
    int t;  //테스트 개수
    int a, b;
    scanf("%d", &t);    // 테스트 개수 입력

    for (int j=0; j<t; j++) {   // 테스트 개수
        scanf("%d %d", &a, &b); // 두 수 입력
        printf("%d\n", (a*b)/gcd(a, b));
    }

    return 0;
}
