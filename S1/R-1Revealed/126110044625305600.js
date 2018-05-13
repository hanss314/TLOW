var a = 0, b = 1, f = 1; console.log(0); for(var i = 2; i <= Infinity; i++) { f = a + b; a = b; b = f; console.log(f); }
