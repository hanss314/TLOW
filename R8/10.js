function r8(n) {
  if (n <= -1.5) {
    return -n;
  } else {
    return Math.floor(Math.log2(n+1.5));
  }
}
