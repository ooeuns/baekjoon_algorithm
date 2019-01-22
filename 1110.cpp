#include <cstdio>
int main() {
    int n, temp, some;
    int ten, one;
    int count=0;

    scanf("%d", &n);
    if (n>=0 && n<=99) {
        temp = n;
        do {
            if (temp < 10) { // n이 10보다 작다면
                temp = temp * 10 + temp;
                count++;
            }
            else if (temp % 10 == 0) {   // 1의 자리 수가 0인 경우
                temp = temp/10;
                count++;
            }
            else if (temp >= 10) {    // n이 10이상이라면
                ten = temp/10;
                one = temp%10;
                some = ten + one;
                temp = some % 10 + one * 10;
                count++;
            }
        } while (temp!=n);

        printf("%d", count);
    }
    return 0;
}
