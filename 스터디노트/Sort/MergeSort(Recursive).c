#include<stdio.h>
#include<stdlib.h>
/*
합병 정렬(merge sort) 
하나의 배열을 두개의 배열로 분할하고, 분할된 배열을 정렬하고,
두개의 정렬된 배열을 합하여 전체가 정렬되도록 하는 정렬 방법
*/
void merge(int* ar, int left,int mid, int right) {
	int i, j, k, l;
	//임시 저장할 배열 동적할당
	int* tmp = (int*)malloc(sizeof(int) * (right + 1));
	i = left;
	j = mid + 1;
	k = left;
	//분할된 두 배열을 비교하여 작은 값부터 tmp에 하나씩 복사
	while (i <= mid && j <= right) {
		if (ar[i] < ar[j]) {
			tmp[k++] = ar[i++];
		}
		else {
			tmp[k++] = ar[j++];
		}
	}
	//두 배열중 남은 한 배열의 나머지 값 전부 붙여넣기
	while (i <= mid) {
		tmp[k++] = ar[i++];
	}
	while (j <= right) {
		tmp[k++] = ar[j++];
	}

	//tmp를 배열 ar로 복사
	for (l = left; l <= right; l++) {
		ar[l] = tmp[l];
	}
	free(tmp);
}
void mergeSort(int* ar, int left,int right) {
	int mid;
	if (left < right) {
		mid = (left + right) / 2;
		mergeSort(ar, left, mid); //절반 나눴을 때 왼쪽
		mergeSort(ar, mid + 1, right); //절반 나눴을 때 오른쪽
		merge(ar, left, mid, right); //정렬된 두 배열 합치기
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
	mergeSort(ar, 0, n - 1); //정렬
	printArray(ar, n); //출력
	return 0;
}
