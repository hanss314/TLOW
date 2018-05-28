function s1r0(ptext, key) {
  otp = ""; alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for (var i = 0; i < ptext.length; i++) {
    c1 = alpha.indexOf(ptext[i]); c2 = alpha.indexOf(key[i % key.length]) % 26;
    if      (c1 == -1) otp += ptext[i]                   // if non-letter, pass
    else if (c1 <= 25) otp += alpha[(c1 + c2) % 26]      // encode lowercase
    else               otp += alpha[(c1 + c2) % 26 + 26] // encode uppercase
  }
  return otp;
}
