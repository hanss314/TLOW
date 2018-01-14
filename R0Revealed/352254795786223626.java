public static char atbash(char c) {
	if (c >= 65 && c <= 90) {
		return (char) (('Z' - c) + 'A');
	}
	else if (c >= 97 && c <= 122) {
		return (char) (('z' - c) + 'a');
	} else {
		return c;
	}
}