function atbash(letter) {
	var charcode = letter.charCodeAt(0) // getting letter ascii code
	if (charcode < 65 || (charcode > 90 && charcode < 97) || charcode > 122) {
		return letter; // if isn't letter, return
	} else {
		var letterOffset = charcode <= 90 ? 64 : 96;
		var letterNum = charcode - letterOffset;
		return String.fromCharCode(27 - letterNum + letterOffset);
	}
}

console.log(atbash('a'))
console.log(atbash('B'))
console.log(atbash('1'))
console.log(atbash(';'))