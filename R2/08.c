int largestProduct(int n[], int size) {
	int l1, l2;
	l1 = l2 = n[0];	
	for (int i = 1; i < size; i++) {
		if (n[i] > l1) {
			l2 = l1;
			l1 = n[i]; 
		} else if (n[i] > l2 && n[i] != l1) l2 = n[i];
	} return l1 * l2;
}