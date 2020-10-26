#include<stdio.h>
#include<stdlib.h>
#define SWAP(a,b) {int t; t=a; a=b; b=t;}

void insertionSort(int* ar, int n) {
	int i, j;
	int key;
	for (j = 1; j < n; j++) {
		key = ar[j];
		i = j - 1;
		while (i >= 0 && ar[i] > key) {
			ar[i + 1] = ar[i];
			i = i - 1;
		}
		ar[i + 1] = key;
	}
}
void printArray(int* ar, int n) {
	int i;
	for (i = 0; i < n; i++) {
		printf("%d\n", ar[i]);
	}
}
int main() {
	int n, i;
	int* ar;
	scanf("%d", &n); //배열의 개수
	ar = (int*)malloc(sizeof(int) * n); //길이가 n인 배열 동적할당
	for (i = 0; i < n; i++) {
		scanf("%d", (ar+i)); 
	}
	insertionSort(ar, n); //정렬
	printArray(ar, n); //출력
	return 0;
}
