let atbash = (char) => {
  if (char.length > 1) {return "uhoh you bozo, your string is too long"} // if the bozo inputs a string longer than 2
  let code = char.charCodeAt(0); // finds ASCII of character
  if (code < 65) {return char} // not letter
  if (code < 91) {return String.fromCharCode(155-code)} // lowercase case
  if (code < 97) {return char} // not letter
  if (code < 123) {return String.fromCharCode(219-code)} // uppercase case
  return char; // not letter
}

