#include <cstdio>
int gcd (int a, int b) {
    if(b==0) {
        return a;
    } else {
        return gcd (b, a%b);
    }
}

int main() {
    long long int a, b;
    long long int lcm=0;

        scanf("%d %d", &a, &b); // 두 수 입력
        lcm = (a*b)/gcd(a, b);
        printf("%lld", lcm);


    return 0;
}
