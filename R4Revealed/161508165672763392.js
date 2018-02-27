function tlow4(array, K, count=0) {
    for (n = 0; n < array.length - K + 1; n ++) {
        if (!array[n]) {
            for (nn = n; nn < n + K; nn ++)
                array[nn] = !array[nn];
            count ++;
        }
    }
    return array.every((n) => n) ? count : -1
}
