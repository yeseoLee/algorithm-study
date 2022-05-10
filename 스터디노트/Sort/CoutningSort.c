#include<stdio.h>
#include<stdlib.h>
/*
ī��������(Counting Sort)
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
	int count[10001] = { 0 , }; //0~10000 ������ ������ �Էµȴٰ� ����

	scanf("%d", &n); //�迭�� ����
	ar = (int*)malloc(sizeof(int) * n); //���̰� n�� �迭 �����Ҵ�
	sorted_ar = (int*)malloc(sizeof(int) * n);
	for (i = 0; i < n; i++) {
		scanf("%d", (ar+i));
		count[ar[i]] += 1; //�Է¹��� ���� ���� �ε����� +1 count �Ѵ�
		//count �迭�� ��-> �ε����� ���� ���� ������ ������ ����
	}

	// ��� 1. ������
	for (i = 1; i < 10001; i++) {
		count[i] += count[i - 1]; //���� ������Ű�鼭 ����
	}
	j = 0;
	for (i = 0; i < 10001; i++) {
		if (j < count[i]) {
			sorted_ar[j] = i;
			j++;
		}
	}

	// ��� 2.
	/*int k = 0;
	for (i = 0; i < 10001; i++) {
		if (count[i] != 0) {
			for (j = 0; j < count[i]; j++) {
				sorted_ar[k] = i;
				k++;
			}
		}
	}*/
	printArray(ar, n); //���� �� ���
	printArray(sorted_ar, n); //���� �� ���
	return 0;
}
