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
			//key의 앞자리 값이 키값보다 크면
			ar[i + 1] = ar[i];
			i = i - 1;
			//key 보다 더 작은 값이 나올 때까지 한칸씩 이동
		}
		ar[i + 1] = key;
		// key보다 작은값(ar[i]) 앞에, 큰값(ar[i+2]) 뒤에 key 삽입
	}
}
/* 또는
void insertionSort(int* ar, int n) {
	int i, j;
	int key;
	for (j = 1; j < n; j++) {
		key = ar[j]; 
		for (i = j - 1; i >= 0; i--) {
			if (ar[i] > key) { 
				//key의 앞자리 값이 키값보다 크면
				ar[i + 1] = ar[i];
				//key 보다 더 작은 값이 나올 때까지 한칸씩 이동
			}
			else {
				break;
			}
		}
		ar[i + 1] = key;
		// key보다 작은값(ar[i]) 앞에, 큰값(ar[i+2]) 뒤에 key 삽입
	}
}
*/
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

