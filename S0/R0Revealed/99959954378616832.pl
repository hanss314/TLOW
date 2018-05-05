sub f($s) {
	return chr('A'.ord + 25 - ($s.ord - 'A'.ord)) if 'A' le $s le 'Z';
	return chr('a'.ord + 25 - ($s.ord - 'a'.ord)) if 'a' le $s le 'z';
	return $s;
}
