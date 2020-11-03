#include<stdio.h>
#include<stdlib.h>
/*
카운팅정렬(Counting Sort)
*/
void printArray(int* ar, int n) {
	int i;
	for (i = 0; i < n; i++) {
		printf(" %d", ar[i]);
	}
	printf("\n");
}
int main() {
	int n, i, j;
	int* ar, * sorted_ar;
	int count[10001] = { 0 , }; //0~10000 범위의 정수가 입력된다고 가정

	scanf("%d", &n); //배열의 개수
	ar = (int*)malloc(sizeof(int) * n); //길이가 n인 배열 동적할당
	sorted_ar = (int*)malloc(sizeof(int) * n);
	for (i = 0; i < n; i++) {
		scanf("%d", (ar+i));
		count[ar[i]] += 1; //입력받은 값과 같은 인덱스에 +1 count 한다
		//count 배열의 값-> 인덱스와 같은 값을 가지는 정수의 개수
	}

	// 방법 1. 누적합
	for (i = 1; i < 10001; i++) {
		count[i] += count[i - 1]; //값을 누적시키면서 더함
	}
	j = 0;
	for (i = 0; i < 10001; i++) {
		if (j < count[i]) {
			sorted_ar[j] = i;
			j++;
		}
	}

	// 방법 2.
	/*int k = 0;
	for (i = 0; i < 10001; i++) {
		if (count[i] != 0) {
			for (j = 0; j < count[i]; j++) {
				sorted_ar[k] = i;
				k++;
			}
		}
	}*/
	printArray(ar, n); //정렬 전 출력
	printArray(sorted_ar, n); //정렬 후 출력
	return 0;
}
