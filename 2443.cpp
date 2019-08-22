#include<iostream>
using namespace std;

int main(void) {
    int num =0;
    scanf("%d", &num);
    if(1<=num && num<=100) {
        int n=1;
        for(int i=0; i<num; i++) {
            
            int write = 2*num-n;
            for(int j=0; j<i; j++) {
                printf(" ");
            }
            for(int y=0; y<write; y++) {
                printf("*");
            }
            printf("\n");
            n+=2;
        }
    }

    return 0;
}