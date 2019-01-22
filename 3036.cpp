#include <cstdio>
int gcd (int a, int b) {
    if(b==0) {
        return a;
    } else {
        return gcd (b, a%b);
    }
}

int main() {
    int n;
    int temp;
    int arr[101];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {   //링의 갯수
        scanf("%d", &arr[i]);
    }

    for (int i=1; i<n; i++) {
        temp = gcd(arr[0], arr[i]);
        printf("%d/%d\n", arr[0]/temp, arr[i]/temp);
    }

    return 0;
}
