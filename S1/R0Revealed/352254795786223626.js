function crypt(input, key) {
  var output = "";
  for (var i = 0, j = 0; i < input.length; i++) {
    var c = input.charCodeAt(i);
    if (65 <= c && c <= 90) output += String.fromCharCode((c - 65 + key.toLowerCase().charCodeAt(j % key.length) + 7) % 26 + 65);
    else if (97 <= c && c <= 122) output += String.fromCharCode((c - 97 + key.toLowerCase().charCodeAt(j % key.length) + 7) % 26 + 97);
    else output += input.charAt(i);
    j++;
  } return output;
}
