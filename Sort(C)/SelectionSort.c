#include<stdio.h>
#include<stdlib.h>
#define SWAP(a,b) {int t; t=a; a=b; b=t;}

/*
선택정렬은 배열의 길이를 1씩 줄여가면서
최솟값/최댓값을 구해 하나씩 앞으로 빼주는 정렬방식이다.
*/
void selectionSort(int* ar, int n) {
	int i, j, min_idx;
	for (i = 0; i < n - 1; i++) {
		//마지막 숫자는 나머지 숫자들이 정해지면 알아서 정해지므로 N-1
		min_idx = i; //최솟값을 가지는 인덱스
		for (j = i + 1; j < n; j++) { 
			if (ar[j] < ar[min_idx]) { //최솟값 보다 작은 값
				min_idx = j; //최솟값의 인덱스 갱신
			}
		}
		if (i != min_idx) { //ar[i]가 최솟값이 아닐 때
			SWAP(ar[i], ar[min_idx]); // 최솟값을 앞으로 빼줌
		}
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
	selectionSort(ar, n); //정렬
	printArray(ar, n); //출력
	return 0;
}
