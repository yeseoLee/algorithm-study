#include<stdio.h>
#include<stdlib.h>
/*
�պ� ����(merge sort) 
�ϳ��� �迭�� �ΰ��� �迭�� �����ϰ�, ���ҵ� �迭�� �����ϰ�,
�ΰ��� ���ĵ� �迭�� ���Ͽ� ��ü�� ���ĵǵ��� �ϴ� ���� ���
*/
void merge(int* ar, int left,int mid, int right) {
	int i, j, k, l;
	//�ӽ� ������ �迭 �����Ҵ�
	int* tmp = (int*)malloc(sizeof(int) * (right + 1));
	i = left;
	j = mid + 1;
	k = left;
	//���ҵ� �� �迭�� ���Ͽ� ���� ������ tmp�� �ϳ��� ����
	while (i <= mid && j <= right) {
		if (ar[i] < ar[j]) {
			tmp[k++] = ar[i++];
		}
		else {
			tmp[k++] = ar[j++];
		}
	}
	//�� �迭�� ���� �� �迭�� ������ �� ���� �ٿ��ֱ�
	while (i <= mid) {
		tmp[k++] = ar[i++];
	}
	while (j <= right) {
		tmp[k++] = ar[j++];
	}

	//tmp�� �迭 ar�� ����
	for (l = left; l <= right; l++) {
		ar[l] = tmp[l];
	}
	free(tmp);
}
void mergeSort(int* ar, int left,int right) {
	int mid;
	if (left < right) {
		mid = (left + right) / 2;
		mergeSort(ar, left, mid); //���� ������ �� ����
		mergeSort(ar, mid + 1, right); //���� ������ �� ������
		merge(ar, left, mid, right); //���ĵ� �� �迭 ��ġ��
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
	scanf("%d", &n); //�迭�� ����
	ar = (int*)malloc(sizeof(int) * n); //���̰� n�� �迭 �����Ҵ�
	for (i = 0; i < n; i++) {
		scanf("%d", (ar+i)); 
	}
	mergeSort(ar, 0, n - 1); //����
	printArray(ar, n); //���
	return 0;
}
