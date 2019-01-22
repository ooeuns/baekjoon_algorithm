#include <cstdio>
int main() {
    int num, n;
    int arr[10000];
    scanf("%d %d", &num, &n);
    for(int i=0; i<num; i++) {
        scanf("%d", &arr[i]);
    }
    for (int j=0; j<num; j++) {
        if (arr[j]<n) {
            printf("%d ", arr[j]);
        }
    }
    return 0;
}
