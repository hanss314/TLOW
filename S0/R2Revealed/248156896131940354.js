function compare_function(a, b) { // Unlike actually good programming
	return b - a;                // languages, JS sorts by converting
}                               // all array elements to strings. WHY

function product_largest(input) {
	input.sort(compare_function);
	return input[0] * input[1];  // compare_function sorts in reverse
}