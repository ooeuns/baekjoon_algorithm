#include<iostream>
using namespace std;

int main(void) {
    int num;
    scanf("%d", &num);
    if(num >=1 && num<=100) {
        // 삼각형
        int blank = num-1;
        int write = 1;
        for(int q=0; q<num; q++) {  // enter
            for(int i=0; i<blank; i++) {
                printf(" ");
            }
            for(int i=0; i<write; i++) {
                printf("*");
            }
            printf("\n");   // 줄 바꿈
            write +=2;
            blank--;
        }  
        // 역삼각형 (-1)
        int n=1;
        num--;
        for(int i=0; i<num; i++) {
            
            int write = 2*num-n;
            for(int j=0; j<=i; j++) {
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