#include<iostream>
using namespace std;
int main(void) {
    int num;
    scanf("%d", &num);

    int write = num*2-1;
    
    if(num >=0 && num <= 100) {
        // top
        for(int i=1; i<num; i++) {
            for(int k=1; k<i; k++) {
                printf(" ");
            }
            for(int j=0; j<write; j++) {
                printf("*");
            }
            write-=2;
            printf("\n");
        }
        // bottom
        int write = 1;
        int blank = num-1;
        for(int i=0; i<num; i++) {
            for(int k=0; k<blank; k++) {
                printf(" ");
            }
            for(int j=0; j<write; j++) {
                printf("*");
            }
            blank--;
            write+=2;
            printf("\n");
        }


    }
 
    return 0;
}