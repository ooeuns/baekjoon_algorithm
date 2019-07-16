#include <iostream>

using namespace std;

int n;
int a[10001];   // 전역변수로 초기화시 배열의 모든 index는 0으로 초기화가 됨.

int main(void) {
    scanf("%d", &n);    // 데이터에 개수를 입력
    for(int i=0; i<n; i++) {
        int x;
        scanf("%d", &x);
        a[x]++;
    }
    for(int i=0; i<10001; i++) {
        while(a[i] != 0) {
            printf("%d\n", i);
            a[i]--;
        }
    }
    return 0;
}