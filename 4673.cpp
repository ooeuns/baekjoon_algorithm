#include <cstdio>
using namespace std;

bool arr[10001] = {false, };



// 각 자릿수를 더하는 알고리즘에 문제가 있음.
int hap(int n, int result){ // 각 자릿수의 합을 더함.
    if(n==0)
        return result;
    else {
        result+=n%10;
        return hap(n/10, result);
    }   // 괄호 의문
}

void check (int n) {  // 재귀함수
    int sum = hap(n, 0);
    if (sum <= 10000) {
        check(sum);
    }
    else {
    arr[n] = true;
    }
}

int main() {

    for (int i=1; i < 10001; i++) {
        if (arr[i] == false) {
            check(i);
        }
    }

    for (int i=1; i<10001; i++) {
        if (arr[i] == false)
            printf("%d\n", i);
    }
    return 0;
}
