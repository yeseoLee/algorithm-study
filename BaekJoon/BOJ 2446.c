#include <stdio.h>

int main(void)
{
    int n;
	scanf("%d", &n);

    // 역 피라미드 출력
    for (int i=n; i>0; i--){
        int space_count = n-i;
        int star_count = 2*i-1;
        for (int j=0; j< space_count; j++){
            printf(" ");
        }
        for (int j=0; j< star_count; j++){
            printf("*");
        }
        printf("\n");
    }

    // 피라미드 출력
    for (int i=2; i<n+1; i++){
        int space_count = n-i;
        int star_count = 2*i-1;
        for (int j=0; j< space_count; j++){
            printf(" ");
        }
        for (int j=0; j< star_count; j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}