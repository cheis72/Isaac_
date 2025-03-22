#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void max_min(int* arr, int** max, int** min) {
	int i;
	*max = arr;
	*min = arr;

	for (i = 0; i < 5; i++) {
		if (**max < *(arr + i)) *max = arr + i;
		if (**min > *(arr + i)) *min = arr + i;
	}

	printf("max_add: %p, min_add: %p\nmax_val: %d, min_val: %d", *max, *min, **max, **min);
}

int main(void){
	int* maxPtr, * minPtr;
	int arr[5] = { 3,7,2,5,6 };

	max_min(arr, &maxPtr, &minPtr);

	return 0;
}
