public static string Cipher(string input, string code) {
    string rtnStr = ""; int codeIndex = 0; int inInt = 0; int codeInt = 0; int diff = 0; //Varibles.
    for (int i = 0; i < input.Length; i++) {
        inInt = Char.IsLower(input[i]) ? 97 : 65; codeInt = Char.IsLower(code[codeIndex]) ? 97 : 65; //inputInt and codeInt handler.
        diff = (input[i] - inInt) + (code[codeIndex] - codeInt); //difference handler.
        rtnStr = Char.IsLetter(input[i]) ? rtnStr += diff <= 25 ? (char)(diff + inInt):(char)((diff - 26) + inInt) : rtnStr += input[i];
        codeIndex++; if (!(codeIndex < code.Length)) codeIndex = 0; //codeIndex handler.
    }
    return rtnStr;
}
