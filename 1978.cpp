#include <cstdio>
bool prime (int n) {
    if (n<2) {
    return false;
    }
    for (int i=2; i*i <= n; i++) {
        if(n%i ==0) {
            return false;
        }
    }
    return true;
}

int main () {
    int num, count=0;
    int arr[100];
    scanf("%d", &num);
    for (int i=0; i<num; i++) {
        scanf("%d", &arr[i]);
    }
    for (int i=0; i<num; i++) {
        if(prime(arr[i])==true)
            count++;
    }
    printf("%d", count);
    return 0;
}
