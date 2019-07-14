#include <cstdio>
int gcd (unsigned long long int a, unsigned long long int b) {
    if(b==0) {
        return a;
    } else {
        return gcd (b, a%b);
    }
}

int main() {
    unsigned long long int x, y;
    int Cdiv;
    scanf("%lld %lld", &x, &y);
    Cdiv = gcd(x,y);
    while (Cdiv) {
        Cdiv--;
        printf("1");
    }

    return 0;

}
