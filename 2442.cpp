#include <iostream>
using namespace std;


void starStamp(int num) {
    int zero = num-1;
    int star = 1;
    for(int j=1; j<=num; j++) {
        for(int i=0; i<zero; i++) {
            printf(" ");
        }
        for(int i=0; i<star; i++) {
            printf("*");
        }
        printf("\n");
        zero--;
        star = 2*(j+1)-1;
    }
}

int main(void) {
int n;
scanf("%d", &n);
starStamp(n);
return 0;

}