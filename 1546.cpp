#include <cstdio>
int main() {
    int n;  //과목 수
    double arr[1000];
    int max=0;
    double ave=0;

    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%lf", &arr[i]);
    }

    //최대 값 구하기
    for (int j=0; j<n; j++) {
        if (max<arr[j]) {
            max=arr[j];
        }
    }

    for(int k=0; k<n; k++) {
        arr[k]=arr[k]/max*100;
        //    printf("%d ", arr[k]);
    }

    for (int m=0; m<n; m++) {
        ave+=arr[m];
    }

    printf("%0.2lf", ave/n);

    return 0;
}
