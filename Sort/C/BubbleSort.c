#include<stdio.h>
#include<stdlib.h>
#define SWAP(a,b) {int t; t=a; a=b; b=t;} //swap 매크로 함수
void bubbleSort(int* ar, int n);
void printArray(int* ar, int n);

int main() {
	int n, i;
	int* ar;
	scanf("%d", &n); //배열의 개수
	ar = (int*)malloc(sizeof(int) * n); //길이가 n인 배열 동적할당
	for (i = 0; i < n; i++) {
		scanf("%d", (ar+i)); 
	}
	bubbleSort(ar, n); //정렬
	printArray(ar, n); //출력
	return 0;
}
void bubbleSort(int* ar, int n) {
	int i,j;
	for (i = 0; i < n - 1; i++) { 
		for (j = 0; j < n - 1 - i; j++) { //n-1개를 정렬하면 마지막 1개는 자동으로 정렬된다
			if (ar[j] >= ar[j+1]) { 
				SWAP(ar[j], ar[j + 1]);
				//인접한 두 값을 비교하며 큰 값을 계속 뒤로 보냄 -> 오름차순 정렬
			}
		}
	}
}
void printArray(int* ar, int n) {
	int i;
	for (i = 0; i < n; i++) {
		printf("%d\n",ar[i]);
	}
}
